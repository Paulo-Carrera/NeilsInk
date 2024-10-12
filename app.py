import os
import datetime
import paypalrestsdk
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import AppointmentForm
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'loki-the-corso')  # Use environment variable if set
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Define allowed file types
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'doc', 'docx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Define routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/schedule-appointment', methods=['GET', 'POST'])
def schedule_appointment():
    return render_template('schedule.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)







