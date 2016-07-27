from django.conf.urls import url
from django.contrib.auth import views as auth_views

# Provide custom templates for django auth views.
urlpatterns = [
    url(r'^login/$',
        auth_views.login,
        {'template_name': 'user/login.html'},
        name='login'),

    url(r'^logout/$',
        auth_views.logout,
        {'template_name': 'user/logout.html'},
        name='logout'),

    url(r'^password/change/$',
        auth_views.password_change,
        {'template_name': 'user/password_change.html',
         'post_change_redirect': 'user:auth_password_change_done'},
        name='auth_password_change'),

    url(r'^password/change/done/$',
        auth_views.password_change_done,
        {'template_name': 'user/password_change_done.html'},
        name='auth_password_change_done'),

    url(r'^password/reset/$',
        auth_views.password_reset,
        {'template_name': 'user/password_reset.html',
         'post_reset_redirect': 'user:auth_password_reset_done',
         'email_template_name': 'user/password_reset_email.txt'},
        name='auth_password_reset'),

    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/'
        r'(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'user/password_reset_confirm.html',
         'post_reset_redirect': 'user:auth_password_reset_complete'},
        name='auth_password_reset_confirm'),

    url(r'^password/reset/complete/$',
        auth_views.password_reset_complete,
        {'template_name': 'user/password_reset_complete.html'},
        name='auth_password_reset_complete'),

    url(r'^password/reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'user/password_reset_done.html'},
        name='auth_password_reset_done'),
]
