from app.schemas import Education, Experience, Skill, User

data = {
    "experience": [
        Experience(
            "Software Developer",
            "A Cool Company",
            "October 2022",
            "Present",
            "Writing Python Code",
            "example-logo.png",
        )
    ],
    "education": [
        Education(
            "Computer Science",
            "University of Tech",
            "September 2019",
            "July 2022",
            "A+",
            "example-logo.png",
        ),
        Education(
            "Computer Science",
            "Harvard",
            "October 2019",
            "June 2024",
            "70%",
            "example-logo.png",
        ),
        Education(
            "Cybersecurity",
            "University of florida",
            "August 2016",
            "January 2022",
            "90%",
            "example-logo.png",
        ),
        Education(
            "Cybersecurity",
            "University of florida",
            "August 2016",
            "January 2022",
            "C+",
            "example-logo.png",
        ),
    ],
    "skill": [Skill("Python", "1-2 Years", "example-logo.png")],
    "user": [
        User(
            name="Akin Friday",
            phone="+2348050780750",
            email="akinfriday@example.com",
            resume_order="[1,2,3]",
        )
    ],
}
