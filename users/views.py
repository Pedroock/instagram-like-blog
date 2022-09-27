from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .forms import UsersLoginForm, UsersProfileUpdateForm, UsersRegisterForm
from .models import UsersProfile
from django.contrib.auth.decorators import login_required


# Create your views here.
def users_register(request):
    if request.method == 'POST':
        form = UsersRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            print(new_user)
            login(request, new_user)
            return redirect('home')
    else:
        form = UsersRegisterForm()
    context={
        'form': form
    }    
    return render(request, 'users/register.html', context)


def users_login(request):
    if request.method == 'POST':
        form = UsersLoginForm(request.POST)
        if form.is_valid():
            new_user = authenticate(username=form.cleaned_data['username_or_email'], 
                                    password=form.cleaned_data['password'])
            if new_user is None:
                new_user = authenticate(email=form.cleaned_data['username_or_email'], 
                                        password=form.cleaned_data['password'])
            login(request, new_user)
            return redirect('home')
    else:
        form = UsersLoginForm()
    context={
        'form': form
    }    
    return render(request, 'users/login.html', context)


def users_logout(request):
    logout(request)
    return redirect('register')


@login_required
def users_profile(request, pk):
    profile_user = User.objects.filter(pk=pk).first()
    profile = UsersProfile.objects.filter(user=profile_user).first()
    context = {'profile': profile}
    return render(request, 'users/profile.html', context)


@login_required
def users_profile_update(request, pk):
    profile_user = User.objects.filter(pk=pk).first()
    profile = UsersProfile.objects.filter(user=profile_user).first()
    if request.method == 'POST':
        form = UsersProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk)
    else:
        form = UsersProfileUpdateForm(instance=profile)
    context = {'form': form}
    return render(request, 'users/profile_update.html', context)