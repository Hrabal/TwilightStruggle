# -*- coding: utf-8 -*-
import pycountry
from flask import g
import tempy.tags as tags
from babel.dates import format_date
from datetime import date
from dateutil.relativedelta import relativedelta

from app import url_for
import views.base as base


class UserPage(base.BasePage):
    def set_referrer(self, ref):
        self.form.referrer.attr(value=ref)
        return self


class LoginPage(UserPage):

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
        self.form.prepend(
            tags.Div(klass='alert alert-danger')('Wrong ', what.title())
        )
        return self

    def set_form(self, form):
        self.form.username.attr(value=form['username'])
        self.form.referrer.attr(value=form['referrer'])
        return self


class SignupPage(UserPage):

    def init(self):
        self.form = tags.Form(action="/signup",
                              method='post',
                              klass='omb_loginForm')(
            email=tags.Input('required',
                             typ="email",
                             name="email",
                             klass='form-control',
                             placeholder='Email'),
            l_email=tags.Label(_for='email',
                               klass='sr-only')('Email'),
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
                           klass='btn btn-lg btn-primary btn-block')('Sign Up'),
        )
        self.content(
            tags.Div(klass='omb_login')(
                tags.H3(klass='omb_authTitle')(
                    'Sign Up or ', tags.A(href='/login')('Login')
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
                tags.Div(klass='row omb_row-sm-offset-3')(
                    tags.Div(klass='col-xs-12 col-sm-6')(
                        tags.Hr(klass='omb_hrOr'),
                    )
                ),
            )
        )


class Profile(base.BasePage):
    def init(self):
        self.content(
            tags.Div(klass='row')(
                tags.Div(klass='col-xs-12 col-sm-3')(
                    tags.Img(src=url_for('static', filename=f'img/profile_pics/{g.user.pic}'),
                             klass='profile-user-pic')
                ),
                tags.Div(klass='col-xs-12 col-sm-3')(
                    tags.Div(klass='container')(
                        tags.Div(klass='row')(
                            tags.Div(klass='col-sm')(tags.H1()(g.user.username, f' - Level {g.user.level}')),
                        ),
                        tags.Div(klass='row')(
                            tags.Div(klass='col-sm')(tags.H2()(g.user.tagline)),
                        ),
                        tags.Div(klass='row')(
                            tags.Div(klass='col-sm-1')('Joined:'),
                            tags.Div(klass='col-sm')(format_date(g.user.joined, format='short', locale=g.user.country)),
                        ),
                        tags.Div(klass='row')(
                            tags.Div(klass='col-sm-1')('E-mail:'),
                            tags.Div(klass='col-sm')(g.user.email),
                        ),
                        tags.Div(klass='row')(
                            tags.Div(klass='col-sm-1')('Country:'),
                            tags.Div(klass='col-sm')(
                                tags.Span(klass=f'flag-icon flag-icon-{g.user.country}'), ' ',
                                pycountry.countries.get(alpha_2=g.user.country.upper()).official_name
                            )
                        ),
                        tags.Div(klass='row')(
                            tags.Div(klass='col-sm-1')('Birthday:'),
                            tags.Div(klass='col-sm')(format_date(g.user.birth, format='long', locale=g.user.country)),
                        ),
                        tags.Div(klass='row')(
                            tags.Div(klass='col-sm-1')('Age:'),
                            tags.Div(klass='col-sm')(relativedelta(date.today(), g.user.birth).years),
                        ),
                    )
                )
            ),
            tags.Div(klass='row')(
                tags.Div(klass='col-xs-2 col-sm-1')(
                    tags.H2()('Stats')
                )
            )
        )
