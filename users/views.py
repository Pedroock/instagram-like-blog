from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from .forms import UsersLoginForm, UsersProfileUpdateForm, UsersRegisterForm, UsersFollowersForm
from .models import UsersProfile, UsersFollowers
from django.contrib.auth.decorators import login_required
from blog.models import BlogPosts


# Create your views here.
def users_register(request):
    if request.method == 'POST':
        form = UsersRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password1'])
            user.save()
            print(user)
            login(request, user)
            return redirect('home')
    else:
        form = UsersRegisterForm()
    context={
        'form': form
    }    
    return render(request, 'users/users_register.html', context)


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
    return render(request, 'users/users_login.html', context)


def users_logout(request):
    logout(request)
    return redirect('register')


@login_required
def users_profile(request, pk):
    profile_user = User.objects.filter(pk=pk).first()
    profile = UsersProfile.objects.filter(user=profile_user).first()
    followers = []
    followed = []
    follow_check = False
    followers_query = UsersFollowers.objects.filter(followed=profile)
    followed_query = UsersFollowers.objects.filter(follower=profile)
    for instance in followed_query:
        followed.append(instance.followed)
    for instance in followers_query:
        followers.append(instance.follower)
    print(follow_check)
    context = {
        'profile': profile,
        'posts': BlogPosts.objects.filter(profile=profile),
        'followers': followers,
        'followeds': followed,
        'follow_form': UsersFollowersForm({'follower': request.user, 'followed': profile}),
        }
    return render(request, 'users/users_profile.html', context)


@login_required
def users_profile_update(request, pk):
    profile_user = User.objects.filter(pk=pk).first()
    profile = UsersProfile.objects.filter(user=profile_user).first()
    if profile != request.user.profile:
        return redirect('profile', profile.user.pk)
    if request.method == 'POST':
        form = UsersProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile', pk)
    else:
        form = UsersProfileUpdateForm(instance=profile)
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'users/users_profile_update.html', context)