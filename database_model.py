from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app import app

db = SQLAlchemy()
app.app_context().push()


class User(db.Model):
    """A user"""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    phone = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    resume_order = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"<User id={self.id} fname={self.name} email={self.email} resume_order={self.resume_order}>"


class Skill(db.Model):
    """A skill"""

    __tablename__ = "skills"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    proficiency = db.Column(db.String(25), unique=False, nullable=False)
    logo = db.Column(db.String(30), nullable=True)

    def __repr__(self):
        return f"<Skill id={self.id} skill name={self.name} proficiency={self.proficiency}>"


class Experience(db.Model):
    """A experience"""

    __tablename__ = "experiences"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(25), nullable=False)
    company = db.Column(db.String(50), unique=False, nullable=False)
    start_date = db.Column(db.String(30), nullable=False)
    end_date = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    logo = db.Column(db.String(30), nullable=True)

    def __repr__(self):
        return f"<Experience id={self.id} title={self.title}, company={self.company}>"


class Education(db.Model):
    """A education"""

    __tablename__ = "educations"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    course = db.Column(db.String(25), nullable=False)
    school = db.Column(db.String(50), unique=False, nullable=False)
    start_date = db.Column(db.String(30), nullable=False)
    end_date = db.Column(db.String(30), nullable=False)
    grade = db.Column(db.String(25), nullable=False)
    logo = db.Column(db.String(30), nullable=True)

    def __repr__(self):
        return f"Education id={self.id} course={self.course} school={self.school}>"


def connect_to_db(app, db_name):
    """Connect flask service to the database."""

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = app
    db.init_app(app)
    print("Connected to the db!")


if __name__ == "__main__":  # check if we run the file or import it
    connect_to_db(app, "resume")  # conncet the flask app to database
