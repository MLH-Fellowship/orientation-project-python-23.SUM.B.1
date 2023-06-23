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
