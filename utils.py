from datetime import datetime

'''
validate_date_string
🍀 `vaidate_date_string` takes a date string as input.
✅ It attempts to parse the date string using the strptime method from datetime module
✅ The [%B %Y] directives are used to match date's full month name and year respectively.
✅ It returns True if the date string format is valid, False otherwise.

'''
def validate_date_string(date_string):
    if date_string.lower() in ["present", "now", "current", "till date", "till now"]:
        return True
    try:
        datetime.strptime(date_string, "%B %Y")
        return True
    except ValueError:
        return False
'''
validate_request
🍀 `validate_request` takes a payload and a list of required fields as input.
✅ It iterates over the list of required fields and checks if each field is present in the payload.
✅ It returns True if all the required fields are present in the payload, False otherwise.
'''
def validate_request(payload, required_fields) -> bool:
    for field in required_fields:
        if field not in payload:
            return False
    return True


'''
validate_proifciency
🍀 `validate_proficiency` takes a proficiency string as input.
✅ It checks if the proficiency string ends with the `%` character.
✅ It attempts to convert the proficiency string to an integer.
✅ It returns True if the proficiency string is a valid integer between 0 and 100, False otherwise.
'''
def validate_proficiency(proficiency)-> bool:
    if proficiency.endswith('%'):
        proficiency_value = proficiency[:-1]
        try:
            proficiency_value = int(proficiency_value)
            if proficiency_value >= 0 and proficiency_value <= 100:
                return True
        except ValueError:
            pass
    return False

'''
validate_grade
🍀 `validate_grade` takes a grade string as input.
✅ It checks if the grade string is present in the list of valid grades.
✅ It returns True if the grade string is valid, False otherwise.
'''
def validate_grade(grade):
    valid_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "F"]
    if grade.upper() in valid_grades:
        return True
    return False
