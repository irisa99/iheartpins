from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout
from .models import *
import uuid


@login_required
def account(request):
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


def Logout(request):
    logout(request)
    return redirect('/')

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


def send_forget_password_mail(email , token ):
    subject = '[Iheartpins] - Reset your Password'
    message = f'Hi , click on the link to reset your password http://127.0.0.1:8000/accounts/resetpassword/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True


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


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user_object = User.objects.filter(email = email).first()
        if user_object is None:
            messages.success(request, 'email not found.')
            return redirect('forgotpassword')
        
        user_object = User.objects.get(email = email)
        forgot_token = str(uuid.uuid4())
        profile_object= Profile.objects.get(user = user_object)
        profile_object.forgot_password_token = forgot_token
        profile_object.save()
        send_forget_password_mail(email, forgot_token)
        messages.success(request, 'An email is sent.')
        return redirect('forgotpassword')

    return render(request, 'accounts/forgot_password.html')

def reset_password(request, resettoken):
    context = {}
    
    try:
        profile_object = Profile.objects.filter(forgot_password_token = resettoken).first()
        context = {'user_id' : profile_object.user.id}
        print('user_id ', context )
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            user_id = request.POST.get('user_id')
            print(new_password)
            if user_id is  None:
                print(user_id)
                messages.success(request, 'No user found.')
                return redirect(f'/accounts/resetpassword/{resettoken}')
                
            
            if  new_password != confirm_password:
                print(new_password)
                messages.success(request, 'both should  be equal.')
                return redirect(f'/accounts/resetpassword/{resettoken}')

            user_object = User.objects.get(id = user_id)
            user_object.set_password(new_password)
            user_object.save()
            messages.success(request, 'Your Password have Changed.')
            return redirect('/accounts/login')   
    except Exception as e:
        print(e)
    return render(request, 'accounts/reset_password.html', context)