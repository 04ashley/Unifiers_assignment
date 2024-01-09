# accounts/urls.py
from django.urls import path
from .views import (
    register, login, dashboard, profile,
    password_change, password_reset, email_confirmation, logout
)

urlpatterns = [
    path('register.html/', register, name='register'),
    path('login.html/', login, name='login'),
    path('dashboard.html/', dashboard, name='dashboard'),
    path('profile.html/', profile, name='profile'),
    path('password_change.html/', password_change, name='password_change'),
    path('password_reset.html/', password_reset, name='password_reset'),
    path('email_confirmation.html/', email_confirmation, name='email_confirmation'),
    path('logout.html/', logout, name='logout'),
]