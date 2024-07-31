from ..models import taxis
from flask import jsonify

def getTaxis(page, per_page, plate):
    taxis_response = taxis.get(page, per_page, plate)
    response = {"taxis": taxis_response, "count": len(taxis_response)}
    return jsonify(response)