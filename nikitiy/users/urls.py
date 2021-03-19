from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path('registration', views.registration, name='reg'),
    path('login', auth.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('exit', auth.LogoutView.as_view(template_name='users/exit.html'), name='exit'),
    path('profile', views.profile, name='profile'),
]
