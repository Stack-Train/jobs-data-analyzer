from flask import Flask
from flask_restx import Api
from flask_admin import Admin
from flask_login import LoginManager
from flask_meld import Component

jda = Flask(__name__)
jda.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

from .models import Job, User, db  # Admin removed; use User.is_admin instead

jda.config['SQLALCHEMY_DATABASE_URI'] = __import__('os').getenv('PG_LOCAL_URI', 'sqlite:///jda.db')
jda.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(jda)

api = Api(jda)
admin = Admin(jda, name='JDA', template_mode='bootstrap3')
login_manager = LoginManager(jda)


class Search(Component):
    search = ""

    @property
    def jobs(self):
        result = [
            Job.query.filter(Job.title.contains(self.search)).all(),
            Job.query.filter(Job.desc.contains(self.search)).all(),
        ]
        temp = []
        for job in result:
            temp.extend(job)
        return temp


from .views import bp as main_bp
jda.register_blueprint(main_bp)

if __name__ == "__main__":
    jda.run(debug=True)
