from flask_wtf.file import FileField, FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, DecimalField
from wtforms.validators import DataRequired, Optional


class AppointmentForm(FlaskForm):
    client_name = StringField('Client Name', validators=[DataRequired()])
    appointment_time = StringField('Appointment Time', validators=[DataRequired()])  # Changed to StringField
    description = TextAreaField('Description', validators=[Optional()])  # Make this optional
    image = FileField('Image', validators=[FileAllowed(['jpg', 'png'], 'Images only!')])  # Optional

    payment_method = SelectField('Payment Method', choices=[
        ('paypal', 'PayPal'),
        ('cash_app', 'Cash App'),
        ('venmo', 'Venmo'),
    ], validators=[DataRequired()])

    payment_amount = DecimalField('Payment Amount', places=2, validators=[DataRequired()])

    submit = SubmitField('Schedule Appointment')

