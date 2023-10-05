from django.shortcuts import render

# Create your views here.

def signup_page(request):
  return render ( request, "signup.html")

def login_page(request):
  print("rendering")
  return render (request , "user_accounts/login.html")

