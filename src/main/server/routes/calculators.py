from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calc_route_bp = Blueprint("calc_routes", __name__)

@calc_route_bp.route("/calculator/1", methods=["POST"])
def calculator_1():
  calc = Calculator1()
  response = calc.calculate(request)

  return jsonify(response), 200

@calc_route_bp.route("/calculator/2", methods=["POST"])
def calculator_2():
  return jsonify({"data": "Calculadora 2 a todo vapor!"}), 200