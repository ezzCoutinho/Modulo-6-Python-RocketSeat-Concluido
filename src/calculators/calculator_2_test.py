from typing import Dict, List
from .calculator_2 import Calculator2
from ..drivers.numpy_handler import NumpyHandler
from ..drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

class MockDriverHandler(DriverHandlerInterface):
  
  def standard_derivation(self, numbers: List[float]) -> float:
    return 3
  
  def variance(self, numbers: List[float]) -> float:
    return 2 # apenas para corrigir o error de métodos absctract

def test_calculate_integration():
  mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})

  driver = NumpyHandler()
  calculator = Calculator2(driver)

  formated_response = calculator.calculate(mock_request)
  print()
  print(formated_response)

  assert isinstance(formated_response, dict)
  assert formated_response == {"data": {"Calculator": 2, "result": 0.08}}

def test_calculate():
  mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})

  driver = MockDriverHandler()
  calculator = Calculator2(driver)

  formated_response = calculator.calculate(mock_request)
  print()
  print(formated_response)

  assert isinstance(formated_response, dict)
  assert formated_response == {"data": {"Calculator": 2, "result": 0.33}}