from ..models import taxis
from flask import jsonify

def getTaxis():
    taxis_response = taxis.get()
    response = {"taxis": taxis_response, "count": len(taxis_response)}
    return jsonify(response)