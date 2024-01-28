from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('mach-up/', create_user, name='create_user'),
]