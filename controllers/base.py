# -*- coding: utf-8 -*-
from app import app

import views.base as base
import models.site as site


@app.route('/')
def index():
    return base.HomePage().render()


@app.route('/rules')
def rules():
    rules = site.Content.query.filter_by(title='Rules').first()
    return base.ContentPage(data={'content': rules}).render()
