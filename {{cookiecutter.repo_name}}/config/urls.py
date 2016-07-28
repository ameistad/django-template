from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('apps.user.urls', namespace='user')),
    url(r'^$', TemplateView.as_view(template_name='start.html'), name='home'),
]
