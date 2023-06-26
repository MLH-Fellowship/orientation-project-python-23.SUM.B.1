from datetime import datetime
from typing import Any


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


def validate_education(body):
    """ Return if education object is valid and if it's not what response and error code should be returned"""
    required_fields = ['course', 'school', 'start_date', 'grade', 'logo']
    if(body.get('grade') and not validate_grade(body.get('grade'))):
        return False, jsonify({"error": "Invalid grade. The grade should be like A+ or F"}), 400
    if body.get('start_date') and not validate_date_string(body.get('start_date')):
        return False, jsonify({"error": "Invalid start date. Format should be `June 2023`"}), 400
    if(body.get('end_date') and not validate_date_string(body.get('end_date'))):
        return False, jsonify({"error": "Invalid end date. Format should be like `June 2023`"}), 400
    if not validate_request(body, required_fields):
        return False, jsonify({"error": "Invalid request. Required attributes are missing"}), 400    
    return True, None, None