'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill
from utils import validate_date_string, validate_grade, validate_proficiency, validate_request


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
                  "example-logo.png")
    ],
    "skill": [
        Skill("Python",
              "1-2 Years",
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
        body = request.json
        required_fields = ['title', 'company', 'start_date', 'description', 'logo']
        if body.get('start_date') and not validate_date_string(body.get('start_date')):
            return jsonify({"error": "Invalid start date. The format should be `June 2023`"}), 400
        if(body.get('end_date') and not validate_date_string(body.get('end_date'))):
            return jsonify({"error": "Invalid end date. Format should be like `June 2023`"}), 400
        if not validate_request(body, required_fields):
            return jsonify({"error": "Invalid request. Required attributes are missing"}), 400
        # Request validation End
        return jsonify({}), 201
    return jsonify({})

@app.route('/resume/education', methods=['GET', 'POST'])
def education():
    '''
    Handles education requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        # Request validation Start
        body = request.json
        required_fields = ['course', 'school', 'start_date', 'grade', 'logo']
        if(body.get('grade') and not validate_grade(body.get('grade'))):
            return jsonify({"error": "Invalid grade. The grade should be like A+ or F"}), 400
        if body.get('start_date') and not validate_date_string(body.get('start_date')):
            return jsonify({"error": "Invalid start date. Format should be `June 2023`"}), 400
        if(body.get('end_date') and not validate_date_string(body.get('end_date'))):
            return jsonify({"error": "Invalid end date. Format should be like `June 2023`"}), 400
        if not validate_request(body, required_fields):
            return jsonify({"error": "Invalid request. Required attributes are missing"}), 400
        # Request validation End
        return jsonify({}), 201

    return jsonify({})


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        body = request.json
        required_fields = ['name', 'proficiency', 'logo']
        if(body.get('proficiency') and not validate_proficiency(body.get('proficiency'))):
            return jsonify({"error": "Invalid proficiency format.Format should look like 82%"}), 400
        if not validate_request(body, required_fields):
            return jsonify({"error": "Invalid request payload. Attributes are missing"}), 400
        return jsonify({}), 201

    return jsonify({})
