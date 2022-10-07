from django.shortcuts import render
from blog.forms import BlogPostsLikesForm, BlogPostsCommentsForm
from blog.models import BlogPostsLikes, BlogPostsComments
from users.forms import UsersFollowersForm
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from users.models import UsersFollowers
# Create your views here.
@csrf_exempt
def AjaxProfileFollow(request):
    if request.method == 'POST':
        form = UsersFollowersForm(request.POST)
        if form.is_valid():
            follow_instance = UsersFollowers.objects.filter(follower=form.cleaned_data['follower'], 
                                                            followed=form.cleaned_data['followed']).first()
            if follow_instance: 
                return JsonResponse({'error': 'follow instance exists'}, status=400)
            else:
                instance = form.save()
            # serializar é transforma info pra o ajax joga pro outro lado
            ser_instance = serializers.serialize('json', [instance,])
            return JsonResponse({"instance": ser_instance}, status=200)
        else:
            return JsonResponse({"error": form.errors}, status=400)
    else:
        return JsonResponse({"error": form.erros}, status=400)
        # 200 deu certo, 400 deu nn


@csrf_exempt
def AjaxProfileUnfollow(request):
    if request.method == 'POST':
        form = UsersFollowersForm(request.POST)
        if form.is_valid():
            print('form is valid')
            follower = form.cleaned_data['follower']
            followed = form.cleaned_data['followed']
            instance = UsersFollowers.objects.filter(follower=follower, followed=followed).first()
            instance.delete()
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'error'}, status=400)
    else:
        return JsonResponse({'status': 'error'}, status=400)
        # 200 deu certo, 400 deu nn


@csrf_exempt
def AjaxPostLike(request):
    if request.method == 'POST':
        form = BlogPostsLikesForm(request.POST)
        if form.is_valid():
            post_like_check = BlogPostsLikes.objects.filter(post=form.cleaned_data['post'],
                                             profile=form.cleaned_data['profile']).first()
            if post_like_check:
                JsonResponse({'status': 'error'}, status=400)
            else:
                form.save()
                return JsonResponse({'status': 'foi'}, status=200)
        else:
            JsonResponse({'status': 'error'}, status=400)
    else:
        return JsonResponse({'status': 'error'}, status=400)




@csrf_exempt
def AjaxPostUnlike(request):
    if request.method == 'POST':
        form = BlogPostsLikesForm(request.POST)
        if form.is_valid():
            print('form is valid')
            post = form.cleaned_data['post']
            profile = form.cleaned_data['profile']
            instance = BlogPostsLikes.objects.filter(post=post, profile=profile).first()
            if instance:
                instance.delete()
            else:
                return JsonResponse({'status': 'error'}, status=400) 
            return JsonResponse({'status': 'success'}, status=200)
        else:
            return JsonResponse({'status': 'error'}, status=400)
    else:
        return JsonResponse({'status': 'error'}, status=400)
        # 200 deu certo, 400 deu nn


@csrf_exempt
def AjaxPostComment(request):
    if request.method == 'POST':
        form = BlogPostsCommentsForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'foi'}, status=200)
        else:
            JsonResponse({'status': 'error'}, status=400)
    else:
        return JsonResponse({'status': 'error'}, status=400)