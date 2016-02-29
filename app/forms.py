
from flask.ext.wtf import Form
from wtforms.fields import TextField, IntegerField, SelectField
from wtforms.validators import Required

class ContactForm(Form):
    firstname = TextField('Firstname', validators=[Required()])
    lastname = TextField('Lastname', validators=[Required()])
    age = IntegerField('Age', validators=[Required()])
    sex = SelectField('Sex', choices = [('m', 'Male'), ('f', 'Female')])
