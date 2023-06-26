import sqlite3

connection = sqlite3.connect("resume.db")
cursor = connection.cursor()

#creating tables
experience_table = """CREATE TABLE IF NOT EXISTS 
                experience (title_name TEXT, company TEXT, stare_date TEXT, end_date TEXT, description TEXT, logo TEXT)"""
cursor.execute(experience_table)

education_table = """CREATE TABLE IF NOT EXISTS
                education (course TEXT, school TEXT, start_date TEXT, end_date TEXT, grade TEXT, logo TEXT)"""
cursor.execute(education_table)

skill_table = """CREATE TABLE IF NOT EXISTS
                skill (name TEXT, proficiency TEXT, logo TEXT)"""
cursor.execute(skill_table)


#adding data do tables
cursor.execute("""INSERT INTO experience VALUES ("Software Developer",
            "A Cool Company",
            "October 2022",
            "Present",
            "Writing Python Code",
            "example-logo.png")"""
        )

cursor.execute("""INSERT INTO education VALUES ("Computer Science",
                  "University of Tech",
                  "September 2019",
                  "July 2022",
                  "A+",
                  "example-logo.png")"""
            )

cursor.execute("""INSERT INTO skill VALUES ("Python",
              "1-2 Years",
              "example-logo.png")"""
            )    


connection.commit()
connection.close()