from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired, Email
#from wtforms.validators import DataRequired, Email



class ContactForm(FlaskForm):

    name = StringField('Name', validators=[InputRequired()])
    #firstname = StringField('First Name', validators=[InputRequired()])
    #lastname = StringField('Last Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    subject = StringField('Subject', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])