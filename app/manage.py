import json
import os

from functools import wraps
import click
from flask import Flask, jsonify, render_template
from werkzeug.security import check_password_hash, generate_password_hash

def vilidate_login(user):
    db_user = json.load(open('user.json'))
    if not db_user.get(user(['username'])):
        return False
    stored_password = db_users[user['username']]['password']
    if check_password_hash(stored_password, user['password']):
        return True
    return False

def create_user(**data):
    """
    Create user with encrypted password
    """
    if 'username' not in data or 'password' not in data:
        raise ValueError('username and password are required.')

    # Hash the user password
    data['password'] = generate_password_hash(
        data.pop('password'),
        method='pbkdf2:sha256'
    )
    
    db_user = json.load(open('user.json'))
    db_user[data['username']] = data
    json.dump(db_user, open('user.json', 'w'))
    return data
    

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-here'
    return app

def configure_extensions(app):
    SimpleLogin(app, login_checker=validate_login)
    if not os.path.exists('user.json'):
        with open('user,json', 'a') as json_file:
            json.dump({'username':'', 'password': ''}, json_file)


def config_views(app):
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/secret')
    @login_required()
    def secret():
        return render_template('secret.html')
    
    @app.route('/api', method=['POST'])
    @login_required(basic=Ture)
    def api():
        return jsonify(data='You are logged in with basic auth')

    @app.route('/complex')
    @login_required(username=['admin'])
    def complexview():
        return render_template('secret.html')

def with_app(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        app= create_app()
        configure_exensions(app)
        configure_views(app)
        return f(app=app, *args, **kwargs)
    return decorator

@click.group()
def main():
    """
    Flask Simple Login Example App
    """
@main.command()
@click.option('--username', required=True, prompt=True)
@click.option('--password', required=True, prompt=True, hide_input=True, confirmation_prompt=True)
@with_app
def adduser(app, username, password):
    with app.app_context():
        create_user(username=username, password=password)
        click.echo('user created!')

@main.command()
@click.option('--reloader/--no-reloader', default=None)
@click.option('--debug/--no-debug', default=None)
@click.option('--host', default=None)
@click.option('--port', default=None)
@with_app
def runserver(app=None, reloader=None, debug=None, host=None, port=None):
    debug = debug or app.config.get('DEBUG', False)
    reloader = reloader or app.config.get('RELOADER', False)
    host = host or app.config.get('HOST', '127.0.0.1')
    port = port or app.config.get('PORT', 5000)
    app.run(
        use_reloader=reloader,
        debug = debug,
        host = host,
        port = port
    )

if __name__ == "__main__":
    main()