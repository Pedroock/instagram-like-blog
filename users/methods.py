from blog.models import BlogPosts, BlogPostsLikes
from blog.forms import BlogPostsComments


def sort_profile_posts(profile):
    '''
    Will sort the profile posts and will add the comment and like objs for the hover
    '''
    posts_query = BlogPosts.objects.filter(profile=profile)
    profile_posts = []
    for post in posts_query:
        post_dict = {
            'post_obj': post,
            'comment_obj': BlogPostsComments.objects.filter(post=post),
            'like_obj': BlogPostsLikes.objects.filter(post=post)
        }
        profile_posts.insert(0, post_dict)
    return profile_posts