from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.home, name="home"),
    path('signup/', views.signup, name='signup'),
]




