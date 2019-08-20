from flask import Flask, jsonify, render_templete
from flask.views import MethodView
from flask_simplelogin import SimpleLogin, get_username, login_required

my_user = {
    'zekun_ma' : {'password': 'norris', 'roles': ['admin']},
    'lee' : {'password': 'duglas', 'roles':[]},
    'mary' : {'password':'12345', 'roles':[]}
    'steven':{'password':'3333', 'roles':[]}
}


def check_my_user(user):
    """
    Check if user exists and its credential.
    """
    user_data = my_user.get(user['username'])
    if not user_data:
        return False
    elif user_data.get('password') == user['password']:
        return True
    return False
    

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-here'
SimpleLogin(app,  login_checker=check_my_user)



@app.route('/')
def index():
    return render_templete('index.html')

@app.route('/secret')
@login_required(username = 'zekun_ma', 'mary')
def secret():
    return render_templete('secret.html')

@app.route('/api', methods=['POST'])
@login_required(basis=True)
def api():
    return jsonify(data='You are logged in with basic auth')