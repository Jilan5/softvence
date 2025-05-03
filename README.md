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
env/bin/activate  
```
### 2. set up the django project and database migrations
```bash
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
```
### 3. Run the Backend server
```bash
python manage.py runserver
```
### 4. Api endpoints


