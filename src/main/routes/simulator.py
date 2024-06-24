from flask import Blueprint, jsonify, request
from src.simulator.simulator import Simulator

simulator_route_bp = Blueprint("simulator_route", __name__)

@simulator_route_bp.route('/simulator', methods=['POST'])
def simulator():
    simulator = Simulator()
    response = simulator.simulate(request)

    return jsonify(response), 200