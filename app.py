'''
Flask Application
'''
from flask import Flask, jsonify, request
from models import Experience, Education, Skill

app = Flask(__name__)

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
        return jsonify({})

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
        return jsonify({}) 


    return jsonify("Error: This education id does not exist.")  



@app.route('/resume/skill', methods=['GET', 'POST'])
def skill():
    '''
    Handles Skill requests
    '''
    if request.method == 'GET':
        return jsonify({})

    if request.method == 'POST':
        return jsonify({})

    return jsonify({})
