from django.shortcuts import render,redirect
from.models import *
from django.contrib.auth.models import User
from  django.contrib.auth import authenticate
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,"Home.html")
def user(request):

    if request.POST:
        name=request.POST['name']
        address=request.POST['Address']
        username=request.POST['username']
        password=request.POST['password']
        User_exist=User.objects.filter(username=username).exists()
        if not User_exist:
        
            try:
                u=User.objects.create_user(username=username,password=password,is_staff=0,is_active=1)
                u.save()
                r=Userreg.objects.create(name=name,Address=address,username=username)
                r.save()
            except Exception as e:
                messages.info(request,e)
                print(e)
            else:
                messages.info(request,"REGISTRATION SUCCESSFULLY")
        else:
            messages.info(request,"USER ALREADY EXISTED")       
    return render(request,"User.html")
def authority(request):
    if request.POST:
        authorityname=request.POST['authorityname']
        officialname=request.POST['officialname']
        address=request.POST['address']
        phonenumber=request.POST['phonenumber']
        username=request.POST['username']
        password=request.POST['password']
        User_exist=User.objects.filter(username=username).exists()
        if not User_exist:
        
            try:
                u=User.objects.create_User(username=username,password=password,is_staff=0,is_active=1)
                u.save()
                r=authority.objects.create(authorityname=authorityname,officialname=officialname,address=address,phonenumber=phonenumber,username=username)
                r.save()
            except Exception as e:
                messages.info(request,e)
                print(e)
            else:
                messages.info(request,"REGISTRATION SUCCESSFULLY")
        else:
            messages.info(request,"USER ALREADY EXISTED")       
    return render(request,"authority.html")
# def login(request):
    
    
#     return render(request,"Login.html")