import database_model
import os
import json
import crud
import database_model
# from database_model import app_temporary
# import app

os.system("dropdb resume")
os.system("createdb resume")
database_model.connect_to_db(database_model.app_temporary, "resume")
database_model.db.create_all()   #create database structure