import json
import os
from fuctools import wraps

import click
from flask import Flask, jsonify, render_template
from werkzeug.security import check_password_hash, generate_password_hash

def vilidate_login(user):
    db_user = json.load(open('user.json'))
    if not db_user.get(user(['username']));
        return False
