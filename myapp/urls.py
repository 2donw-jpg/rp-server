from django.urls import path
from .views import home, login_view

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home, name='home'),
]