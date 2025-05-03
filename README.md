# 🛠 Employer Management System API

A simple REST API for managing employers, built with Django REST Framework. Includes custom user authentication using email and JWT tokens (Simple JWT), and secure CRUD operations for employer data.

---

## 📦 Features

- Custom `User` model with email login
- JWT Authentication with access/refresh tokens
- Employer CRUD operations (Create, Read, Update, Delete)
- Secure: Users can only access their own employer data

---

## 🚀 Installation Guide

### 1. Clone the Repository and creating Virtual ENV

```bash
git clone https://github.com/Jilan5/softvence.git
cd softvence
python -m venv env
env/scripts/activate  
```
### 2. set up the django project 
```bash
pip install -r requirements.txt

```
### 3. Run the Backend server
```bash
python manage.py runserver
```
### 4. Api endpoints
###🔐 Authentication
| Method | Endpoint              | Description                      |
| ------ | --------------------- | -------------------------------- |
| POST   | `/api/auth/signup/`   | Register a new user              |
| POST   | `/api/auth/login/`    | Obtain JWT access & refresh      |
| POST   | `/api/auth/logout/`   | Logout & blacklist refresh token |
| GET    | `/api/auth/profile/`  | Get current user profile         |
| POST   | `/api/token/refresh/` | Get new access token (optional)  |
###🔐  Employer CRUD (Authenticated Only)
| Method | Endpoint               | Description                       |
| ------ | ---------------------- | --------------------------------- |
| POST   | `/api/employers/`      | Create a new employer             |
| GET    | `/api/employers/`      | List all employers (for the user) |
| GET    | `/api/employers/<id>/` | Retrieve a specific employer      |
| PUT    | `/api/employers/<id>/` | Update a specific employer        |
| DELETE | `/api/employers/<id>/` | Delete a specific employer        |

