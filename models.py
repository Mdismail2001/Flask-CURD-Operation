from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Add_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  
    description = db.Column(db.String(100), nullable=False)
    salary = db.Column(db.Integer)    
    


class Signup_Info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
