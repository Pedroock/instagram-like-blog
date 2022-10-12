from users.models import UsersFollowers, UsersProfile
from users.forms import UsersFollowersForm
from blog.models import BlogPosts, BlogPostsLikes
from .forms import BlogPostsCommentsForm, BlogPostsLikesForm, BlogPostsComments
from random import sample


def sort_follow_dict(request):
    '''
    Sort and return two lists, one of the profiles that follow the request.user.profile and one of the profiles that are being followed by, inside a dictionary {'followers': [followers_list], 'followeds': [followeds_list]}
    '''
    follower_profiles_query = UsersFollowers.objects.filter(followed=request.user.profile)
    followed_profiles_query = UsersFollowers.objects.filter(follower=request.user.profile)
    follower_profiles_list = []
    followed_profiles_list = []
    for follwer_model_instance in follower_profiles_query:
        follower_profiles_list.append(follwer_model_instance.follower)
    for followed_model_instance in followed_profiles_query:
        followed_profiles_list.append(followed_model_instance.followed)
    return {'followers': follower_profiles_list, 'followeds': followed_profiles_list}


def sort_follower_suggestions(request):
    '''
    Sort the elegible follower suggestions, it will be five random unfollowed users. This will return a list o dictionaries {'profile': profile, 'form': form}
    '''
    followed_users = []
    for profile in sort_follow_dict(request)['followeds']:
        followed_users.append(profile.user)
    not_followed_profiles_query = UsersProfile.objects.exclude(user__in=followed_users).exclude(user=request.user)
    not_followed_profiles = []
    for profile in not_followed_profiles_query:
        not_followed_profiles.append(profile)
    if len(not_followed_profiles) < 6:
        suggested_profiles_list = sample(not_followed_profiles, len(not_followed_profiles))
    else:
        suggested_profiles_list = sample(not_followed_profiles, 5)
    suggestions_list = []
    for profile in suggested_profiles_list:
        suggested_profile_form = {
            'profile': profile,
            'form': (UsersFollowersForm({'follower': request.user.profile, 'followed': profile}))
        }
        suggestions_list.append(suggested_profile_form)
    return suggestions_list


def sort_home_posts(request):
    '''
    This will get the 20 latest posts from the profiles followed by the request.user.profile and will put it in a dictionary {'post_obj': post_obj, 'like_form': like_form, 'like_obj': like_obj, 'is_liked': True, 
                'comment_form': comment_form, 'comment_obj': comment_obj, 'comment_first': comment_first,
                'post_index': post_index,
               }
    and theese dicts will be stored in a list that will be looped in the template
    '''
    post_objs = BlogPosts.objects.filter(profile__in=sort_follow_dict(request)['followeds'])[:20]
    post_index = 0
    post_utils_list = []
    for post_obj in reversed(post_objs):
        like_form = BlogPostsLikesForm({'profile': request.user.profile, 'post': post_obj})
        like_obj = BlogPostsLikes.objects.filter(post=post_obj)
        if BlogPostsLikes.objects.filter(post=post_obj, profile=request.user.profile).first():
            is_liked = True
        else:
            is_liked = False
        comment_form = BlogPostsCommentsForm({'profile': request.user.profile, 'post': post_obj})
        comment_obj = BlogPostsComments.objects.filter(post=post_obj) 
        comment_first = BlogPostsComments.objects.filter(post=post_obj).last()
        post_index = post_obj.pk
        post_dict = {
            'post_obj': post_obj, 'like_form': like_form, 'like_obj': like_obj, 'is_liked': is_liked, 
            'comment_form': comment_form, 'comment_obj': comment_obj, 'comment_first': comment_first,
            'post_index': post_index,
        }
        post_utils_list.append(post_dict)
    return post_utils_list


def detail_post(request, pk):
    '''
    dictionary {'post_obj': post_obj, 'like_form': like_form, 'like_obj': like_obj, 'is_liked': True, 
                'comment_form': comment_form, 'comment_obj': comment_obj, 'post_index': post_index,
               }
    will be created for the detail post
    '''
    post_obj = BlogPosts.objects.filter(pk=pk).first()
    if BlogPostsLikes.objects.filter(post=post_obj, profile=request.user.profile).first():
        is_liked = True
    else:
        is_liked = False
    post = {
        'post_obj': post_obj,
        'like_form': BlogPostsLikesForm({'profile': request.user.profile, 'post': post_obj}),
        'like_obj': BlogPostsLikes.objects.filter(post=post_obj),
        'is_liked': is_liked,
        'comment_form': BlogPostsCommentsForm({'profile': request.user.profile, 'post': post_obj}),
        'comment_obj': BlogPostsComments.objects.filter(post=post_obj),
        'post_index': pk
    }
    return post