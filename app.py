'''
Flask Application
'''
import phonenumbers
from flask import Flask, jsonify, request

from models import Education, Experience, Skill, User
from utils import (validate_date_string, validate_grade, validate_proficiency,
                   validate_request, validate_education)

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
              "example-logo.png")],
    "user":[
        User(name='Akin Friday', phone='+2348050780750',email='akinfriday@example.com', resume_order='[1,2,3]')
    ],
}


@app.route('/test')
def hello_world():
    '''
    Returns a JSON test message
    '''
    return jsonify({"message": "Hello, World!"})

@app.route('/resume/experience', methods=['GET', 'POST'])
@app.route('/resume/experience/<index>', methods=['GET', 'POST','DELETE','pUT'])
def experience(index = None):
    '''
    Handle experience requests
    '''
    if request.method == 'GET':
        if index:
            if str(index).isnumeric():
                exp_id = int(index)
                if 1 <= exp_id <= len(data['experience']):
                    return jsonify(data['experience'][exp_id-1]), 200
                else:
                    return jsonify({"message": "Invalid experience ID"}), 404
            else:
                return jsonify({"message": "Invalid experience ID"}), 404
        else:
            return jsonify(data['experience']), 201

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

        # Extract the required attributes from the data
        title = body.get('title')
        company = body.get('company')
        start_date = body.get('start_date')
        end_date = body.get('end_date')
        description = body.get('description')
        logo = body.get('logo')

        # Create a new instance of the Experience class
        new_experience = Experience(title, company, start_date, end_date, description, logo)
        
        data['experience'].append(new_experience)
        return jsonify({
            "message": "New experience successfully created",
            "id": len(data['experience']) -1
            }), 201
    if request.method == 'DELETE':
        if index and str(index).isnumeric():
                expId = int(index)
                if 1 <= expId <= len(data['experience']):
                    data['experience'].pop((expId - 1))
                    return jsonify({"message":f"Experience with id {expId} has been successfully deleted"}), 200
                else:
                    return jsonify({"error": "Invalid experience id"}), 400
                
        else:
            return jsonify({"error": "Invalid experience id"}), 400

    if request.method == 'PUT':
        if index and str(index).isnumeric():
            exp_id = int(index)
            body = request.json

            # Find the experience to edit
            experience = None

            # Request validation
            required_fields = ['title', 'company', 'start_date', 'description', 'logo']
            if body.get('start_date') and not validate_date_string(body.get('start_date')):
                return jsonify({"error": "Invalid start date. The format should be `June 2023`"}), 400
            if(body.get('end_date') and not validate_date_string(body.get('end_date'))):
                return jsonify({"error": "Invalid end date. Format should be like `June 2023`"}), 400
            if not validate_request(body, required_fields):
                return jsonify({"error": "Invalid request. Required attributes are missing"}), 400
            # Request validation End

            if 1 <= exp_id <= len(data['experience']):
                    data['experience'][exp_id-1] = body
                    return jsonify({
                    "message": f"Experience with id {exp_id} was successfully updated",
                    "Updated data": data['experience'][exp_id-1]
                    }), 201
            else:
                return jsonify({"error": f"Experience with id {exp_id} not found"}), 404
        else:
            return jsonify({"error": "Invalid experience ID"}), 400

    return jsonify({})



