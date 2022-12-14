from multiprocessing import context
from turtle import pos
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogCreatePost
from .methods import sort_follower_suggestions, sort_home_posts, detail_post, discover_posts


@login_required
def blog_home(request):
    if request.method == 'POST':
        if 'post-post' in request.POST:
            print('post-post')
            form = BlogCreatePost(request.POST, request.FILES)
            if form.is_valid():
                print('form is valid')
                form.save()
                print('saved')
                return redirect('home')
            else:
                form = BlogCreatePost({'profile': request.user.profile})
    else:
        form = BlogCreatePost({'profile': request.user.profile})
    context = { 
        'home': True, 
        'form': form,
        'post_utils_list': sort_home_posts(request),
        'suggestions_list': sort_follower_suggestions(request),
    }
    return render(request, 'blog/blog_home.html', context)


@login_required
def blog_post_detail(request, pk):
    return render(request, 'blog/blog_post_detail.html', {'post': detail_post(request, pk)})


@login_required
def blog_discover(request):
    context = {
        'discover_posts': discover_posts(request),
        'discover': True
    }
    return render(request, 'blog/blog_discover.html', context)