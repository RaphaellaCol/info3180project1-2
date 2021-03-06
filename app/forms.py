
from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField
from wtforms.validators import Required
from flask_wtf.file import FileField, FileAllowed, FileRequired

class ContactForm(Form):
   
    firstname = TextField('Firstname', validators=[Required()])
    lastname = TextField('Lastname', validators=[Required()])
    age = TextField('Age', validators=[Required()])
    sex = SelectField('Sex', choices = [('m', 'Male'), ('f', 'Female')])
    img = FileField('img', validators=[])
    