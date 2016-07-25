from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/user_profile.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'
