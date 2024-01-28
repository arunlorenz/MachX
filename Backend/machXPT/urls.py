from django.urls import path
from . import views

urlpatterns = [
    path('', views.ask_mach, name='main'),
    path('submit_form/', views.submit_form, name='submit_form'),  # Ensure this line is present
]
