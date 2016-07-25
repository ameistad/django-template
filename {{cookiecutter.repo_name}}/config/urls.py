from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('apps.users.urls', namespace='users')),
    url(r'^$', TemplateView.as_view(template_name='start.html'), name='start'),
]
