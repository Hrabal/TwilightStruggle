# -*- coding: utf-8 -*-
import tempy.tags as tags

import views.base as base


class LoginPage(base.BasePage):

    def init(self):
        self.form = tags.Form(action="/login",
                              method='post',
                              klass='omb_loginForm')(
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
            tags.Div(klass='omb_login')(
                tags.H3(klass='omb_authTitle')(
                    'Login or ',
                    tags.A(href='/signup')('Sign up')
                ),
                tags.Div(klass='row omb_row-sm-offset-3 omb_socialButtons')(
                    tags.Div(klass='col-xs-4 col-sm-3')(
                        tags.A(href='#', klass='btn btn-lg btn-block omb_btn-facebook')(
                            tags.I(klass='fas fa-facebook visible-xs'),
                            tags.Span(klass='hidden-xs')('Facebook')
                        )
                    ),
                    tags.Div(klass='col-xs-4 col-sm-3')(
                        tags.A(href='#', klass='btn btn-lg btn-block omb_btn-google')(
                            tags.I(klass='fas fa-google-plus visible-xs'),
                            tags.Span(klass='hidden-xs')('Google')
                        )
                    )
                ),
                tags.Div(klass='row omb_row-sm-offset-3 omb_loginOr')(
                    tags.Div(klass='col-xs-12 col-sm-6')(
                        tags.Hr(klass='omb_hrOr'),
                        tags.Span(klass='omb_spanOr')('or')
                    )

                ),
                tags.Div(klass='row omb_row-sm-offset-3')(
                    tags.Div(klass='col-xs-12 col-sm-6')(
                        self.form
                    )
                ),
                tags.Div(klass='row omb_row-sm-offset-3 omb_loginOr')(
                    tags.Div(klass='col-xs-12 col-sm-3')(
                        tags.Label(klass='checkbox')(
                            tags.Input(typ='checkbox', value='remember-me'),
                            'Remember Me'
                        )
                    ),
                    tags.Div(klass='col-xs-12 col-sm-3')(
                        tags.P(klass='omb_forgotPwd')(
                            tags.A(href='#')('Forgot Password')
                        )
                    )
                )
            )
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
