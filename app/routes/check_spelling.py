from ast import literal_eval

from flask import Response, jsonify, request

from app import App
from app.utils import is_invalid_content, process_sugesstion


@App.post("/check-spelling")
def check_spelling() -> tuple[Response, int]:
    """
    Check spelling of the content and provide suggestions.

    Payload:
        {
            "content": "Hellq there"
        }
        content (str): The user input to check for spelling errors.

    Returns:
        Response: A JSON response containing a list of dictionaries. Each dictionary has two keys:
        - 'before' (str): The original word in the content.
        - 'after' (str): The suggested corrected word.

    """
    response_body = {}
    corrections = []

    content = request.json.get("content")  # Get the user input from the request payload

    if is_invalid_content(content):
        return jsonify({"message": "Please pass in the right format for content."}), 400

    contents = literal_eval(content)

    # Perform spelling check based on the section
    response_body = process_sugesstion(words=contents, corrections=corrections)
    return jsonify(response_body), 200
