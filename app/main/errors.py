# -*- coding: utf-8 -*-
@main.app_errorhandler(403)
def forbidden(error):
    '''error handler for 403'''
    return render_template("errors/403.html"), 403

@main.app_errorhandler(404)
def page_not_found(error):
    '''error handler for 404'''
    return render_template('errors/403.html'), 403
@main.app_errorhandler(500)
def internal_sevser_error(error):
    '''error handler for 500'''
    return render_template("errors/500.html"), 500
