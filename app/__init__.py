# Initializes Flask application
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
# Configure other Flask extensions and database settings here


mysql = MySQL(app)  # Initialize Flask extension MySQL

# Import routes at the end to avoid circular dependencies
from . import routes
