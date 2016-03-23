from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project1:info3180@localhost/contactdb'
db = SQLAlchemy(app)
from models import *

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://rdtwxsjehwsmjd:9lZQ_CSyBm6Me2bh6MrUHx0Lcd@ec2-107-21-229-87.compute-1.amazonaws.com:5432/db82305n0ob52'
#db.drop_all()
db.create_all()

db.session.commit()
from app import views, models