from django.core.urlresolvers import reverse
from django.views.generic import DetailView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

from registration.backends.hmac.views import ActivationView, RegistrationView

from .models import User
from .forms import UserRegistrationForm


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/profile.html'
    context_object_name = 'user'
    slug_field = 'username'
    slug_url_kwarg = 'username'


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('user:profile',
                       kwargs={'username': self.request.user.username})


class UserActivationView(ActivationView):
    template_name = 'user/registration_activation.html'

    def get_success_url(self, user):
        return ('user:registration_activation_complete', (), {})


class UserRegistrationView(RegistrationView):
    email_body_template = 'user/registration_email_body.txt'
    email_subject_template = 'user/registration_email_subject.txt'
    template_name = 'user/registration_form.html'
    form_class = UserRegistrationForm

    def get_success_url(self, user):
        return ('user:registration_complete', (), {})
