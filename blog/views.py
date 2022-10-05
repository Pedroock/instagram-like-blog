from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import UsersFollowers, UsersProfile
from users.forms import UsersFollowersForm
from blog.models import BlogPosts, BlogPostsLikes
from .forms import BlogCreatePost, BlogPostsLikesForm
from random import sample

# Create your views here.
@login_required
def blog_home(request):
    '''
    Sort followers and followed users
    '''
    followed_profiles_query = UsersFollowers.objects.filter(follower=request.user.profile)
    follower_profiles_query = UsersFollowers.objects.filter(followed=request.user.profile)
    followed_profiles_list = []
    followed_profiles_user_list = []
    follower_profiles_list = []
    for follower_model_instance in followed_profiles_query:
        followed_profile = follower_model_instance.followed
        followed_profiles_list.append(followed_profile)
        followed_profiles_user_list.append(followed_profile.user)
    '''
    Sort the elegible follower suggestions, 5 will be randomly chosen and will be sent to the template
    '''
    not_followed_profiles_query = UsersProfile.objects.exclude(user__in=followed_profiles_user_list).exclude(user=request.user)
    not_followed_profiles = []
    # tive q tacar numa lista pq as func do random n pega nos obj q o ORM do django retorna
    for profile in not_followed_profiles_query:
        not_followed_profiles.append(profile)
    # faz o sample e ve se vai sair com 5 ou menos e se for mais, capa pra 5
    if len(not_followed_profiles) < 6:
        suggested_profiles_list = sample(not_followed_profiles, len(not_followed_profiles))
    else:
        suggested_profiles_list = sample(not_followed_profiles, 5)
    # agr vai criar uma form para cada profile e manda junto com eles na lista [[profile, form], [profile, form]]
    suggestions_list = []
    for profile in suggested_profiles_list:
        suggested_profile_form = []
        suggested_profile_form.append(profile)
        suggested_profile_form.append(UsersFollowersForm({'follower': request.user.profile,
                                                          'followed': profile}))
        suggestions_list.append(suggested_profile_form)
    # ta meio confuso, mas da pra entender
    '''
    Sort posts and put them in a list
    >>>post_list = [] # -> 0-posts_obj, 1-likeform, 2-like obj, 3-is_liked , 4-index
                            5-commentform, 6-comment obj, 7-commetfirst
    For each post there will have a like form and obj, comment form and obj for each post 
    post_utils_list = [
        [post_obj, like_form, ...],
        [post_obj, like_form, ...],
        ...
    ]
    '''
    post_utils_list = []
    # First 20 newest posts
    post_objs = BlogPosts.objects.filter(profile__in=followed_profiles_list)[:20]
    # create the post-specific list
    post_index = 0
    for post_obj in reversed(post_objs):
        post_list = []
        post_index += 1
        post_author_profile = post_obj.profile
        # aqui fica o resto qnd eu fizer os models com like e comment
        like_form = BlogPostsLikesForm({'profile': request.user.profile, 'post': post_obj})
        like_obj = BlogPostsLikes.objects.filter(post=post_obj)
        if BlogPostsLikes.objects.filter(post=post_obj, profile=request.user.profile).first():
            is_liked = True
        else:
            is_liked = False
        
        post_list.append(post_obj)
        post_list.append(like_form)
        post_list.append(like_obj)
        post_list.append(is_liked)
        post_list.append(post_index)
        # append post list to post utils list
        post_utils_list.append(post_list)
    '''
    Create Post Form Part and like and comment form
    '''
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
    '''
    Context
    '''
    context = {
        'form': form,
        'post_utils_list': post_utils_list,
        'home': True, # só pra checkar o botao de upload
        'suggestions_list': suggestions_list,
    }
    return render(request, 'blog/blog_home.html', context)

