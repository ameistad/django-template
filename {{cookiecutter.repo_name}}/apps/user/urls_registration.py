# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    # Urls for django-registration
    url(r'^activate/complete/$',
        TemplateView.as_view(
            template_name='user/registration_activation_complete.html'
        ),
        name='registration_activation_complete'),

    # The activation key can make use of any character from the
    # URL-safe base64 alphabet, plus the colon as a separator.
    url(r'^activate/(?P<activation_key>[-:\w]+)/$',
        views.UserActivationView.as_view(),
        name='registration_activate'),

    url(r'^register/$',
        views.UserRegistrationView.as_view(),
        name='registration_register'),

    url(r'^register/complete/$',
        TemplateView.as_view(
            template_name='user/registration_complete.html'
        ),
        name='registration_complete'),

    url(r'^register/closed/$',
        TemplateView.as_view(
            template_name='user/registration_closed.html'
        ),
        name='registration_disallowed'),
]
