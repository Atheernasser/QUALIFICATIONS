from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request:HttpRequest):
    """ This function view create new user """
    if request.method == "POST":
        new_user = User.objects.create_user(username=request.POST["username"],email=request.POST["email"],password=request.POST["password"]) 
        new_user.save()
        #redirect("Jobs:home_page")
        
    return render(request,"accounts/signup.html")


def login_user(request:HttpRequest):
    """ This function view make log in and see if the data correct """
    msg = ""
    if request.method == "POST":
        user = authenticate(request, username=request.POST["username"],password=request.POST["password"]) 
        if user is not None:
            login(request,user)
            return redirect("Jobs:home_page")
        else:
           msg = "Wrong!! use correct credentials" 
        
    return render(request,"accounts/login.html",{"msg":msg})



def logout_user(request:HttpRequest):
    """ This function view make log out """
    logout(request)
        
    return redirect("Jobs:home_page")





signup.__doc__
login_user.__doc__
logout_user.__doc__