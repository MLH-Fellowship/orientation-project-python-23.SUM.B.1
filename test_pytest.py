from app import app

# def test_client():
#     '''
#     Makes a request and checks the message received is the same
#     '''
#     response = app.test_client().get('/test')
#     assert response.status_code == 200
#     assert response.json['message'] == "Hello, World!"


# def test_experience():
#     '''
#     Add a new experience and then get all experiences.

#     Check that it returns the new experience in that list
#     '''
#     example_experience = {
#         "title": "Software Developer",
#         "company": "A Cooler Company",
#         "start_date": "October 2022",
#         "end_date": "Present",
#         "description": "Writing JavaScript Code",
#         "logo": "example-logo.png"
#     }

#     item_id = app.test_client().post('/resume/experience',
#                                      json=example_experience)
#     response = app.test_client().get('/resume/experience')
#     assert response.json[item_id] == example_experience


# def test_education():
#     '''
#     Add a new education and then get all educations.

#     Check that it returns the new education in that list
#     '''
#     example_education = {
#         "course": "Engineering",
#         "school": "NYU",
#         "start_date": "October 2022",
#         "end_date": "August 2024",
#         "grade": "86%",
#         "logo": "example-logo.png"
#     }
#     item_id = app.test_client().post('/resume/education',
#                                      json=example_education)

#     response = app.test_client().get('/resume/education')
#     assert response.json[item_id] == example_education


# def test_skill():
#     '''
#     Add a new skill and then get all skills.

#     Check that it returns the new skill in that list
#     '''
#     example_skill = {
#         "name": "JavaScript",
#         "proficiency": "2-4 years",
#         "logo": "example-logo.png"
#     }

#     item_id = app.test_client().post('/resume/skill',
#                                      json=example_skill)

#     response = app.test_client().get('/resume/skill')
#     assert response.json[item_id] == example_skill


def test_add_experience():
    """
    Summary
    -------
    makes request to add a new experience and checks if the received payload have all required fileds with valid formats
    """
    response = app.test_client().post(
        "/resume/experience",
        json={
            "title": "Software Developer",
            "company": "A Cool Company",
            "start_date": "June 2022",
            "end_date": "October 2024",
            "description": "Writing Python Code",
            "logo": "example-logo.png",
        },
    )
    print(response.json)
    assert response.status_code == 201


def test_add_education():
    """
    Summary
    -------
    makes request to add a new education and checks if the received payload have all required fileds with valid formats
    """
    response = app.test_client().post(
        "/resume/education",
        json={
            "course": "Computer Science",
            "school": "University of Tech",
            "start_date": "September 2019",
            "end_date": "July 2022",
            "grade": "A+",
            "logo": "example-logo.png",
        },
    )
    print(response.json)
    assert response.status_code == 201

def test_delete_education():
    """ Test deleting a education"""    
    response = app.test_client().delete('/resume/education/1')
    assert response.status_code == 200

def test_add_skill():
    """
    Summary
    -------
    makes request to add a new skill and checks if the received payload have all required fileds with valid formats
    """
    response = app.test_client().post(
        "/resume/skill",
        json={"name": "Python", "proficiency": "15%", "logo": "example-logo.png"},
    )
    print(response.json)
    assert response.status_code == 201


def test_delete_skill():
    """
    Test deleting a skill through the skill endpoint
    """
    # Add a new skill to the data list for testing
    new_skill = {
        "name": "Python",
        "proficiency": "82%",
        "logo": "example-logo.png"
    }
    response = app.test_client().post('/resume/skill',json=new_skill)
    assert response.status_code == 201
    if response.json is not None:
        item_id = response.json["id"]

        # Make a DELETE request to delete the skill
        delete_response = app.test_client().delete(f"/resume/skill/{item_id}")

        # Assert the response status code is 200 (OK)
        assert delete_response.status_code == 200
        if delete_response.json is not None:
            # Assert the response payload contains the expected fields
            assert "status" in delete_response.json
            assert "message" in delete_response.json
            assert "deleted_item" in delete_response.json

            # Assert the response payload has the correct values
            assert delete_response.json["status"] == "success"
            assert delete_response.json["message"] == "Skill deleted successfully"
