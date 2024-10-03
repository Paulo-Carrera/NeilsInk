from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Appointment(db.Model):
    __tablename__ = 'appointments'  # Optional: Explicitly define table name

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    image_file = db.Column(db.String(255), nullable=True)
    payment_method = db.Column(db.String(100), nullable=False)
    payment_amount = db.Column(db.Float, nullable=False, default=15.00)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Appointment {self.id} - {self.client_name}>"

class Availability(db.Model):
    __tablename__ = 'availability'  # Optional: Explicitly define table name

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.String(100), nullable=False)
    end_time = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Availability {self.day} from {self.start_time} to {self.end_time}>"




