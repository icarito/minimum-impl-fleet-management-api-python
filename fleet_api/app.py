from flask import Flask
from fleet_api.controllers.TaxiController import getTaxis

app = Flask(__name__)

@app.route("/taxis")
def getHttpTaxis():
    return getTaxis()