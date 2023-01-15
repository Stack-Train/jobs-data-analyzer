from flask import Flask, abort, render_template, redirect, url_for, request, make_response
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from urllib.parse import urlparse, urljoin

from flask_restx import Api
from flask_admin import Admin
from flask_login import LoginManager
from flask_meld import Component
from app.models import Job, User # not yet created, might need more models

# Not sure if this works, yet
class Search(Component):
    search=""

    @property
    def jobs(self):
        result = [ Job.query.filter(Job.title.contains(self.search)).all(),
                 Job.query.filter(Job.description.contains(self.search)).all(),
                 Job.query.filter(Job.description.contains(self.search)).all()
                 ]
        temp = []
        for job in result:
            temp.extend(job)
        return temp

jda = Flask(__name__)
api = Api(app)
#api.init_app(app)


jda.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
admin = Admin(jda, name='JDA', template_mode='bootstrap3')

from JDA-12 import models, views

if __name__ == "__main__":
    jda.run(debug=True)
    
