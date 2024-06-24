from flask import Flask
from src.main.routes.simulator import simulator_route_bp

app = Flask(__name__)

app.register_blueprint(simulator_route_bp)