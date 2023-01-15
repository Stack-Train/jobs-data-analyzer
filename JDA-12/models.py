from flask_admin.contrib.sqla import ModelView
from JDA-12 import jda

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)

	def __repr__(self):
		return '<User %r>' % self.username

class Admin(User):
	def __repr__(self):
		return '<Admin %r>' % self.username

 venn diagrams


class Job(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250))
	desc = db.Column(db.String(250))
	position = db.Column(db.String(250))
	skill_lvl = db.Column(db.String(250))
	yrs_exp = db.Column(db.Integer)
	company = db.Column(db.Float, unique=True)
	num_applied = db.Column(db.Float)
	date_posted = db.Column(db.Date)
