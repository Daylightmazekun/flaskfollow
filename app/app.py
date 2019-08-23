from flask_mongoengine import MongoEngine

app.confg['MONGODB_SETTING'] = {
    'db' : 'JUST_THE_WAY_YOU_ARE',
    'host' : 'localhost',
    'port' : 27017
}
mdb = MongoEngine()
mdb.init_app()


