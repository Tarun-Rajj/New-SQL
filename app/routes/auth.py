from flask import Blueprint,request,jsonify
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.models import User
from app import db


auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    role = data.get('role')

    # Validate the role
    valid_roles = ['admin', 'manager', 'employee']
    if role not in valid_roles:
        return jsonify({'message': 'Invalid role. Choose a valid role: admin, manager, employee.'}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists. Choose a different username.'}), 400
    
    hashed_password = generate_password_hash(data['password'])

    new_user = User(username=username, password=hashed_password, email=email, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User signed up successfully!'})


@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        login_user(user)
        return jsonify({'message': 'Login successful!'})
    else:
        return jsonify({'message': 'Login unsuccessful. Please check your username and password.'}), 401




