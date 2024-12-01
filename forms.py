# from flask_wtf.file import FileField, FileAllowed
# from flask_wtf import FlaskForm
# from wtforms import StringField, TextAreaField, SubmitField, SelectField, DecimalField, DateTimeField
# from wtforms.validators import DataRequired, Optional
# from wtforms import ValidationError
# from datetime import datetime

# class AppointmentForm(FlaskForm):
#     description = TextAreaField('Description', validators=[Optional()])  # Optional field for additional notes
    
#     # Image upload with additional file types allowed
#     image = FileField('Image (optional)', validators=[
#         FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'pdf', 'doc', 'docx'], 'Images and documents only!')
#     ])  # Allow images and documents

#     payment_method = SelectField('Payment Method', choices=[
#         ('', 'Select a payment method'),  # Default option
#         ('paypal', 'PayPal'),
#         ('cash_app', 'Cash App'),
#         ('venmo', 'Venmo'),
#     ], validators=[DataRequired()])

#     submit = SubmitField('Schedule Appointment')

#     # Custom validator to ensure appointment time is in the future
#     def validate_appointment_time(form, field):
#         if field.data <= datetime.now():
#             raise ValidationError('Appointment time must be in the future.')

