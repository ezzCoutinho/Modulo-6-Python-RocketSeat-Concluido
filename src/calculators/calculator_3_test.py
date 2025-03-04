from typing import Dict, List
from pytest import raises
from src.calculators.calculator_3 import Calculator3

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandlerError():  
  def variance(self, numbers: List[float]) -> float:
    return 3 # apenas para corrigir o error de métodos absctract   

class MockDriverHandler():  
  def variance(self, numbers: List[float]) -> float:
    return 1000000 # apenas para corrigir o error de métodos absctract

def test_calculate_with_variance_error():
  mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
  calculator = Calculator3(MockDriverHandlerError())

  with raises(Exception) as excinfo:
    calculator.calculate(mock_request)

  assert str(excinfo.value) == "Falha no processo: Variance menor que multiplication"

def test_calculate():
  mock_request = MockRequest(body={"numbers": [1, 1, 1, 1, 100]})
  calculator = Calculator3(MockDriverHandler())

  formated_response = calculator.calculate(mock_request)
  print()
  print(formated_response)

  assert isinstance(formated_response, dict)
  assert formated_response == {'data': {'Calculator': 3, 'value': 1000000, 'Success': True}}
