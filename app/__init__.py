from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()
import os
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    # from .models import Base
    from app.routes import auth

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")
    db.init_app(app)
    app.register_blueprint(auth.auth_bp,url_prefix='/auth')
    return app 

create_app()