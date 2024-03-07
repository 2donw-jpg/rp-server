from django.urls import path
from .views import home, profile, notification,  login, register, password_reset

urlpatterns = [
    path('', login, name='login'),
    path('accounts/login/', login, name='login'),
    path('home/', home, name='home'),
    path('home/profile/', profile, name='profile'),
    path('home/notification/', notification, name='notification'),
    path('accounts/register/', register, name='register'),
    path('accounts/password-reset/', password_reset, name='password_reset'),
]