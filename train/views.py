from django.shortcuts import render,redirect
from .models import *
from django.db.models import Q,Sum
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

def login_page(request):

    if request.method=="POST":
        data=request.POST
        username=data.get('username')
        password=data.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request,"Invalid Username")
            return redirect("/login")
        user=authenticate(username=username,password=password)
        if user is None:
            messages.error(request,"Invalid Password")
            return redirect("/login/")
        else:
            login(request,user)
            return redirect("/page/")

    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        data=request.POST
        first_name=data.get("first_name")
        last_name=data.get("last_name")
        username=data.get("username")
        password=data.get("password")

        user=User.objects.filter(username=username)
        if user.exists():
            messages.error(request,"username already taken")
            return redirect("/register/")

        user=User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Account Created Successfully")
        return redirect("/register/")

    return render(request,"register.html")
@login_required
def page(request):
    if request.method=="POST":
        data=request.POST
        name=data.get("name")
        train.objects.create(user=request.user,name=name)
        return redirect("/page/")
    todos=train.objects.filter(user=request.user)
    print(todos)
    context={'todo':todos}
    return render(request,"page.html",context)
def logout_page(request):
    logout(request)
    return redirect("/login/")
def delete_page(request,id):
    to=train.objects.get(id=id)
    to.delete()
    return redirect("/page/")
def update_page(request,id):
    to=train.objects.get(id=id)
    to.status=True
    to.save()
    return redirect("/page/")
