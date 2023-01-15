from flask import render_template, url_for
from JDA-12 import jda


# minimal api
@jda.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# Route for handling the login page logic
# Checks if user exists and password matches
# @jda.route('/login', methods=['GET', 'POST'])
# def login():
#     error = None
#     if (request.method == 'POST'):
#         if (request.form['username'] not in users or request.form['password'] != password_login):
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             user = User(users.index(request.form['username']))
#             login_user(user)
#             next = request.args.get('next')

#             if not is_safe_url(next):
#                 return abort(400)

#             resp = make_response(redirect('/homepage'))

#             resp.set_cookie('username', request.form['username'])
#             return resp
#     return render_template('login.html', error=error)


# Used to by Flask to check which is the current logged user.
# @login_manager.user_loader
# def load_user(user_id):
#     return User(user_id)


# Route to redirect - when the onload event occurs - to the login page directly
# @jda.route("/")
# def hello():
#     return redirect(url_for('login'))

# @jda.route("/homepage")
# @login_required
# def homepage(): #index with all the dashboards
#     return render_template("select-dashboard.html")

@jda.route("/dashboard")    #page of a single dashboard
# @login_required
def dashboard():
    return render_template("dashboard.html")

@jda.route("/", methods=['GET'])
def index():
    return render_template("index.html")

# @jda.route('/logout')
# def sign_out():
#     logout_user()
#     return redirect(url_for('login'))

# @jda.route('/get_token')
# def get_token():
#     resp = make_response()

#     token = requests.post("http://10.0.55.1/trusted?username=" + request.cookies.get("username"))
#     if (token.status_code != 200 or token.text == '-1'): #200 = OK in HTTP requests
#         return abort(400)

#     resp.set_cookie("auth_token", token.text)
#     return resp
