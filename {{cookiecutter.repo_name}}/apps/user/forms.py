from registration.forms import RegistrationForm

from .models import User


class UserRegistrationForm(RegistrationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
