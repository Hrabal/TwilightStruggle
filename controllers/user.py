# -*- coding: utf-8 -*-
from flask import g, request, redirect
from flask_login import current_user, login_user, logout_user, login_required

from app import app, login_manager
from models.user import User
from views.user import LoginPage, SignupPage

from actions.user import save_user


@login_manager.user_loader
def load_user(userid):
    return User.query.get(userid)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        login_page = LoginPage().set_referrer(request.referrer)
        if user:
            form_password = request.form['password'].encode('utf-8')
            if user.validate_password(form_password):
                login_user(user, remember=True)
                app.logger.debug('Logged in user %s', user.username)
                return redirect(request.form['referrer'])
            else:
                login_page.set_form(request.form)
                return login_page.wrong('password').render()
        else:
            return login_page.wrong('username').render()
    return LoginPage().set_referrer(request.referrer).render()


@app.route('/logout')
def logout():
    logout_user()
    return redirect(request.referrer)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_dict = request.form.to_dict()
        user = save_user(user_dict)
        login_user(user, remember=True)
        return redirect('/')
    return SignupPage().render()


@app.route('/manage_users')
@login_required
def manage_users_handler():
    return ManageUsers().render()


@app.route('/edit_user')
@app.route('/edit_user/<user_id>')
@login_required
def user_handler(**kwargs):
    return UserEdit(data=kwargs).render()


@app.route('/api/save_user', methods=['POST', ])
@login_required
def api_save_user():
    user_dict = request.form.to_dict()
    save_user(user_dict)
    return redirect('/manage_users')


@app.route('/api/delete_user/<user_id>')
@login_required
def api_delete_user(**kwargs):
    delete_user(kwargs['user_id'])
    return redirect(request.referrer)
