import db from app.app

class Words(db.Document):
    word_id = db.IntField(required = True)
    word = db.StringField()
    honnyaku = db.StringFiled()
    word_note = db.StringFiled()

class User(db.Document):
    user_id = db.IntField(required = True)
    user_name = db.StringField()
    user_password = db.StringField()
    user_role = db.StringField()