import pytest
from typing import Dict
from .simulator import Simulator

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

@pytest.fixture
def simulator():
    return Simulator()

def test_simulate_with_all_parameters(simulator):
    mock_request = MockRequest({"val_almejado": 2000,
                                "hr_trabalhadas": 36,
                                "km/l_g": 11.5,
                                "km/l_a": 7.9
                                })

    response = simulator.simulate(mock_request)
    
    assert "custo_alc" in response 
    assert "custo_gas" in response
    assert "val_necessario_gas" in response
    assert "val_necessario_alc" in response
    assert response["custo_gas"] == 378.66
    assert response["custo_alc"] == 349.1
    assert response["val_necessario_gas"] == 2378.66
    assert response["val_necessario_alc"] == 2349.1

def test_simulate_with_gas_only(simulator):
    mock_request = MockRequest({"val_almejado": 2000,
                                "hr_trabalhadas": 36,
                                "km/l_g": 11.5
                                })

    response = simulator.simulate(mock_request)
    
    assert "custo_gas" in response
    assert response["custo_gas"] == 378.66
    assert response["val_necessario_gas"] == 2378.66    

def test_simulate_with_alc_only(simulator):
    mock_request = MockRequest({"val_almejado": 2000,
                                "hr_trabalhadas": 36,
                                "km/l_a": 7.9
                                })
    
    response = simulator.simulate(mock_request)
    
    assert "custo_alc" in response
    assert response["custo_alc"] == 349.1
    assert response["val_necessario_alc"] == 2349.1
