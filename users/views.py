from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

"""
Handles user logging in to our page
"""
def loginUser(request):
    # check for post request
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
    
        if user is None:
            return render(request, "users/login.html", {"message": "Invalid login credentials"})
    
        login(request, user)
        return (HttpResponseRedirect(reverse("menu")))

    return (render(request, "users/login.html"))

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def register(request):
    # check for post request
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        # make sure email, username unique
        if User.objects.filter(email = email).exists():
            return (render(request, "users/register.html", {"message": "Email already exists"}))
        
        if User.objects.filter(username = username).exists():
            return (render(request, "users/register.html", {"message": "Username already exists"}))

        # check if password match
        if password != password2:
            return (render(request, "users/register.html", {"message": "Passwords do not match"}))

        user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password)
        user.save()
        return (render(request, "users/register.html", {"message": "Account successfully created. You may now login."}))

    return (render(request, "users/register.html"))