@app.route('/resume/education', methods=['GET', 'POST'])
@app.route('/resume/education/<index>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def education(index=None):
    """ Return a education based on index, return all educations in the list and add new education to the the list"""    
    if request.method == 'GET' and index is None:
        return jsonify(data["education"]) 
    elif request.method == 'GET' and index.isnumeric():        
        index_num = int(index)
        if index_num > 0 and index_num <= len(data["education"]):
            return jsonify(data["education"][index_num - 1])
        else:
            return jsonify({"Error": "There is no education related to this index"})
        
    if request.method == 'POST':
        # Request validation Start
        body = request.json
        is_valid, result_response, code = validate_education(body)
        if not is_valid:
            return result_response, code           

        data['education'].append(body)
        new_education_index = len(data["education"])
        return jsonify({"id": new_education_index}), 201    
    
    if request.method == 'PUT':
        if index:
            id = int(index) -1
            body = request.json
            is_valid, result_response, code = validate_education(body)
            if not is_valid:
                return result_response, code 
            if id < len(data['education']):                                          
                data['education'][id] = body                
                return jsonify({'id': id + 1}), 200   
            else:                 
                data['education'].append(body)
                new_education_id = len(data["education"])
                return jsonify({"id": new_education_id}), 201   

    if request.method == 'DELETE':
        id = int(index)        
        deleted_education = data['education'].pop((id - 1))        
        return jsonify({'message':f'Education {deleted_education.course} successfully deleted'})    

    return jsonify({"message":"Error: Not correct education index"})

@app.route('/resume/skill', methods=['GET', 'POST'])
@app.route('/resume/skill/<index>', methods=['GET', 'POST', 'PUT', 'DELETE'])
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
            if 0 < skill_id <= len(data['skill']):
                return jsonify(data['skill'][skill_id - 1]), 200
            return jsonify({'message': f'Skill with ID {skill_id} does not exist'}), 400
        return jsonify(data['skill']), 200

    if request.method == 'PUT':
        if index:
            # if user is trying to access a specific skill with id=index
            skill_id = int(index)
            if 0 < skill_id <= len(data['skill']):
                body = request.json
                required_fields = ['name', 'proficiency', 'logo']

                name = body['name']
                proficiency = body['proficiency']
                logo = body['logo']

                    # update the skill in the database.
                    # for now, we fetch the current user based on ID - position in the array = (id - 1)

                a_skill = data['skill'][skill_id - 1] # get user to update

                # update their info
                a_skill.name = name
                a_skill.proficiency = proficiency
                a_skill.logo = logo


                data['skill'][skill_id - 1] = a_skill # add to list
                index = data['skill'].index(a_skill)

                return jsonify({
                    'id': index,
                    'message': 'Skill updated successfully',
                    'body': a_skill,
                }), 201

        return jsonify({'message': f'Skill with ID {skill_id} does not exist'}), 400

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
        index = len(data['skill']) - 1

        return jsonify({
        'id': (index + 1),
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

@app.route('/user', methods=['GET', 'POST'])
@app.route('/user/<user_id>', methods=['PUT'])
def user(user_id=None):
    '''
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
    '''
    if request.method == 'GET':
        return jsonify(data["user"]), 200

    if request.method == 'PUT':
        if user_id:
            # if user is trying to access a specific skill with id=index
            uid = int(user_id)
            if 0 < uid <= len(data['user']):
                body = request.json
                required_fields = ['name', 'phone', 'email', 'resume_order']

                name = str(body['name'])
                phone = str(body['phone'])
                email = str(body['email'])
                resume_order = str(body['resume_order'])

                if not validate_phone(phone):
                    return jsonify({"error": "Invalid phone number. Please provide a valid international phone number."}), 400

                    # update the user in the database.
                    # for now, we fetch the current user based on ID - position in the array = (id - 1)

                a_user = data['user'][uid - 1] # get user to update

                # update their info
                a_user.name = name
                a_user.phone = phone
                a_user.email = email
                a_user.resume_order = resume_order


                data['user'][uid - 1] = a_user # add to list
                index = data['user'].index(a_user)

                return jsonify({
                    'id': index,
                    'message': 'User updated successfully',
                    'body': a_user,
                }), 201

        return jsonify({'message': f'User with ID {uid} does not exist'}), 400


    if request.method == 'POST':
        body = request.json
        required_fields = ['name', 'phone', 'email', 'resume_order']

        # ensure that the body has all required params
        if not validate_request(body, required_fields):
            return jsonify({"error": "Invalid request payload. Required fields are missing."}), 400

        name = str(body['name'])
        phone = str(body['phone'])
        email = str(body['email'])
        resume_order = str(body['resume_order'])

        if not validate_phone(phone):
            return jsonify({"error": "Invalid phone number. Please provide a valid international phone number."}), 400

        # Create the user in the database.
        # for now, we add it to a list
        a_user = User(name=name, phone=phone, email=email, resume_order=resume_order )
        data['user'].append(a_user) # add to list
        index = len(data['user']) - 1

        return jsonify({
            'message': 'User created successfully',
            'body': a_user,
            'id': (index + 1)
        }), 201

def validate_phone(phone):
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
