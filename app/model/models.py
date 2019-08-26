import sys
sys.path.append("..")
from mongoconfig import db 
class Words(db.Document):
    word_id = db.IntField(required = True)
    word = db.StringField()
    honnyaku = db.StringField()
    word_note = db.StringField()

class User(db.Document):
    user_id = db.IntField(required = True)
    user_name = db.StringField(required = True, max_length=20)
    user_password = db.StringField(required = True, max_length=50)
    user_role = db.StringField(required = True, max_length=50)