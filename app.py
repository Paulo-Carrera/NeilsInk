import os
import datetime
import paypalrestsdk
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import AppointmentForm
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
from models import db, Appointment, Availability
from dotenv import load_dotenv
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configuration settings
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PASSWORD = quote(DB_PASSWORD)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'loki-the-corso')  # Use environment variable if set
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/appointments_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)

# PayPal SDK Configuration
paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" in production
    "client_id": os.getenv('PAYPAL_CLIENT_ID'),
    "client_secret": os.getenv('PAYPAL_CLIENT_SECRET')
})

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Create database tables before the first request
with app.app_context():
    db.create_all()

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
    form = AppointmentForm()
    availability = Availability.query.all()

    if form.validate_on_submit():
        client_name = form.client_name.data 
        appointment_time = datetime.datetime.strptime(form.appointment_time.data, '%Y-%m-%dT%H:%M')
        description = form.description.data 
        payment_method = form.payment_method.data
        payment_amount = form.payment_amount.data

        # Create upload directory if it doesn't exist
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

        image_file_name = None 
        if form.image.data:
            image_file = form.image.data
            if allowed_file(image_file.filename):
                image_file_name = secure_filename(image_file.filename)
                image_file.save(os.path.join(app.config['UPLOAD_FOLDER'], image_file_name))
            else:
                flash('Invalid file type. Only images and documents are allowed.', 'error')
                return redirect(url_for('schedule_appointment'))

        # Create a new appointment record
        new_appointment = Appointment(
            client_name=client_name,
            appointment_time=appointment_time,
            description=description,
            image_file=image_file_name,  # Save the file name
            payment_method=payment_method,
            payment_amount=payment_amount
        )
        
        try:
            db.session.add(new_appointment)
            db.session.commit()
            flash('Appointment scheduled successfully!', 'success')
        except Exception as e:
            db.session.rollback()  # Rollback in case of error
            flash(f'Error scheduling appointment: {str(e)}', 'error')
            return redirect(url_for('schedule_appointment'))

        return redirect(url_for('view_schedule'))

    return render_template('schedule.html', form=form, availability=availability)

@app.route('/view-schedule')
def view_schedule():
    appointments = Appointment.query.all()
    return render_template('view_schedule.html', appointments=appointments)

@app.route('/pay', methods=['POST'])
def pay():
    payment_amount = request.form.get('payment_amount', 15.00)

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": url_for('payment_success', _external=True),
            "cancel_url": url_for('payment_cancel', _external=True)
        },
        "transactions": [{
            "amount": {
                "total": str(payment_amount),
                "currency": "USD"
            },
            "description": "Appointment Deposit"
        }]
    })

    if payment.create():
        return redirect(payment.links[1].href)
    else:
        return render_template('error.html', error=payment.error)

@app.route('/payment-success')
def payment_success():
    return "Payment successful!"

@app.route('/payment-cancel')
def payment_cancel():
    return "Payment cancelled!"

if __name__ == '__main__':
    app.run(debug=True)







