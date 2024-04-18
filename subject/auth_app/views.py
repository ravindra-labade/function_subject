from random import choice

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from django.core.mail import send_mail
from .models import Otp
from subject.settings import EMAIL_HOST_USER
def user_login(request):
    template_name = 'auth_app/login.html'
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        user = authenticate(username=un, password=pw)
        if user:
            login(request, user)
            return redirect('show_url')
        else:
            return HttpResponse('plz enter proper username and password')
    return render(request, template_name)

def user_signup(request):
    template_name = 'auth_app/register.html'
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            un = form.cleaned_data.get( 'username' )
            pw = form.cleaned_data.get( 'password' )
            em = form.cleaned_data.get( 'email' )
            user = User.objects.create_user(username=un, password=pw, email=em, is_active=False )

            otp = ''
            li = [str(i) for i in range(0,10)]
            for i in range(4):
                otp += choice(li)

            send_mail('otp', f'your otp is {otp}', EMAIL_HOST_USER,
                      [user.email]
                      )

            otp = Otp(user=user, otp=int(otp))
            otp.save()

            return redirect('otp_url')
    context = {'form': form}
    return render(request, template_name, context)


def otp_view(request):
    if request.method == "POST":
        un = request.POST['un']
        pw = request.POST['pw']
        otp = request.POST['otp']

        try:
            user = User.objects.get(username=un)
            if user.check_password(pw):
                otp = Otp.objects.get(user=user, otp=otp)
                print(otp)
                if otp:
                    user.is_active = True
                    user.save()
                    return redirect('login_url')
        except:
            return HttpResponse('Something went Wrong')
    template_name = 'auth_app/otp.html'
    context = {}
    return render(request, template_name, context)

def user_logout(request):
    logout(request)
    return redirect('login_url')

@login_required(login_url='login_url')
def change_password(request):
    if request.method == 'POST':
        old = request.POST['old']
        new = request.POST['new']
        user = request.user
        res = user.check_password(old)
        if res:
            user.set_password(new)
            user.save()
            return redirect('login_url')
    return render(request, 'auth_app/cpass.html')
