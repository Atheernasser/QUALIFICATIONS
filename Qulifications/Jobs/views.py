from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Jobtitle

# Create your views here.

def home(request:HttpRequest):
    """ This function view takes objects from models (Jobtitle) and returns them to template """

    bank = Jobtitle.objects.get(namejob="Bank Accountant")
    hr = Jobtitle.objects.get(namejob="HR Junior Recruiter")
    isa = Jobtitle.objects.get(namejob="Information Security Analyst")
    it = Jobtitle.objects.get(namejob="IT Support Analyst")
    dba = Jobtitle.objects.get(namejob="Oracle Dba")

    return render(request,"jobs/home.html",{"bank":bank , "hr": hr , "isa":isa ,"it":it , "dba": dba})




home.__doc__