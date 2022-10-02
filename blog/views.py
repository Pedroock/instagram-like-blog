from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import UsersFollowers, UsersProfile
from users.forms import UsersFollowersForm
from blog.models import BlogPosts
from .forms import BlogCreatePost
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
    >>>post_list = [] # -> 0-posts_obj, 1-likeform, 2-like obj, 3-commentform, 4-comment obj, 5-commetfirst
    For each post there will have a like form and obj, comment form and obj for each post 
    post_utils_list = [
        [post_obj, like_form, ...],
        [post_obj, like_form, ...],
        ...
    ]
    '''
    post_utils_list = []
    # First 20 newest posts
    post_obj = BlogPosts.objects.filter(profile__in=followed_profiles_list)[:20]
    # create the post-specific list
    for post_obj in post_obj:
        post_list = []
        post_author_profile = post_obj.profile
        # aqui fica o resto qnd eu fizer os models com like e comment
        post_list.append(post_obj)

        # append post list to post utils list
        post_utils_list.append(post_list)



    '''
    Create Post Form Part
    '''
    if request.method == 'POST':
        form = BlogCreatePost(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
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

