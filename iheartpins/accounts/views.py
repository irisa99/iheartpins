from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate

@login_required
def account_home(request):
    return render(request , 'accounts/profile.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_object = User.objects.filter(email = email).first()
        if user_object is None:
            messages.success(request, 'email not found.')
            return redirect('/accounts/login')
        profile_object = Profile.objects.filter(user = user_object).first()
        if not profile_object.is_verified:
            messages.success(request, 'Profile is not verified check your email.')
            return redirect('/accounts/login')
        user = authenticate(request , email = email , password = password)
        print(user)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')
        auth_login(request , user)
        return redirect('/accounts')
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(password)
        try:
            if User.objects.filter(username=username).first():
                messages.error(request, 'Username is already Taken')
                return redirect('/accounts/register')
            if User.objects.filter(email=email).first():
                messages.error(request, 'email is already Taken')
                return redirect('/accounts/register')

            user_object = User(username = username, email=email)
            user_object.set_password(password)
            user_object.save()
            auth_token = str(uuid.uuid4())
            profile_object = Profile.objects.create(user = user_object, auth_token = auth_token)
            profile_object.save()
            send_account_verify_mail(email , auth_token)
            return redirect('/accounts/tokenverify')
        except Exception as e:
            print(e)
            return redirect('/')
    return render(request, 'accounts/register.html')

def TokenVerify(request):
    return render(request, 'accounts/token.html')


def send_account_verify_mail(email, token):
    subject = "[Iheartpins] - Please Verify your Email Account "
    mail_message = f'Thank you for registration on Iheartpins, Click here to verify your email http://localhost:8000/accounts/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, mail_message , email_from ,recipient_list ) 


def verify(request , auth_token):
    try:
        profile_object = Profile.objects.filter(auth_token = auth_token).first()
        if profile_object:
            if profile_object.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_object.is_verified = True
            profile_object.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/')
