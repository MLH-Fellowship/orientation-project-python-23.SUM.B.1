from datetime import datetime
from typing import Any

import phonenumbers
import pkg_resources
from flask import jsonify
from symspellpy import SymSpell


def validate_date_string(date_string: str) -> bool:
    """
    Summary
    -------
    🍀 `vaidate_date_string` takes a date string as input.
    ✅ It attempts to parse the date string using the strptime method from datetime module
    ✅ The [%B %Y] directives are used to match date's full month name and year respectively.
    ✅ It returns True if the date string format is valid, False otherwise.

    Parameters
    ----------
    date_string (str): date string

    Returns
    -------
    valid (bool): True if the date string format is valid, False otherwise.
    """
    if date_string.lower() in ["present", "now", "current", "till date", "till now"]:
        return True

    try:
        datetime.strptime(date_string, "%B %Y")
        return True

    except ValueError:
        return False


def validate_request(payload: dict[str, Any], required_fields: list[str]) -> bool:
    """
    Summary
    -------
    🍀 `validate_request` takes a payload and a list of required fields as input.
    ✅ It iterates over the list of required fields and checks if each field is present in the payload.
    ✅ It returns True if all the required fields are present in the payload, False otherwise.

    Parameters
    ----------
    payload (dict[str, Any]): payload
    required_fields (list[str]): list of required fields

    Returns
    -------
    valid (bool): True if all the required fields are present in the payload, False otherwise.
    """
    return all(field in payload for field in required_fields)


def validate_proficiency(proficiency: str) -> bool:
    """
    Summary
    -------
    🍀 `validate_proficiency` takes a proficiency string as input.
    ✅ It checks if the proficiency string ends with the `%` character.
    ✅ It attempts to convert the proficiency string to an integer.
    ✅ It returns True if the proficiency string is a valid integer between 0 and 100, False otherwise.

    Parameters
    ----------
    proficiency (str): proficiency string

    Returns
    -------
    valid (bool): True if the proficiency string is a valid integer between 0 and 100, False otherwise.
    """
    if not proficiency.endswith("%"):
        return False

    try:
        proficiency_value = int(proficiency[:-1])

    except ValueError:
        return False

    return 0 <= proficiency_value <= 100


def validate_grade(grade: str) -> bool:
    """
    Summary
    -------
    🍀 `validate_grade` takes a grade string as input.
    ✅ It checks if the grade string is present in the list of valid grades.
    ✅ It returns True if the grade string is valid, False otherwise.

    Parameters
    ----------
    grade (str): grade string

    Returns
    -------
    valid (bool): True if the grade string is a valid grade, False otherwise.
    """
    return grade.upper() in [
        "A+",
        "A",
        "A-",
        "B+",
        "B",
        "B-",
        "C+",
        "C",
        "C-",
        "D+",
        "D",
        "D-",
        "F",
    ]


def check_for_suggestion(value: str) -> tuple[str, int]:
    """
    Check for spelling suggestions using SymSpell.

    Args:
        value: The input value to check for spelling suggestions.

    Returns:
        A tuple containing the suggested value and the number of corrections made.

    Example:
        check_for_suggestion("Hellq there")

    """
    sym_spell = SymSpell(max_dictionary_edit_distance=1, prefix_length=5)
    dictionary_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_dictionary_en_82_765.txt"
    )
    bigram_path = pkg_resources.resource_filename(
        "symspellpy", "frequency_bigramdictionary_en_243_342.txt"
    )
    # term_index is the column of the term and count_index is the
    # column of the term frequency
    sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
    sym_spell.load_bigram_dictionary(bigram_path, term_index=0, count_index=2)

    results = sym_spell.lookup_compound(
        value, max_edit_distance=1, transfer_casing=True
    )

    for result in results:
        print(result)

    parts = str(results[0]).split(",")
    print(parts)
    suggestion = parts[0].lower()
    corrections_made = int(parts[1])

    return (suggestion, corrections_made)


