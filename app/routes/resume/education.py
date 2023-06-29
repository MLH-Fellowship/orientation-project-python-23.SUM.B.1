from flask import jsonify, request

from app import App
from app.data import data
from app.utils import validate_date_string, validate_grade, validate_request


@App.route("/resume/education", methods=["GET", "POST"])
@App.route("/resume/education/<index>", methods=["GET", "POST", "DELETE", "PUT"])
def education(index: str | None = None):
    """Return a education based on index, return all educations in the list and add new education to the the list"""
    if request.method == "DELETE" and index is not None and index.isnumeric():
        index_num = int(index)
        return_data = None
        if 0 < index_num <= len(data["education"]):
            del data["education"][index_num - 1]
            return_data = jsonify("Education deleted successfully"), 200
        return_data = jsonify("error: There is no education related to this index")
        return return_data

    if request.method == "GET" and index is None:
        return jsonify(data["education"])
    if request.method == "GET" and index is not None and index.isnumeric():
        index_num = int(index)
        return_data = None
        if 0 < index_num <= len(data["education"]):
            return_data = jsonify(data["education"][index_num - 1])
        return_data = jsonify("error: There is no education related to this index")
        return return_data
    if request.method == "POST":
        # Request validation Start
        if request.json is not None:
            body = request.json
            required_fields = ["course", "school", "start_date", "grade", "logo"]
            error_response = None
            if body.get("grade") and not validate_grade(body.get("grade")):
                error_response = {
                    "error": "Invalid grade. The grade should be like A+ or F"
                }
            elif body.get("start_date") and not validate_date_string(
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
            elif not validate_request(body, required_fields):
                error_response = {
                    "error": "Invalid request. Required attributes are missing"
                }
            if error_response:
                return jsonify(error_response), 400
        # Request validation End
        return jsonify({}), 201
    return jsonify("Error: Not correct education index")
