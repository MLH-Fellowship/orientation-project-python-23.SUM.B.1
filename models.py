# pylint: disable=R0913

'''
Models for the Resume API. Each class is related to
'''

from dataclasses import dataclass


@dataclass
class Experience:
    '''
    Experience Model

    Attributes:
        title (str): The title of the experience.

        company (str): The company name.

        start_date (str): The start date of the experience.

        end_date (str): The end date of the experience.

        description (str): The description of the experience.

        logo (str): The logo of the experience.
    '''
    title: str
    company: str
    start_date: str
    end_date: str
    description: str
    logo: str


@dataclass
class Education:
    '''
    Education Model

    Attributes:
        course (str): The course name.

        school (str): The school name.

        start_date (str): The start date of the education.

        end_date (str): The end date of the education.

        grade (str): The grade achieved in the education.

        logo (str): The logo of the education.
    '''
    course: str
    school: str
    start_date: str
    end_date: str
    grade: str
    logo: str


@dataclass
class Skill:
    '''
    Skill Model

    Attributes:
        name (str): The name of the skill.

        proficiency (str): The proficiency level of the skill.
        
        logo (str): The logo of the skill.
    '''
    name: str
    proficiency: str
    logo: str
