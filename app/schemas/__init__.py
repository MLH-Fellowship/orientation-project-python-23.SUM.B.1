from dataclasses import dataclass


@dataclass
class Experience:
    """
    Summary
    -------
    dataclass for experiences schema

    Attributes
    ----------
    title (str): title
    company (str): company
    start_date (str): start date
    end_date (str): end date
    description (str): description
    logo (str): logo
    """

    title: str
    company: str
    start_date: str
    end_date: str
    description: str
    logo: str


@dataclass
class Education:
    """
    Summary
    -------
    dataclass for educations schema

    Attributes
    ----------
    course (str): course name
    school (str): school name
    start_date (str): start date
    end_date (str): end date
    grade (str): grade
    logo (str): logo
    """

    course: str
    school: str
    start_date: str
    end_date: str
    grade: str
    logo: str


@dataclass
class Skill:
    """
    Summary
    -------
    dataclass for skills schema

    Attributes
    ----------
    name (str): skill name
    proficiency (str): skill proficiency
    logo (str): logo
    """

    name: str
    proficiency: str
    logo: str


@dataclass
class User:
    """
    Summary
    -------
    dataclass for user schema

    Attributes
    ----------
    name (str): user name
    phone (str): user phone
    email (str): user email
    resume_order (list): user resume order

    where 1-> Experience, 2 -> Education,  3 -> Skills

    Example:
    ```
    # this means that we have a user with name Jon Doe, with other properties. The `resume_order` is used to specify that
    # this user wants their resume to be represented in a particular order: (Experience, Education, and Skill)
    user = User(name='Jon Doe', phone'+2348050590740', email'jon.doe@example.com', resume_order = '[1, 2, 3]')
    ```
    """

    name: str
    phone: str
    email: str
    resume_order: str
