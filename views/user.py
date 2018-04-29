# -*- coding: utf-8 -*-
import tempy.tags as tags

import views.base as base


class LoginPage(base.BasePage):

    def init(self):
        self.form = tags.Form(action="/login",
                              method='post',
                              klass='form-signin')(
            title=tags.H2(klass='form-signin-heading')('Login'),
            username=tags.Input('required', 'autofocus',
                                typ="text",
                                name="username",
                                klass='form-control',
                                placeholder='Username'),
            l_user=tags.Label(_for='username',
                              klass='sr-only')('Username'),
            password=tags.Input('required',
                                typ="password",
                                name="password",
                                klass='form-control',
                                placeholder='Password'),
            l_pwd=tags.Label(_for='password',
                             klass='sr-only')('Password'),
            lb=tags.Button(typ="submit",
                           klass='btn btn-lg btn-primary btn-block')('Login'),
            referrer=tags.Input(typ='hidden',
                                name='referrer'),
        )
        self.content(
            form=self.form
        )

    def wrong(self, what):
        self.content.form.prepend(
            tags.Div(klass='alert alert-danger')('Wrong ', what.title())
        )
        return self

    def set_referrer(self, ref):
        self.form.referrer.attr(value=ref)
        return self

    def set_form(self, form):
        self.form.username.attr(value=form['username'])
        self.form.referrer.attr(value=form['referrer'])
        return self
