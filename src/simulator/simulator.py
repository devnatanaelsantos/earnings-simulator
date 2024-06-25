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
        if "val_almejado" not in body or "hr_trabalhadas" not in body:
            raise Exception("Invalid body")
        
        if "km/l_g" in body or "km/l_a" in body:
            validated_data = body

            return validated_data
        
        raise Exception("Invalid body")
    
    def __calc_req_value(self, g_price: float, a_price: float, validated_data: Dict) -> Dict:
        #Simula a distância percorrida com base na velocidade média de circulação dos veículos em sp (22,4 km/h) e na quantidade de horas trabalhadas
        dist_traveled = 22.4 * float(validated_data["hr_trabalhadas"])

        if "km/l_g" in validated_data and "km/l_a" in validated_data:
            #Calcula o consumo de conbustíve por km percorrido
            g_veh_cons = 1 / float(validated_data["km/l_g"])
            a_veh_cons = 1 / float(validated_data["km/l_a"])
                
            #Calcula o consumo total de conbustível com base na distância percorrida
            g_cons = dist_traveled * g_veh_cons
            a_cons = dist_traveled * a_veh_cons

            #Calcula o custo total de conbustível
            g_cost = g_cons * g_price
            a_cost = a_cons * a_price

            #Estima o valor necessario a acumular para obter o valor almejado
            g_req_value = g_cost + validated_data["val_almejado"]
            a_req_value = a_cost + validated_data["val_almejado"]
            
            required_value = {"cost_g": g_cost,
                                "cost_a": a_cost, 
                                "req_value_g": g_req_value, 
                                "req_value_a": a_req_value
                                }

            return required_value
           
        elif "km/l_g" in validated_data:
            g_veh_cons = 1 / float(validated_data["km/l_g"])

            g_cons = dist_traveled * g_veh_cons

            g_cost = g_cons * g_price

            g_req_value = g_cost + validated_data["val_almejado"]

            required_value = {"cost_g": g_cost, 
                                "req_value_g": g_req_value 
                                }
            
            return required_value
        
        else:
            a_veh_cons = 1 / float(validated_data["km/l_a"])

            a_cons = dist_traveled * a_veh_cons

            a_cost = a_cons * a_price

            a_req_value = a_cost + validated_data["val_almejado"]

            required_value = {"cost_a": a_cost, 
                                "req_value_a": a_req_value
                                }
        
            return required_value

    def __format_response(self, required_value: Dict) -> Dict:
            if "cost_g" in required_value and "cost_a" in required_value:
                return {
                    "custo_g": round(required_value["cost_g"], 2),
                    "custo_a": round(required_value["cost_a"], 2),
                    "val_necessario_g": round(required_value["req_value_g"], 2),
                    "val_necessario_a": round(required_value["req_value_a"], 2),
                    }
            
            elif "cost_g" in required_value:
                return {
                    "custo_g": round(required_value["cost_g"], 2),
                    "val_necessario_g": round(required_value["req_value_g"], 2),
                    }
            
            else:
                return {
                    "custo_a": round(required_value["cost_a"], 2),
                    "val_necessario_a": round(required_value["req_value_a"], 2),
                    }