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
    
    def __calc_req_value(self, gas_price: float, alc_price: float, validated_data: Dict) -> Dict:
        #Simula a distância percorrida com base na velocidade média de circulação dos veículos em sp (22,4 km/h) e na quantidade de horas trabalhadas
        dist_traveled = 22.4 * float(validated_data["hr_trabalhadas"])

        if "km/l_g" in validated_data and "km/l_a" in validated_data:
            #Calcula o consumo de conbustíve por km percorrido
            gas_veh_cons = 1 / float(validated_data["km/l_g"])
            alc_veh_cons = 1 / float(validated_data["km/l_a"])
                
            #Calcula o consumo total de conbustível com base na distância percorrida
            gas_cons = dist_traveled * gas_veh_cons
            alc_cons = dist_traveled * alc_veh_cons

            #Calcula o custo total de conbustível
            gas_cost = gas_cons * gas_price
            alc_cost = alc_cons * alc_price

            #Estima o valor necessario a acumular para obter o valor almejado
            gas_req_value = gas_cost + validated_data["val_almejado"]
            alc_req_value = alc_cost + validated_data["val_almejado"]
            
            required_value = {"cost_gas": gas_cost,
                                "cost_alc": alc_cost, 
                                "req_value_gas": gas_req_value, 
                                "req_value_alc": alc_req_value
                                }

            return required_value
           
        elif "km/l_g" in validated_data:
            gas_veh_cons = 1 / float(validated_data["km/l_g"])
            gas_cons = dist_traveled * gas_veh_cons
            gas_cost = gas_cons * gas_price
            gas_req_value = gas_cost + validated_data["val_almejado"]
            required_value = {"cost_gas": gas_cost, 
                                "req_value_gas": gas_req_value 
                                }
            
            return required_value
        
        else:
            alc_veh_cons = 1 / float(validated_data["km/l_a"])
            alc_cons = dist_traveled * alc_veh_cons
            alc_cost = alc_cons * alc_price
            alc_req_value = alc_cost + validated_data["val_almejado"]
            required_value = {"cost_alc": alc_cost, 
                                "req_value_alc": alc_req_value
                                }
        
            return required_value

    def __format_response(self, required_value: Dict) -> Dict:
            if "cost_gas" in required_value and "cost_alc" in required_value:
                return {
                    "custo_gas": round(required_value["cost_gas"], 2),
                    "custo_alc": round(required_value["cost_alc"], 2),
                    "val_necessario_gas": round(required_value["req_value_gas"], 2),
                    "val_necessario_alc": round(required_value["req_value_alc"], 2),
                    }
            
            elif "cost_gas" in required_value:
                return {
                    "custo_gas": round(required_value["cost_gas"], 2),
                    "val_necessario_gas": round(required_value["req_value_gas"], 2),
                    }
            
            else:
                return {
                    "custo_alc": round(required_value["cost_alc"], 2),
                    "val_necessario_alc": round(required_value["req_value_alc"], 2),
                    }