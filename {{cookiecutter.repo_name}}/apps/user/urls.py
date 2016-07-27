# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^profile/(?P<username>[\w.@+-]+)/$',
        views.UserDetailView.as_view(), name='profile'),
    url(r'^~redirect/$',
        views.UserRedirectView.as_view(), name='redirect'),
    url(r'^', include('apps.user.urls_auth')),
    url(r'^registration/', include('apps.user.urls_registration')),
]
