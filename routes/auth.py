
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

auth_blueprint = Blueprint('auth', __name__)

# Simple user storage (use a database in production)
users = {}

# Helper function to create a hashed password
def hash_password(password):
    return generate_password_hash(password)

# Helper function to verify hashed password
def verify_password(stored_password, provided_password):
    return check_password_hash(stored_password, provided_password)

@auth_blueprint.route('/login', methods=['POST'])
def login():
    # Retrieve username and password from the request
    username = request.json.get('username')
    password = request.json.get('password')

    print(f"Received login attempt with username: {username} and password: {password}")  # Debug log

    # Validate the user credentials
    if username in users and verify_password(users[username]["password"], password):
        # Create JWT token upon successful login (expires in 1 hour)
        access_token = create_access_token(identity=username, fresh=True, expires_delta=False)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message="Invalid credentials"), 401

@auth_blueprint.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    # Simplified registration logic (add password hashing and database logic for production)
    if username not in users:
        users[username] = {"password": hash_password(password)}
        return jsonify(message="User registered successfully"), 201
    else:
        return jsonify(message="User already exists"), 400

# Protect a route with JWT (for demo purposes, added '/dashboard')
@auth_blueprint.route('/dashboard', methods=['GET'])
@jwt_required()  # Protect the dashboard route with JWT authentication
def dashboard():
    # Get the current user from the JWT token
    current_user = get_jwt_identity()
    return jsonify(message=f"Welcome to the Dashboard, {current_user}!")
