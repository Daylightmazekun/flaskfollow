from flask_mongoengine import MongoEngine, MongoEngineSessionInterface 
from flask import Flask

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {'HOST':'127.0.0.1','port':27017,'DB': 'local'}
db = MongoEngine(app)
app.session_interface = MongoEngineSessionInterface(db)
