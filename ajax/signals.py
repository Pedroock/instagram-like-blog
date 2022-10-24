from turtle import pos
from django.dispatch import receiver
from users.models import UsersProfile, UsersFollowers
from  django.db.models.signals import post_save
from django.contrib.auth.models import User
from blog.models import BlogPosts, BlogPostsLikes, BlogPostsComments
from ajax.models import AjaxNotification

@receiver(post_save, sender=BlogPostsLikes)
def like_post(sender, instance, created, **kwargs):
    if created:
        notifier = instance.profile
        action = 'liked your'
        post = instance.post
        receiver = instance.post.profile
        notification = AjaxNotification(
            notifier=notifier, action=action, post=post, receiver=receiver, like_obj=instance
        )
        notification.save()


@receiver(post_save, sender=BlogPostsComments)
def comment_post(sender, instance, created, **kwargs):
    if created:
        notifier = instance.profile
        action = 'commented your'
        post = instance.post
        receiver = instance.post.profile
        notification = AjaxNotification(
            notifier=notifier, action=action, post=post, receiver=receiver, comment_obj=instance
        )
        notification.save()

@receiver(post_save, sender=UsersFollowers)
def follow(sender, instance, created, **kwargs):
    if created:
        notifier = instance.follower
        action = 'followed your profile'
        receiver = instance.followed
        notification = AjaxNotification(
            notifier=notifier, action=action, receiver=receiver, follow_obj=instance
        )
        notification.save()