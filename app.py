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
    img_folder = os.path.join(app.static_folder, 'img')
    images = [f"img/{file}" for file in os.listdir(img_folder) if file.endswith(('.jpg', '.png', '.jpeg'))]
    return render_template('home.html', images = images)

@app.route('/schedule-appointment', methods=['GET', 'POST'])
def schedule_appointment():
    return render_template('schedule.html')

@app.route('/appointment')
def appointment():
    return render_template('calendly.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    # Update these filenames to match the actual files you have
    piercings_images = [
        'Screenshot 2024-11-02 000324.png',
        'Screenshot 2024-11-02 000414.png',
        'Screenshot 2024-11-02 161627.png'
    ]
    tattoos_images = [
        'Screenshot 2024-11-02 001347.png',
        'Screenshot 2024-11-02 001701.png',
        'Screenshot 2024-11-02 002021.png'
    ]

    return render_template('gallery.html', piercings_images=piercings_images, tattoos_images=tattoos_images)


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about-us')
def about_us():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)







