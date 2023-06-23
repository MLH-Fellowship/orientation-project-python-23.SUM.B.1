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
@app.route('/resume/education/<index>', methods=['GET', 'POST'])
def education(index=None):
    """ Return a education based on index, return all educations in the list,"""
      
    if request.method == 'GET' and index is None:
        return jsonify(data["education"]) 
    elif request.method == 'GET' and index.isnumeric():        
        index_num = int(index)
        if index_num > 0 and index_num <= len(data["education"]):
            return jsonify(data["education"][index_num - 1])
        else:
            return jsonify("Error: There is no education related to this index")   
    
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
        data['education'].append(body)
        new_education_index = len(data["education"]) -1
        return jsonify({"id": new_education_index})
       
    return jsonify("Error: Not correct education index")  


@app.route('/resume/skill', methods=['GET', 'POST'])
@app.route('/resume/skill/<index>', methods=['GET', 'POST'])
def skill(index=None):
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        if index:
            # if user is trying to access a specific skill with id=index
            id = int(index)
            if id > 0 and id <= len(data['skill']):
                return jsonify(data['skill'][id - 1]), 200
            else:
                return jsonify({'message': f'Skill with ID {id} does not exist'}), 400
        else:
            return jsonify(data['skill']), 200

    if request.method == 'POST':
        # handle POST request by adding skill to data dictionary
        body = request.json
        required_fields = ['name', 'proficiency', 'logo']
        
        # validate that the body fields has all required fields and proficiency validation
        if(body.get('proficiency') and not validate_proficiency(body.get('proficiency'))):
            return jsonify({"error": "Invalid proficiency format.Format should look like 82%"}), 400
        if not validate_request(body, required_fields):
            return jsonify({"error": "Invalid request payload. Attributes are missing"}), 400
        else:
            skill = Skill(body['name'], body['proficiency'], body['logo'])

            data['skill'].append(skill) # add to list
            index = data['skill'].index(skill)

            return jsonify({
            'id': index,
            'message': 'Skill created successfully',
            'body':  data['skill']
        }), 201

    return jsonify({'message':'Something went wrong'}), 500
    
