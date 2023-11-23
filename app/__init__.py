from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
import os
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # from .models import Base

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    return app 

create_app()