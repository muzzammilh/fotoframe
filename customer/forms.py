from django.contrib.auth.forms import UserCreationForm

from customer.models import AppUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('email', 'password1', 'password2')   



