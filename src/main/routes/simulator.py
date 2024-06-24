from flask import Blueprint, jsonify, request

simulator_route_bp = Blueprint("simulator_route", __name__)

@simulator_route_bp.route('/simulator', methods=['POST'])
def simulator():
    response = {"message": "success"}

    return jsonify(response), 200