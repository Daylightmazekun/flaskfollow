from flask_mongoengine import MongoEngine
from flask import Flask

app = Flask(__name__)
app.config['MONGODB_SETTING'] = {
    'db' : 'just_the_way_you_are',
    'host' : 'localhost',
    'port' : 27017
}
mdb = MongoEngine()
mdb.init_app(app)

