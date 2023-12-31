from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload_image, name='upload_image'),
    path('',views.loginform, name='login'),
    path('options/', views.options_page, name='options'),
    path('password/',views.change_password,name='password_change'),
]
