from django.urls import path

from . import views

urlpatterns = [
    path("", views.SignUpView, name="signup"),
    path("login/", views.LoginView, name="login"),
    path("welcome/", views.welcome, name="welcome"),
]



