from typing import Dict
from .calculator_1 import Calculator1

class MockRequest:
  def __init__(self, body: Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest(body={"number": 1})
  calculator = Calculator1()

  response =  calculator.calculate(mock_request)
  print()
  print(response)

  assert "data" in response
  assert "Calculator" in response["data"]
  assert "result" in response["data"]
  print("Retorno dos tipos OK!")
  assert response == {
    "data": {
      "Calculator": 1,
      "result": 14.25
    }
  }