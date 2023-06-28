"""File to handle interactions to the database"""

from database_model import db, User, Experience, Skill, Education
import os
import database_model
import app



def create_user(name, phone, email, resume_order):
    """Create and return an user"""
    user = User(name=name,
                phone=phone,
                email=email,
                resume_order=resume_order)
    return user


def create_skill(name, proficiency, logo):
    """Create and return a skill"""
    skill = Skill(name=name,
                  proficiency=proficiency,
                  logo=logo)
    return skill


def create_experience(title, company, start_date, end_date, description, logo):
    """Create an return an experience"""
    experience = Experience(title=title,
                            company=company,
                            start_date=start_date,
                            end_date=end_date,
                            description=description,
                            logo=logo)
    return experience


def create_education(course, school, start_date, end_date, grade, logo):
    """Create and return an education"""
    education = Education(course=course,
                          school=school,
                          start_date=start_date,
                          end_date=end_date,
                          grade=grade,
                          logo=logo)
    return education

def get_all_education():
    """Return all educations"""
    return Education.query.all()


def get_education_by_id(id):
    """Return an education based on id"""
    return Education.query.filter(Education.id == id).first()
