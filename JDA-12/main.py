from flask import Flask, abort, render_template, redirect, url_for, request, make_response
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user
from urllib.parse import urlparse, urljoin
from secret import SECRET_KEY, USERS_LIST, PASSWORD_LOGIN

app = Flask(__name__)
app.secret_key = SECRET_KEY
login_manager = LoginManager(app)
users = USERS_LIST
password_login = PASSWORD_LOGIN


class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
        self.name = users[int(user_id)]

    def get(self, name):
        return users.index(name)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] not in users or request.form['password'] != password_login:
            error = 'Invalid Credentials. Please try again.'
        else:
            user = User(users.index(request.form['username']))
            login_user(user)
            next = request.args.get('next')
            if not is_safe_url(next):
                return abort(400)
            resp = make_response(redirect('/homepage'))
            resp.set_cookie('username', request.form['username'])
            return resp
    return render_template('login.html', error=error)


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route("/")
def hello():
    return redirect(url_for('login'))


@app.route("/homepage")
@login_required
def homepage():
    return render_template("select-dashboard.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


@app.route('/logout')
def sign_out():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
