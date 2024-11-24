CRUD FastAPI

This repository demonstrates a CRUD (Create, Read, Update, Delete) API implementation using FastAPI with additional features like authentication and token-based authorization. It includes the following functionalities:

User authentication with password hashing.
JWT token generation for secure authentication.
Endpoints to manage blogs and users.
Database integration using SQLAlchemy.
Features

Authentication:
Login functionality with JWT tokens.
OAuth2-based token authentication.
User Management:
Create users.
Retrieve user details.
Blog Management:
Create, read, update, and delete blogs.
Associate blogs with users.
Database:
Models for users and blogs using SQLAlchemy.
Database connection setup.
Technologies Used

FastAPI: A modern Python web framework for building APIs.
SQLAlchemy: ORM for database interaction.
SQLite: Database used for local development.
Pydantic: Data validation and settings management.
bcrypt: For hashing user passwords.
jose: For JWT token handling.
Installation and Setup

Prerequisites
Ensure you have the following installed:

Python 3.8 or later
Git (optional, for cloning the repository)
Steps
Clone the repository:
git clone https://github.com/karthikzzzzzzz/CRUD-FastAPI.git
cd CRUD-FastAPI
Create a virtual environment and activate it:
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
Install dependencies:
pip install -r requirements.txt
Run the application:
uvicorn main:app --reload
Access the API documentation at:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
