import os
import datetime
import paypalrestsdk
from flask import Flask, render_template, request, redirect, url_for, flash
# from forms import AppointmentForm
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
    return render_template('home.html', images = images, page_header="Home")

@app.route('/schedule-appointment', methods=['GET', 'POST'])
def schedule_appointment():
    return render_template('schedule.html', page_header="Schedule an Appointment")

@app.route('/appointment')
def appointment():
    return render_template('calendly.html', page_header="Schedule an Appointment")

@app.route('/services')
def services():
    # Pass only the filenames
    piercings_images = ['pimg1.png', 'pimg2.png', 'pimg3.png', 'pimg4.png', 'pimg5.png', 'pimg6.png', 'pimg7.png', 'pimg8.png', 'pimg9.png']
    tattoos_images = ['timg1.png', 'timg2.png', 'timg3.png', 'timg4.png', 'timg5.png', 'timg6.png', 'timg7.png', 'timg8.png', 'timg9.png']

    return render_template(
        'services.html', 
        piercings_images=piercings_images, 
        tattoos_images=tattoos_images, 
        page_header="Services"
    )

@app.route('/gallery')
def gallery():
    # Pass only the filenames
    piercings_images = ['pimg1.png', 'pimg2.png', 'pimg3.png', 'pimg4.png', 'pimg5.png', 'pimg6.png', 'pimg7.png', 'pimg8.png', 'pimg9.png']
    tattoos_images = ['timg1.png', 'timg2.png', 'timg3.png', 'timg4.png', 'timg5.png', 'timg6.png', 'timg7.png', 'timg8.png', 'timg9.png']

    return render_template(
        'gallery.html', 
        piercings_images=piercings_images, 
        tattoos_images=tattoos_images, 
        page_header="Gallery"
    )


@app.route('/contact')
def contact():
    return render_template('contact.html', page_header="Contact Us")

@app.route('/about-us')
def about_us():
    return render_template('about.html', page_header="About Us")

if __name__ == '__main__':
    app.run(debug=True)