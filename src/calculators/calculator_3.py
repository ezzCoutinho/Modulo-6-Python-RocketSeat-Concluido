from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
class Calculator3:
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler

  def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json
    input_data = self.__validate_body(body)
    formated_response = self.__format_response()
    
  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise Exception("body mal formatado!")
    
  def __format_response(self, calculated_number: float) -> Dict:
    return {
      "data": {
        "Calculator": 3,
        "result": round(calculated_number, 2)
    } }
  