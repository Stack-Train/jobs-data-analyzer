from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False, default='')
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    desc = db.Column(db.Text)
    position = db.Column(db.String(250))
    skill_lvl = db.Column(db.String(50))
    yrs_exp = db.Column(db.Integer)
    company = db.Column(db.String(250))
    num_applied = db.Column(db.Integer)
    date_posted = db.Column(db.Date, default=date.today)

    def __repr__(self):
        return '<Job %r>' % self.title
