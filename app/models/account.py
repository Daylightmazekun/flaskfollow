# -*- coding: utf-8 -*-

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    default = db.Column(db.Boolean, default = False, index = True)
    permissions = db.Column(db.Interger)
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')
    

class User(UserMixin, db.Model):   