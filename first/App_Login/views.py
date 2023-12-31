from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
# Create your views here.

# Authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

# Forms and Models
from App_Login.models import Profile
from App_Login.forms import ProfileForm,SignUpForm

#  Messages
from django.contrib import messages

# SignUp page View
def sign_up(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Succesfully")
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request,'App_Login/signup.html', context={'form':form})

def login_user(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in")
                return HttpResponseRedirect(reverse('App_Shop:home'))
    return render(request,'App_Login/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request,"You are Logged out")
    return HttpResponseRedirect(reverse('App_Shop:home'))


@login_required
def user_profile(request):
    profile=Profile.objects.get(user=request.user)
    form=ProfileForm(instance=profile)
    if request.method=="POST":
       form=ProfileForm(request.POST,instance=profile)
       if form.is_valid():
           form.save()
           messages.success(request,"Changes Saved")
           form=ProfileForm(instance=profile)
    return render(request,'App_Login/change_profile.html',context={'form':form})

    