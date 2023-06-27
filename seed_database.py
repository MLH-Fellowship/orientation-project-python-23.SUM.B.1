"""This file Loads data from json file and seed the tables"""

import json
import os
import crud
import database_model
from app import app


database_model.connect_to_db(app, "resume")
database_model.db.drop_all()
database_model.db.create_all()   #create database structure


with open('data/user.json') as file:
    user_file= json.loads(file.read())

db_users = []
for user in user_file:
    name = user['name']
    phone = user['phone']
    email = user['email']
    resume_order = user['resume_order']

    save_user_to_db = crud.create_user(name, phone, email, resume_order)
    db_users.append(save_user_to_db)
database_model.db.session.add_all(db_users)    


with open('data/education.json') as education_file:
    educations = json.loads(education_file.read())

education_list = []
for education in educations:
       course = education['course']
       school= education['school']
       start_date = education['start_date']
       end_date = education['end_date']
       grade = education['grade']
       logo = education['logo']

       save_education_to_db = crud.create_education(course, school, start_date, end_date, grade, logo)
       education_list.append(save_education_to_db)
database_model.db.session.add_all(education_list)   


with open('data/experience.json') as experience_file:
    experiences = json.loads(experience_file.read())

experience_list = []
for experience in experiences:
    title = experience['title']
    company = experience['company']
    start_date = experience['start_date']
    end_date = experience['end_date']
    description = experience['description']
    logo = experience['logo']

    save_experience_to_db = crud.create_experience(title, company, start_date, end_date, description, logo)
    experience_list.append(save_experience_to_db)
database_model.db.session.add_all(experience_list)    


with open('data/skills.json') as skill_file:
    skills = json.loads(skill_file.read())

skill_list = []
for skill in skills:
    name = skill['name']
    proficiency = skill['proficiency']
    logo = skill['logo']

    save_skill_to_db = crud.create_skill(name, proficiency, logo)
    skill_list.append(save_skill_to_db)
database_model.db.session.add_all(skill_list)    
database_model.db.session.commit()