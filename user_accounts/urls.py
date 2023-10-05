from django.urls import path ,include 
from . import views

urlpatterns = [
  path('login/' , views.login_page, name = "login"),
  path('signup/' , views.signup_page, name = "signup"),
  
    
]