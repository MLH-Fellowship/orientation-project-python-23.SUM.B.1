from flask import jsonify, request

from app import App
from app.data import data
from app.schemas import User
from app.utils import validate_phone, validate_request


@App.route("/user", methods=["GET", "POST"])
@App.put("/user/<user_id>")
def user(user_id: str | None = None):
    """
    Creates a new user.
    Update a user

    Parameters:
        user_id (str): ID of the user to update.

    Request Body:
        {
            "name": "John Doe",
            "phone": "+1234567890",
            "email": "johndoe@example.com"
        }

    Returns:
        Flask Response: JSON response indicating success or failure.
    """
    if request.method == "GET":
        return jsonify(data["user"]), 200

    if request.method == "PUT":
        if user_id:
            # if user is trying to access a specific skill with id=index
            uid = int(user_id)
            if 0 < uid <= len(data["user"]):
                body = request.json
                required_fields = ["name", "phone", "email", "resume_order"]

                name = str(body["name"])
                phone = str(body["phone"])
                email = str(body["email"])
                resume_order = str(body["resume_order"])

                if not validate_phone(phone):
                    return (
                        jsonify(
                            {
                                "error": "Invalid phone number. Please provide a valid international phone number."
                            }
                        ),
                        400,
                    )

                    # update the user in the database.
                    # for now, we fetch the current user based on ID - position in the array = (id - 1)

                a_user = data["user"][uid - 1]  # get user to update

                # update their info
                a_user.name = name
                a_user.phone = phone
                a_user.email = email
                a_user.resume_order = resume_order

                data["user"][uid - 1] = a_user  # add to list
                index = data["user"].index(a_user)

                return (
                    jsonify(
                        {
                            "id": index,
                            "message": "User updated successfully",
                            "body": a_user,
                        }
                    ),
                    201,
                )

        return jsonify({"message": f"User with ID {uid} does not exist"}), 400

    if request.method == "POST":
        body = request.json
        required_fields = ["name", "phone", "email", "resume_order"]

        # ensure that the body has all required params
        if not validate_request(body, required_fields):
            return (
                jsonify(
                    {"error": "Invalid request payload. Required fields are missing."}
                ),
                400,
            )

        name = str(body["name"])
        phone = str(body["phone"])
        email = str(body["email"])
        resume_order = str(body["resume_order"])

        if not validate_phone(phone):
            return (
                jsonify(
                    {
                        "error": "Invalid phone number. Please provide a valid international phone number."
                    }
                ),
                400,
            )

        # Create the user in the database.
        # for now, we add it to a list
        a_user = User(name=name, phone=phone, email=email, resume_order=resume_order)
        data["user"].append(a_user)  # add to list
        index = len(data["user"]) - 1

        return (
            jsonify(
                {
                    "message": "User created successfully",
                    "body": a_user,
                    "id": (index + 1),
                }
            ),
            201,
        )
