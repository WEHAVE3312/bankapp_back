import os
from flask import Flask, Blueprint
from dotenv import load_dotenv

def create_app():

    load_dotenv()

    app = Flask(__name__)
    api = Blueprint('api', __name__)

    app.config['DEBUG'] = True
    app.config['SECRET_KEY'] = '3a7d5e82fd56a6b77ef9720a93284966'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://postgres:v%qkAIt&zDVz@bankdatabase.cg7stozx8h4b.us-east-2.rds.amazonaws.com:5432/postgres'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app, api
