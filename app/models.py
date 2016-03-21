from . import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), unique=False)
    lastname = db.Column(db.String(80), unique=False)
    age= db.Column(db.String(80), unique=False)
    sex = db.Column(db.String(1), unique=False)

    def __init__(self, firstname, lastname, age, sex):
           self.firstname = firstname
           self.lastname = lastname
           self.age = age
           self.sex = sex
    
    def __repr__(self):
        return '<User %r>' % self.username