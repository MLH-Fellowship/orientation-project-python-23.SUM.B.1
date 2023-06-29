from flask import jsonify, request

from app import App
from app.data import data
from app.schemas import Experience
from app.utils import validate_experience


@App.route("/resume/experience", methods=["GET", "POST"])
@App.route("/resume/experience/<index>", methods=["GET", "POST", "DELETE", "PUT"])
def experience(index: str | None = None):
    """
    Handle experience requests
    """
    if request.method == "GET":
        return_data = None
        if index:
            if str(index).isnumeric():
                exp_id = int(index)
                if 1 <= exp_id <= len(data["experience"]):
                    return_data = jsonify(data["experience"][exp_id - 1]), 200
                return_data = jsonify({"message": "Invalid experience ID"}), 400
        return_data = jsonify(data["experience"]), 200
        return return_data

    if request.method == "POST":
        # Request validation Start
        body = request.json
        is_valid, result_response, code = validate_experience(body)
        if not is_valid:
            return result_response, code
        # Request validation End

        # Extract the required attributes from the data
        title = body.get("title")
        company = body.get("company")
        start_date = body.get("start_date")
        end_date = body.get("end_date")
        description = body.get("description")
        logo = body.get("logo")

        # Create a new instance of the Experience class
        new_experience = Experience(
            title, company, start_date, end_date, description, logo
        )
        data["experience"].append(new_experience)
        return (
            jsonify(
                {
                    "message": "New experience successfully created",
                    "id": len(data["experience"]) - 1,
                }
            ),
            201,
        )
    if request.method == "DELETE":
        if index and str(index).isnumeric():
            exp_id = int(index)
            if 1 <= exp_id <= len(data["experience"]):
                data["experience"].pop((exp_id - 1))
                return (
                    jsonify(
                        {
                            "message": f"Experience with id {exp_id} has been successfully deleted"
                        }
                    ),
                    200,
                )
            else:
                return jsonify({"error": "Invalid experience id"}), 400

        else:
            return jsonify({"error": "Invalid experience id"}), 400

    if request.method == "PUT":
        if index and str(index).isnumeric():
            exp_id = int(index)
            body = request.json

            # Request validation
            body = request.json
            is_valid, result_response, code = validate_experience(body)
            if not is_valid:
                return result_response, code
            # Request validation End

            if 1 <= exp_id <= len(data["experience"]):
                data["experience"][exp_id - 1] = body
                return (
                    jsonify(
                        {
                            "message": f"Experience with id {exp_id} has been successfully updated",
                            "Updated data": data["experience"][exp_id - 1],
                        }
                    ),
                    201,
                )
            else:
                return jsonify({"error": f"Experience with id {exp_id} not found"}), 404
        else:
            return jsonify({"error": "Invalid experience ID"}), 400

    return jsonify({"message": "Something went wrong"}), 500
