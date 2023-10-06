from django import forms
from django.contrib.auth.forms import UserCreationForm

from customer.models import AppUser, Post

class SignUpForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ('email', 'password1', 'password2')   


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'description']


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['profile_pic']
        