from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, get_user_model
from .forms import UserRegisterForm


User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            login(request, user)
            messages.success(request, f'Account created for {username}.')
            return redirect('main/pinventory.html')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form':form})


@login_required
def user_profile(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user':user})



