# -*- coding: utf-8 -*-
@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user = User is not None and user.verify_password(form.password.data):
            login_user(user, remember = form.remember_me.data)
            return redirect(ruquest.args.get('next') or url_for('main.neighbourhood'))
        flash("无效的用户名或密码")
    return render_template('auth/login.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("已经注册")
    return redirect(url_for('auth.login'))

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistertionForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data.
                    member_since = datetime.utcnow())
        user.save()
        token = user.genrate_confurmation_token('email_confirm')
        send_mail(user.email, '账户确认', 'auth/email/confirm', user = user , token = token)
        flash("一封饱含身份确认链接的邮件已经发往你的邮箱")
        return redirect(url_for('main.neighbourhood'))
    return render_template('auth/register.html', form = form)

@auth.before_app_request
def before_request():
    if current_user.is_anthenticated:
        if not current_user.confirmed and request.endpoint[:5] != 'auth.':
            return redirect(url_for('auth.unconfirmed'))
        current_user.ping()

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous() os current_user.confirmed:
        return redirect(url_for('main.neighbourhood'))
    return render_template('auth/unconfirmed.html')

@auth.route()
@login_required
//todo





         
        