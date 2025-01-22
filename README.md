# Personal Diary App

A full-stack web application for managing personal daily news entries, built using Flask for both frontend and backend. The app provides a robust and user-friendly interface to store, organize, and retrieve personal news while ensuring data security.

# Features

Daily News Storage: Add, edit, and delete daily entries with timestamps.
User Authentication: Register and log in securely with hashed passwords.
Search and Filter: Easily search for specific entries by keywords or dates.
Responsive Design: Optimized for desktop and mobile use.
Customizable UI: Personalize your dashboard to match your preferences.
Error Handling: Robust error messages and input validation for a seamless user experience.

# Technologies Used

# Backend

Python: Core programming language.
Flask: Web framework for building the application.
Flask-SQLAlchemy: ORM for database management.
Flask-WTF: For form validation and handling.
SQLite/MySQL/PostgreSQL: Database for storing user and diary entry data (configurable).

# Frontend

HTML5 & CSS3: For designing responsive and accessible layouts.
Bootstrap: Frontend framework for styling and UI components.
JavaScript: Adds interactivity and dynamic behavior to the app.

# DevOps

Docker: Containerization for consistent development and deployment environments.
GitHub Actions: Continuous Integration/Continuous Deployment (CI/CD).
Gunicorn: WSGI server for production deployment.

# Installation

# Prerequisites

Python 3.8 or later
Flask and its dependencies
Node.js (optional, for building frontend assets)

# Clone the Repository

    git clone https://github.com/your-username/personal-diary_app.git

    cd personal-diary_app

# Create and Activate a Virtual Environment

    `python3 -m venv venv`

    `source venv/bin/activate`

# On Windows,

    use `venv\Scripts\activate`

# Install Dependencies

    pip install -r requirements.txt

# Run the Development Server

## Setup Instructions

### Secret Key

The app requires a `SECRET_KEY` for security. If you don't have one,
the application will generate it automatically and save it in a `.env` file. Follow these steps:

# flask run

    cd Personal_Diary_App

    python3 server.py

    Open the app in your browser at http://127.0.0.1:5000.

# Usage

Register for a new account or log in with your credentials.
Add entries by providing a title, content, and optional tags.
View and manage all your entries in a clean, intuitive dashboard.
Search for specific entries using keywords or dates.

# Contact

For questions or feedback, feel free to reach out:

Email: tofhatwa@gmail.com

GitHub: TSHIVHENGA-OFHATWA
