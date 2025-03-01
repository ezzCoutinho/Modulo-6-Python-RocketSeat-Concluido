from typing import Dict
from pytest import raises
from .calculator_2 import Calculator2

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest(body={"numbers": [2.12, 4.54, 5.67]})
  calculator = Calculator2()

   
  