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
                  "A+",
                  "example-logo.png"),
        Education("Computer Science",
                  "Harvard", 
                  "October 2019", 
                  "June 2024", 
                  "B-", 
                  "example-logo.png"),
        Education("Cybersecurity",
                  "University of florida", 
                  "August 2016", 
                  "January 2022", 
                  "C+", 
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
@app.route('/resume/experience/<index>', methods=['GET', 'POST'])
def experience(index = None):
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        if index:
            if str(index).isnumeric():
                expId = int(index)
                if 1 <= expId <= len(data['experience']):
                    return jsonify(data['experience'][expId-1]), 200
                else:
                    return jsonify({"message": "Invalid experience ID"}), 400
            else:
                return jsonify({"message": "Invalid experience ID"}), 400
        else:
            return jsonify(data['experience']), 200

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
@app.route('/resume/education/<index>', methods=['GET', 'POST', 'DELETE'])
def education(index=None):
    """ Return a education based on index, return all educations in the list and add new education to the the list"""

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

    if request.method == 'DELETE':
        id = int(index)        
        del data['education'][id - 1]         

    return jsonify("Error: Not correct education index") 

    #todo:
    # Delete existing Education #9
    # Using a DELETE request for the /resume/education route, delete an existing Education using its index position as an ID.
    # As part of this, you should write a test in test_pytest.py to show it works.



@app.route('/resume/skill', methods=['GET', 'POST'])
@app.route('/resume/skill/<index>', methods=['GET', 'POST', 'DELETE'])
def skill(index=None):
    '''
    Handles Skill requests.

    Parameters:
        index (int): Index of the skill to access or delete (optional).

    Returns:
        Flask Response: JSON response containing skill information or an error message.

    '''
    if request.method == 'GET':
        if index:
            # if user is trying to access a specific skill with skill_id=index
            skill_id = int(index)
            if skill_id > 0 and skill_id <= len(data['skill']):
                return jsonify(data['skill'][skill_id - 1]), 200
            return jsonify({'message': f'Skill with ID {skill_id} does not exist'}), 400
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
        a_skill = Skill(body['name'], body['proficiency'], body['logo'])

        data['skill'].append(a_skill) # add to list
        index = data['skill'].index(a_skill)

        return jsonify({
        'id': index,
        'message': 'Skill created successfully',
        'body':  data['skill']
    }), 201

    if request.method == 'DELETE':
        # handle delete requests
        if index:
            # if user is trying to access a specific skill with skill_id=index
            skill_id = int(index)
            if skill_id > 0 and skill_id <= len(data['skill']):
                # remove (skill_id - 1) from the list
                # if the user passes 1 to the url, then they want to remove the first skill record
                deleted_item = data['skill'].pop((skill_id - 1))
                return jsonify({'status':'success', 'message': 'Skill deleted successfully','deleted_item':deleted_item}), 200
            return jsonify({'message': f'Skill with ID {skill_id} does not exist'}), 400

    return jsonify({'message':'Something went wrong'}), 500
