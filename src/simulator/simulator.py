from typing import Dict
from flask import request as FlaskRequest

class Simulator:
    def simulate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        validated_data = self.__validate_data(body)
        required_value = self.__calc_req_value(5.4, 3.42, validated_data) 
        response = self.__format_response(required_value)
        return response
    
    def __validate_data(self, body: Dict) -> Dict:
        required_keys = {"val_almejado", "hr_trabalhadas", "km/l_g", "km/l_a"}

        if not required_keys.issubset(body):
            raise Exception("Invalid body")

        validated_data = body

        return validated_data
    
    def __calc_req_value(self, g_price: float, a_price: float, validated_data: Dict) -> Dict:
        dist_traveled = 22.4 * float(validated_data["hr_trabalhadas"])

        #Calcula o consumo do veículo
        veh_cons_g = 1 / float(validated_data["km/l_g"])
        veh_cons_a = 1 / float(validated_data["km/l_a"])
            
        #Simula a quantidade de conbustivel consumido
        g_cons = dist_traveled * veh_cons_g
        a_cons = dist_traveled * veh_cons_a

        #Calcula o custo do conbustivel
        cost_g = g_cons * g_price
        cost_a = a_cons * a_price

        #Estima o valor necessario    
        req_value_g = cost_g + validated_data["val_almejado"]
        req_value_a = cost_a + validated_data["val_almejado"]
        required_value = {"cost_g": cost_g, 
                            "cost_a": cost_a, 
                            "req_value_g": req_value_g, 
                            "req_value_a": req_value_a}

        return required_value

    def __format_response(self, required_value: Dict) -> Dict:
            return {
                    "custo_g": round(required_value["cost_g"], 2),
                    "custo_a": round(required_value["cost_a"], 2),
                    "val_necessario_g": round(required_value["req_value_g"], 2),
                    "val_necessario_a": round(required_value["req_value_a"], 2),
                    }
                