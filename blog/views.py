from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogCreatePost
from .methods import sort_follower_suggestions, sort_home_posts


@login_required
def blog_home(request):
    if request.method == 'POST':
        if 'post-post' in request.POST:
            form = BlogCreatePost(request.POST, request.FILES)
            if form.is_valid():
                form.save()
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