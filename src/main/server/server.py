from flask import Flask
from src.main.server.routes.calculators import calc_route_bp

app = Flask(__name__)

app.register_blueprint(calc_route_bp)