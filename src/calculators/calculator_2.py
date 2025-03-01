from flask import request as FlaskRequest
from typing import Dict, List

class Calculator2:

  def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
    body = request.json
    print(body, "body")
    input_data = self.__validate_body(body)
    print(input_data,"input_data")

  def __validate_body(self, body: Dict) -> List[float]:
    if "numbers" not in body:
      raise Exception("body mal formatado!")

    input_data = body["numbers"]
    return [float(i) for i in input_data]