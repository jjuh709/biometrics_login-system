# biometrics_login-systemThis login system uses secure one time blockchain token for online transaction that involve funding.

# Biometric Login System README 🛡️🔐

## Overview 📜
This project is a **Flask-based authentication system** that supports **biometric login, SMS authentication, and a web interface**. It is designed for secure and user-friendly access management.

## Features 🚀
- **Biometric Authentication** (Fingerprint/Face recognition)
- **SMS-based Two-Factor Authentication (2FA)**
- **User Management (Signup/Login/Logout)**
- **REST API for Authentication**
- **Secure Password Storage**

## Tech Stack 🛠️
- **Backend:** Flask (Python)
- **Database:** MySQL
- **Biometric API:** OpenCV / External Biometric SDK
- **SMS API:** Twilio / Firebase
- **Frontend:** HTML, CSS, JavaScript

## Installation & Setup ⚙️
### 1. Clone the Repository 🛠️
```bash
 git clone https://github.com/your-repo/biometric-login-system.git
 cd biometric-login-system
```

### 2. Install Dependencies 📦
```bash
pip install -r requirements.txt
```

### 3. Set Up Database 🗄️
```sql
CREATE DATABASE biometric_login;
```

Configure **config.py** with your database credentials.

### 4. Run the Application ▶️
```bash
python app.py
```

The app should now be running at: **http://localhost:5000/**

## API Endpoints 🌐
- `POST /register` → Register a new user
- `POST /login` → Login with username & password
- `POST /biometric-login` → Authenticate using biometrics
- `POST /send-sms` → Send an OTP via SMS

## Future Enhancements 🌟
- OAuth Integration
- FaceID Support
- Mobile App Support

### Contributors ✨
- **Joseph Njuguna** 👨‍💻

Feel free to contribute and enhance this system! 💡🚀


