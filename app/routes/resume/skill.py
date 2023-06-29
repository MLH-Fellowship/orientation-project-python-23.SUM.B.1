from flask import jsonify, request

from app import App
from app.data import data
from app.schemas import Skill
from app.utils import validate_proficiency, validate_request


@App.route("/resume/skill", methods=["GET", "POST"])
@App.route("/resume/skill/<index>", methods=["GET", "POST", "PUT", "DELETE"])
def skill(index: str | None = None):
    """
    Handles Skill requests.

    Parameters:
        index (int): Index of the skill to access or delete (optional).

    Returns:
        Flask Response: JSON response containing skill information or an error message.

    """
    if request.method == "DELETE":
        # handle DELETE request by deleting skill with id=index
        if index:
            skill_index = int(index)
            if 0 < skill_index <= len(data["skill"]):
                deleted_item = data["skill"][skill_index - 1]
                del data["skill"][skill_index - 1]
                return (
                    jsonify(
                        {
                            "message": "Skill deleted successfully",
                            "status": "success",
                            "deleted_item": deleted_item,
                        }
                    ),
                    200,
                )
        else:
            return jsonify({"message": "Invalid request"}), 400

    if request.method == "GET":
        return_data = None
        if index:
            # if user is trying to access a specific skill with id=index
            skill_index = int(index)
            if 0 < skill_index <= len(data["skill"]):
                return_data = jsonify(data["skill"][skill_index - 1]), 200
            return_data = (
                jsonify({"message": f"Skill with ID {skill_index} does not exist"}),
                400,
            )
        return_data = jsonify(data["skill"]), 200
        return return_data

    if request.method == "PUT":
        if index:
            # if user is trying to access a specific skill with id=index
            skill_id = int(index)
            if 0 < skill_id <= len(data["skill"]):
                body = request.json
                required_fields = ["name", "proficiency", "logo"]

                name = body["name"]
                proficiency = body["proficiency"]
                logo = body["logo"]

                # update the skill in the database.
                # for now, we fetch the current user based on ID - position in the array = (id - 1)

                a_skill = data["skill"][skill_id - 1]  # get user to update

                # update their info
                a_skill.name = name
                a_skill.proficiency = proficiency
                a_skill.logo = logo

                data["skill"][skill_id - 1] = a_skill  # add to list
                index = data["skill"].index(a_skill)

                return (
                    jsonify(
                        {
                            "id": index,
                            "message": "Skill updated successfully",
                            "body": a_skill,
                        }
                    ),
                    201,
                )

        return jsonify({"message": f"Skill with ID {skill_id} does not exist"}), 400

    if request.method == "POST":
        # handle POST request by adding skill to data dictionary
        if request.json is not None:
            body = request.json
            required_fields = ["name", "proficiency", "logo"]
            error_response = None

            # validate that the body fields has all required fields and proficiency validation
            if body.get("proficiency") and not validate_proficiency(
                body.get("proficiency")
            ):
                error_response = jsonify(
                    {"error": "Invalid proficiency. The proficiency should be like 80%"}
                )
            if not validate_request(body, required_fields):
                error_response = jsonify(
                    {"error": "Invalid request. Required attributes are missing"}
                )
            if error_response:
                return error_response, 400
            skill_object = Skill(body["name"], body["proficiency"], body["logo"])

            data["skill"].append(skill_object)  # add to list
            index = data["skill"].index(skill_object)

            return (
                jsonify(
                    {
                        "id": index,
                        "message": "Skill created successfully",
                        "body": data["skill"],
                    }
                ),
                201,
            )
    return jsonify({"message": "Something went wrong"}), 500
