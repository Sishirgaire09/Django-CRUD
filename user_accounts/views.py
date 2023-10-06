from django.shortcuts import render , redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from django.http import JsonResponse
# Create your views here.

def signup_page(request):
  if request.method == "POST":
      uname = request.POST.get("username")
      email = request.POST.get("email")
      password1= request.POST.get("password")
      password2= request.POST.get("password2")
      if password1 != password2:
        raise ValidationError("PASSWORD 1 IS NOT EQUAL TO PASSWORD 2")
      print(password1)
      print(password2)
      
      user = User.objects.create_user(username=uname, email=email, password=password1)
      user.save()
      
      return render(request, "user_accounts/login.html")
    
  return render( request, "user_accounts/signup.html")

def login_page(request):
 
  
  if request.method == "POST":
      password = request.POST.get("password")
      username = request.POST.get("username")
      user = authenticate(request , username = username , password = password)
      if user is not None:
        login(request , user)
        return HttpResponseRedirect(reverse('table:table-form'))
      else:
        raise ValidationError("Authentication doesn't match")  
  return render (request , "user_accounts/login.html")

def logout_page(request):
  logout(request)
  return HttpResponseRedirect(reverse('login'))


def hello_json(request):
  return JsonResponse({
    "shishir" : "bhattarai"
  })