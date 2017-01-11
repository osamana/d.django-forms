# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'your-name',
        view=views.get_name,
        name='name-form'
    ),
    url(
        regex=r'thanks',
        view=views.thanks,
        name='thanks'
    ),
]
