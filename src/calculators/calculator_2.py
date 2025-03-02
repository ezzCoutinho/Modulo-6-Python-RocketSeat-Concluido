from flask import request as FlaskRequest
from typing import Dict, List
from ..drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
  def __init__(self, driver_handler: DriverHandlerInterface) -> None:
    self.__driver_handler = driver_handler

  def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json
    input_data = self.__validate_body(body)
    calculated_number = self.__process_data(input_data)
    response = self.__format_response(calculated_number)
    return response

  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise Exception("body mal formatado!")

    input_data = body["numbers"]
    return [float(i) for i in input_data]
  
  def __process_data(self, input_data: List[float]) -> float:
    first_process_result = [(num * 11) ** 0.95 for num in input_data]
    result = self.standard_derivation(first_process_result)
    return 1/result 
  
  def __format_response(self, calculated_number: float) -> Dict:
    return {
      "data": {
        "Calculator": 2,
        "result": round(calculated_number, 2)
    } }
  
  def standard_derivation(self, numbers: List[float]) -> float:
    return self.__driver_handler.standard_derivation(numbers)