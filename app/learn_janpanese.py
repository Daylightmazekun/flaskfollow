from flask import Flask, jsonify, render_template 
from flask.views import MethodView
from flask_simplelogin import SimpleLogin, get_username, login_required

my_user = {
    'zekun_ma' : {'password': 'norris', 'roles': ['admin']},
    'lee' : {'password': 'duglas', 'roles':[]},
    'mary' : {'password':'12345', 'roles':[]},
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
    return render_template('index.html')

@app.route('/secret')
@login_required(username = ['zekun_ma', 'mary'])
def secret():
    return render_template('secret.html')

@app.route('/api', methods=['POST'])
@login_required(basic=True)
def api():
    return jsonify(data='You are logged in with basic auth')


def be_admin(username):
    """
    Validator : all users approved, return None
    """
    return


def have_approval(username):
    """Validator: all users approved, return None"""
    return

@app.route('/complex')
@login_required(must=[be_admin, have_approval])
def complexview():
    return render_template('secret.html')


class ProtectedView(MethodView):
    decorators = [login_required]

    def get(self):
        return "You are logged in as <b>{0}</b>".format(get_username())
        

app.add_url_rule('/protected', view_func=ProtectedView.as_view('protected'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, use_reloader=True, debug=False)