from config.db import db
from werkzeug.security import check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(250))
    Belvo_Links = db.relationship('Bank', backref='user', lazy=True)

    def __init__(self, email,password):
        self.email = email
        self.password = password

    def check_password(self, password):
        return check_password_hash(self.password,password)
    

class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(250))
    status = db.Column(db.String(30))
    link = db.Column(db.String(250), unique=True)
    created_at = db.Column(db.String(250))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, institution, status, link, created_at,user_id):
        self.institution = institution
        self.status = status
        self.link = link
        self.created_at = created_at
        self.user_id = user_id
