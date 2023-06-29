from flask import jsonify, request

from app import App
from app.data import data
from app.utils import validate_date_string, validate_request


@App.route("/resume/education", methods=["GET", "POST"])
def all_education():
    """Return all education in a list format"""
    if request.method == "POST":
        if request.json is not None:
            body = request.json
            error_response = None
            if body.get("start_date") and not validate_date_string(
                body.get("start_date")
            ):
                error_response = {
                    "error": "Invalid start date. Format should be `June 2023`"
                }
            elif body.get("end_date") and not validate_date_string(
                body.get("end_date")
            ):
                error_response = {
                    "error": "Invalid end date. Format should be like `June 2023`"
                }
            elif not validate_request(
                body, ["course", "school", "start_date", "grade", "logo"]
            ):
                error_response = {
                    "error": "Invalid request. Required attributes are missing"
                }
            if error_response:
                return jsonify(error_response), 400
            return jsonify({}), 201

    return data["education"]
