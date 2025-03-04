from numpy import std as np, var 
from typing import List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
  def __init__(self):
    self.__np = np
    self.__var = var

  def standard_derivation(self, numbers: List[float]) -> float:
    return self.__np(numbers)
  
  def variance(self, numbers: List[float]) -> float:
    return self.__var(numbers)