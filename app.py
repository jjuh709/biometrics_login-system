from flask import Flask, render_template, jsonify, redirect, url_for
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from flask_cors import CORS
from routes.auth import auth_blueprint

app = Flask(__name__)

# Enable CORS
CORS(app)

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Change to a more secure key in production
jwt = JWTManager(app)

# Register the Blueprint for /auth routes
app.register_blueprint(auth_blueprint, url_prefix="/auth")

# Render the login page
@app.route('/')
def index():
    return render_template('index.html')  # Make sure index.html is in the 'templates' folder

# Protected Dashboard Route
@app.route('/dashboard')
@jwt_required()  # Protect the dashboard route with JWT authentication
def dashboard():
    # Get the current user from the JWT token
    current_user = get_jwt_identity()  # This retrieves the 'identity' (username) from the JWT token
    return jsonify(message=f"Welcome to the Dashboard, {current_user}!")  # Respond with a welcome message

# Error handling for unauthenticated users
@app.errorhandler(401)
def unauthorized(error):
    return redirect(url_for('index'))  # Redirect to the login page if the user is not authenticated

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
