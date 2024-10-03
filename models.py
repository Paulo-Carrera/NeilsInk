from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Appointment(db.Model):
    __tablename__ = 'appointments'  # Explicitly define table name

    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    appointment_time = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    image_file = db.Column(db.String(255), nullable=True)
    payment_method = db.Column(db.String(100), nullable=False)
    payment_amount = db.Column(db.Numeric(10, 2), nullable=False, default=15.00)  # Use Numeric for precision
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Appointment {self.id} - {self.client_name}>"

class Availability(db.Model):
    __tablename__ = 'availability'  # Explicitly define table name

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(100), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)  # Use DateTime for better handling
    end_time = db.Column(db.DateTime, nullable=False)    # Use DateTime for better handling

    # Optional: Add a unique constraint to prevent overlapping time slots on the same day
    __table_args__ = (db.UniqueConstraint('day', 'start_time', 'end_time', name='unique_availability_time'),)

    def __repr__(self):
        return f"<Availability {self.day} from {self.start_time} to {self.end_time}>"



