from flask import Flask, request, jsonify
from fleet_api.controllers.TaxiController import getTaxis
from .config import Config

DEFAULT_PAGE = 1
ROWS_PER_PAGE = 10
DEFAULT_PLATE = "";

def create_app() -> Flask:
    
    app = Flask(__name__)

    @app.route("/taxis")
    def getHttpTaxis():
        page = request.args.get("page", DEFAULT_PAGE, type=int)
        per_page = request.args.get("limit", ROWS_PER_PAGE, type=int)

        if page < 0 or per_page < 0:
            message = { 'message': 'The page number and limit cannot be less than 0' };
            return jsonify(message), 400

        plate = request.args.get("plate", DEFAULT_PLATE, type=None)
        return getTaxis(page, per_page, plate)

    return app

if __name__ == "__main__":
    taxi_app = create_app()
    taxi_app.run()
