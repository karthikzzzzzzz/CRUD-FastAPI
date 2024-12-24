# CRUD API with FastAPI

This repository demonstrates a CRUD (Create, Read, Update, Delete) API implementation using **FastAPI**, with additional features like user authentication and token-based authorization.

---

## Features

### **User Authentication**
- Password hashing with `bcrypt`.
- JWT token generation for secure authentication.
- OAuth2-based token authentication.

### **User Management**
- Create new users.
- Retrieve user details.

### **Blog Management**
- Create, read, update, and delete blogs.
- Associate blogs with specific users.

### **Database**
- SQLAlchemy models for users and blogs.
- Database connection setup using SQLite (for local development).

---

## Technologies Used

- **FastAPI**: A modern Python web framework for building APIs.
- **SQLAlchemy**: ORM for seamless database interaction.
- **SQLite**: Lightweight database for local development.
- **Pydantic**: Data validation and settings management.
- **bcrypt**: For securely hashing user passwords.
- **jose**: For handling JWT tokens.

---

## Installation and Setup

### **Prerequisites**
Ensure you have the following installed:
- Python 3.8 or later
- Git (optional, for cloning the repository)

---

### **Steps**

1. **Clone the repository**:
   ```bash
   git clone https://github.com/karthikzzzzzzz/CRUD-FastAPI.git
   cd CRUD-FastAPI

2.**Create a virtual environment and activate it**:
On Linux/Mac:
python -m venv env
source env/bin/activate
On Windows:
python -m venv env
env\Scripts\activate

3.**Install dependencies**:
pip install -r requirements.txt
Run the application:
uvicorn main:app --reload
Access the API documentation:
Swagger UI: http://127.0.0.1:8000/docs
ReDoc: http://127.0.0.1:8000/redoc
API Endpoints

**User Endpoints**
POST /users/: Create a new user.
GET /users/{id}: Retrieve user details by ID.


**Blog Endpoints**
POST /blogs/: Create a new blog.
GET /blogs/: Retrieve all blogs.
GET /blogs/{id}: Retrieve a specific blog by ID.
PUT /blogs/{id}: Update a blog by ID.
DELETE /blogs/{id}: Delete a blog by ID.

   
