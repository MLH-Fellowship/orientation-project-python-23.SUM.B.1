'''
Flask Application
'''
from flask import Flask, jsonify, request

from models import Education, Experience, Skill
from utils import (validate_date_string, validate_grade, validate_proficiency,
                   validate_request)

app = Flask(__name__)
# Validation of required fields
data = {
    "experience": [
        Experience("Software Developer",
                   "A Cool Company",
                   "October 2022",
                   "Present",
                   "Writing Python Code",
                   "example-logo.png")
    ],
    "education": [
        Education("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "80%",
                  "example-logo.png"),
        Education("Computer Science",
                  "Harvard",
                  "October 2019",
                  "June 2024",
                  "70%",
                  "example-logo.png"),
        Education("Cybersecurity", "University of florida",   "August 2016",  "January 2022",      "90%",
                  "example-logo.png")

    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
              "example-logo.png"),
         Skill("Pythonx",
              "1-5 Years",
              "example-logo.png")
    ]
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        return jsonify()

    if request.method == 'POST':
        # Request validation Start
        if request.json is not None:
            body = request.json
            required_fields = ['title', 'company',
                            'start_date', 'description', 'logo']
            if body.get('start_date') and not validate_date_string(body.get('start_date')):
                return jsonify({"error": "Invalid start date. The format should be `June 2023`"}), 400
            if (body.get('end_date') and not validate_date_string(body.get('end_date'))):
                return jsonify({"error": "Invalid end date. Format should be like `June 2023`"}), 400
            if not validate_request(body, required_fields):
                return jsonify({"error": "Invalid request. Required attributes are missing"}), 400
            # Request validation End
            return jsonify({}), 201
    return jsonify({})


@app.route('/resume/education/<index>', methods=['GET', 'POST'])
def education(index):
    '''
    Handles education requests
    '''
    if request.method == 'GET' and index.isnumeric():
        index_num = int(index)
        if 0 < index_num <= len(data["education"]):
            return jsonify(data["education"][index_num - 1])
        return jsonify("Error: Not correct education index")
    if request.method == 'POST':
         # Request validation Start
        if request.json is not None:
            body = request.json
            required_fields = ['course', 'school', 'start_date', 'grade', 'logo']
            error_response = None
            if (body.get('grade') and not validate_grade(body.get('grade'))):
                error_response = {"error": "Invalid grade. The grade should be like A+ or F"}
            elif body.get('start_date') and not validate_date_string(body.get('start_date')):
                error_response = {"error": "Invalid start date. Format should be `June 2023`"}
            elif (body.get('end_date') and not validate_date_string(body.get('end_date'))):
                error_response = {"error": "Invalid end date. Format should be like `June 2023`"}
            elif not validate_request(body, required_fields):
                error_response = {"error": "Invalid request. Required attributes are missing"}
            if error_response:
                return jsonify(error_response), 400
        # Request validation End
        return jsonify({}), 201
    return jsonify("Error: Not correct education index")


@app.route('/resume/education', methods=["GET", "POST"])
def all_education():
    '''Return all education in a list format'''
    if request.method == "POST":
        if request.json is not None:
            body = request.json
            error_response = None
            if(body.get('start_date') and not validate_date_string(body.get('start_date'))):
                error_response = {"error": "Invalid start date. Format should be `June 2023`"}
            elif (body.get('end_date') and not validate_date_string(body.get('end_date'))):
                error_response = {"error": "Invalid end date. Format should be like `June 2023`"}
            elif not validate_request(body, ['course', 'school', 'start_date', 'grade', 'logo']):
                error_response = {"error": "Invalid request. Required attributes are missing"}
            if error_response:
                return jsonify(error_response), 400
            return jsonify({}), 201
    if request.method == "GET":
        return data["education"]
    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
@app.route('/resume/skill/<index>', methods=['GET', 'POST'])
def skill(index=None):
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        if index:
            # if user is trying to access a specific skill with id=index
            skill_index = int(index)
            if  0 < skill_index <= len(data['skill']):
                return jsonify(data['skill'][skill_index - 1]), 200
            return jsonify({'message': f'Skill with ID {skill_index} does not exist'}), 400
        return jsonify(data['skill']), 200

    if request.method == 'POST':
        # handle POST request by adding skill to data dictionary
        if request.json is not None:
            body = request.json
            required_fields = ['name', 'proficiency', 'logo']
            error_response = None

            # validate that the body fields has all required fields and proficiency validation
            if (body.get('proficiency') and not validate_proficiency(body.get('proficiency'))):
                error_response = jsonify({"error": "Invalid proficiency. The proficiency should be like 80%"})
            if not validate_request(body, required_fields):
                error_response = jsonify({"error": "Invalid request. Required attributes are missing"})
            if error_response:
                return error_response, 400
            skill_object = Skill(
                body['name'], body['proficiency'], body['logo'])

            data['skill'].append(skill_object)  # add to list
            index = data['skill'].index(skill_object)

            return jsonify({
                'id': index,
                'message': 'Skill created successfully',
                'body':  data['skill']
            }), 201

    return jsonify({'message': 'Something went wrong'}), 500
