# -*- coding: utf-8 -*-
from flask import g, request, redirect
from flask_login import current_user, login_user, logout_user, login_required

from app import app, login_manager
import models.user as m_user
import views.user as v_user
import actions.user as a_user


@login_manager.user_loader
def load_user(userid):
    return m_user.User.query.get(userid)


@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = m_user.User.query.filter_by(username=request.form['username']).first()
        login_page = v_user.LoginPage().set_referrer(request.referrer)
        if user:
            form_password = request.form['password'].encode('utf-8')
            if user.validate_password(form_password):
                login_user(user, remember=True)
                app.logger.debug('Logged in user %s', user.username)
                return redirect('/')
            else:
                login_page.set_form(request.form)
                return login_page.wrong('password').render()
        else:
            return login_page.wrong('username').render()
    return v_user.LoginPage().set_referrer(request.referrer).render()


@app.route('/logout')
def logout():
    logout_user()
    return redirect(request.referrer)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user_dict = request.form.to_dict()
        user = a_user.sava_user.e_user(user_dict)
        login_user(user, remember=True)
        return redirect('/')
    return v_user.SignupPage().render()


@app.route('/edit_user', methods=['GET', 'POST'])
@login_required
def user_handler():
    return v_user.Profile().render()


@app.route('/api/save_user', methods=['POST', ])
@login_required
def api_save_user():
    user_dict = request.form.to_dict()
    a_user.save_user(user_dict)
    return redirect('/manage_users')


@app.route('/api/delete_user/<user_id>')
@login_required
def api_delete_user(**kwargs):
    a_user.delete_user(kwargs['user_id'])
    return redirect(request.referrer)
