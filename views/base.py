# -*- coding: utf-8 -*-
import markdown2
from flask import g

from tempy import Escaped
import tempy.widgets as widg
import tempy.tags as tags

from app import app, url_for


class NavBar(tags.Nav):
    def init(self):
        self.title = tags.Div(klass='navbar-header')(
            menu_btn=tags.Button(**{
                'type': "button",
                'class': "navbar-toggle collapsed",
                'data-toggle': "collapse",
                'data-target': "#navbar",
                'aria-expanded': "false",
                'aria-controls': "navbar"
            })(
                tags.Span(klass='sr-only')('Toggle Navigation'),
                tags.Span(klass='icon-bar'), tags.Span(klass='icon-bar'), tags.Span(klass='icon-bar')),
            brand=tags.A(klass='navbar-brand', href='/')(app.config.get('SITE_TITLE'))
        )
        self.menu = tags.Div(klass='navbar-collapse collapse', id='navbar')
        self(tags.Div(klass='container')(self.title, self.menu))

    def _make_menu(self):
        menu_items = [
            tags.Li()(tags.A()('Games')),
            tags.Li()(tags.A(href='/rules')('Rules')),
        ]
        self.menu(tags.Ul(klass='nav navbar-nav')(menu_items))
        login_link = [[('/login', 'Login'), ('/signup', 'Sign up')], [('/logout', 'Logout'), ]][g.user.is_authenticated]
        user_tags = []
        if g.user.is_authenticated:
            user_tags = [
                tags.Li(klass='active')(tags.A(href='/edit_user')('Profile')),
                tags.Li()(tags.A()(g.user.username, ' ', tags.Span(klass=f'flag-icon flag-icon-{g.user.country}'))),
            ]
        self.menu(
            tags.Ul(klass='nav navbar-nav navbar-right')(
                user_tags,
                (tags.Li()(tags.A(href=link[0])(link[1])) for link in login_link)
            )
        )
        return self


class BasePage(widg.TempyPage):
    def js(self):
        s3_bucket = app.config.get('FLASKS3_BUCKET_NAME')
        return [
            tags.Script(src="https://code.jquery.com/jquery-3.2.1.min.js",
                        integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=",
                        crossorigin="anonymous"),
            tags.Script(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js",
                        integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh",
                        crossorigin="anonymous"),
            tags.Script(src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js",
                        integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ",
                        crossorigin="anonymous"),
            tags.Script(defer=True, src="https://use.fontawesome.com/releases/v5.0.0/js/all.js"),
            tags.Script(src=url_for('static', filename='js/main.js')),
            tags.Script()(Escaped(f'var FLASKS3_BUCKET_NAME = "{s3_bucket}"'))
        ]

    @property
    def page_title(self):
        return app.config.get('SITE_TITLE')

    def css(self):
        return [
            tags.Link(rel="stylesheet", href="http://getbootstrap.com/docs/3.3/dist/css/bootstrap.min.css"),
            tags.Link(rel="stylesheet", href=url_for('static', filename='css/flag-icon-css/css/flag-icon.min.css')),
            tags.Link(href=url_for('static', filename='css/style.css'),
                      rel="stylesheet",
                      typ="text/css"),
        ]

    def init(self):
        self.head(self.css(), self.js())
        self.head(tags.Meta(name="viewport", content="width=device-width, initial-scale=1"))
        self.head.title(self.page_title)
        self.navbar = NavBar(klass='navbar navbar-default navbar-fixed-top')._make_menu()
        self.content = tags.Div(klass='container main-window')
        self.footer = tags.Footer(klass='footer')(
            tags.Div(klass='container')(
                tags.P(klass='text-muted')(
                    "created by Federico Cerchiari with ",
                    tags.Img(src=url_for('static', filename='img/brain.png'), height="17px"),
                    ", Python and TemPy. "
                ),
            )
        )
        self.body(
            self.navbar,
            self.content,
            self.footer
        )


class HomePage(BasePage):
    pass


class ContentPage(BasePage):
    def init(self):
        self.content(
            tags.Div(klass='page-header')(
                tags.H1()(self._data['content'].title)
            ),
            tags.Div(klass='site-content lead')(
                Escaped(markdown2.markdown(self._data['content'].text))
            )
        )