def validate_education(body):
    """Return if education object is valid and if it's not what response and error code should be returned"""
    required_fields = ["course", "school", "start_date", "grade", "logo"]
    if body.get("grade") and not validate_grade(body.get("grade")):
        return (
            False,
            jsonify({"error": "Invalid grade. The grade should be like A+ or F"}),
            400,
        )
    if body.get("start_date") and not validate_date_string(body.get("start_date")):
        return (
            False,
            jsonify({"error": "Invalid start date. Format should be `June 2023`"}),
            400,
        )
    if body.get("end_date") and not validate_date_string(body.get("end_date")):
        return (
            False,
            jsonify({"error": "Invalid end date. Format should be like `June 2023`"}),
            400,
        )
    if not validate_request(body, required_fields):
        return (
            False,
            jsonify({"error": "Invalid request. Required attributes are missing"}),
            400,
        )
    return True, None, None


def validate_experience(body):
    """Validate an experience object and return if it's valid.
    Returns:
        tuple: A tuple containing a boolean value indicating if the experience object is valid,
               a JSON response object with an error message if the object is invalid,
               and an HTTP status code (400) indicating a bad request.
    """

    required_fields = ["title", "company", "start_date", "description", "logo"]
    if body.get("start_date") and not validate_date_string(body.get("start_date")):
        return (
            False,
            jsonify({"error": "Invalid start date. The format should be `June 2023`"}),
            400,
        )
    if body.get("end_date") and not validate_date_string(body.get("end_date")):
        return (
            False,
            jsonify({"error": "Invalid end date. Format should be like `June 2023`"}),
            400,
        )
    if not validate_request(body, required_fields):
        return (
            False,
            jsonify({"error": "Invalid request. Required attributes are missing"}),
            400,
        )
    return True, None, None


def process_sugesstion(
    words: list[str], corrections: list[dict[str, str]]
) -> dict[str, Any]:
    """
    Process spelling suggestions for a list of words.

    Args:
        words (list[str]): The list of words to check for spelling suggestions.
        corrections (list[dict[str, str]]): The list to store the spelling corrections.

    Returns:
        dict[str, Any]: A dictionary containing information about the spelling suggestions.
            - 'message' (str): A message indicating whether suggestions are available.
            - 'suggestions' (list[dict[str, str]]): A list of dictionaries containing spelling suggestions.
                Each dictionary has two keys:
                - 'before' (str): The original word in the content.
                - 'after' (str): The suggested corrected word.
            - 'num_of_corrections_made' (int): The total number of spelling corrections made.
    """
    response_body = {}
    for word in words:
        suggestion, num_of_corrections = check_for_suggestion(word)
        print(f"The suggestions are: {suggestion}")
        print(f"The number of corrections made is: {num_of_corrections}")
        # Add the suggestions to the `suggestions` list
        if num_of_corrections > 0:
            # suggestions.append(suggestion)
            corrections_body = {
                "before": word,
                "after": suggestion,
            }
            corrections.append(corrections_body)
            response_body = {
                "message": "We have a suggestion",
                "suggestions": corrections,
                "num_of_corrections_made": len(corrections),
            }
        else:
            response_body = {
                "message": "We do not any suggestion",
                "suggestions": corrections,
                "num_of_corrections_made": len(corrections),
            }

    return response_body


def is_invalid_content(value: str) -> bool:
    """
    Check if the value is a valid content format.

    Args:
        value (str): The value to check.

    Returns:
        bool: True if the value is an invalid content format, False otherwise.

    Example:
        value = "['Ballr', 'Hellq']"
        is_invalid = is_invalid_content(value)
        print(is_invalid)
    """
    if ("[" not in str(value)) or ("]" not in str(value)):
        return True
    return False


def validate_phone(phone: str) -> bool:
    """
    Validate phone numbers. It ensures that the user is using an international phone number
    """
    try:
        parsed_phone = phonenumbers.parse(phone, None)
        if not phonenumbers.is_valid_number(parsed_phone):
            return False
        return True
    except phonenumbers.NumberParseException:
        return False
