from django.contrib import admin
from .models import BlogPosts, BlogPostsLikes

# Register your models here.
admin.site.register(BlogPosts)
admin.site.register(BlogPostsLikes)