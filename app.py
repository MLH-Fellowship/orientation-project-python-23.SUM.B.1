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
                  "example-logo.png"),
        Education("Computer Science", 
                  "Harvard", 
                  "October 2019", 
                  "June 2024", 
                  "70%", 
                  "example-logo.png"),
        Education("Cybersecurity", 
                  "University of florida", 
                  "August 2016", 
                  "January 2022", 
                  "90%", 
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
    Returns a JSON test message.

    Returns:
        A JSON response with a test message.
    '''
    return jsonify({"message": "Hello, World!"})


@app.route('/resume/experience', methods=['GET', 'POST'])
def experience():
    '''
    Handles experience requests.

    GET:
        Returns an empty JSON response.

    POST:
        Creates a new experience entry based on the provided data.

        Returns:
            A JSON response indicating the status of the operation.
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

@app.route('/resume/education/<index>', methods=['GET', 'POST'])
def education(index):
    '''
    Handles education requests.

    GET:
        Retrieves the education entry at the specified index.

        Parameters:
            index (str): The index of the education entry.

        Returns:
            A JSON response containing the education entry.

    POST:
        Creates a new education entry based on the provided data.

        Parameters:
            index (str): The index of the education entry.

        Returns:
            A JSON response indicating the status of the operation.
    '''  
    if request.method == 'GET' and index.isnumeric():        
        index_num = int(index)
        if index_num > 0 and index_num <= len(data["education"]):
            return jsonify(data["education"][index_num - 1])
        else:
            return jsonify("Error: Not correct education index")  
    
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
       
    return jsonify("Error: Not correct education index")  

@app.route('/resume/education', methods=["GET"])
def all_education():
    '''
    Returns all education entries in a list format.

    Returns:
        A JSON response containing all education entries.
    '''
    
    if request.method == "GET":                                             
        return data["education"]


@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles skill requests.

    GET:
        Returns an empty JSON response.

    POST:
        Creates a new skill entry based on the provided data.

        Returns:
            A JSON response indicating the status of the operation.
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
