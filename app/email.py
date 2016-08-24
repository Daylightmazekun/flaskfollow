# -*- coding: utf-8 -*-
from threading import Thread

from flask import current_app, render_template
from flask_mail import Message

from . import mail


def send_async_email(app, msg):
    '''send async email'''
    with app.app_context():
        mail.seng(msg)
        
def send_email(to, subject, template, **kwargs):
    '''send email'''
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + '' + subject)
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target = send_async_email, args = [app, msg])
    thr.start()
    return thr
    