import imp
from django import forms
from .models import BlogPosts, BlogPostsLikes

class BlogCreatePost(forms.ModelForm):
    desc = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insert a description'}))

    class Meta:
        model = BlogPosts
        fields = ['profile', 'image', 'desc']


class BlogPostsLikesForm(forms.ModelForm):
    class Meta:
        model = BlogPostsLikes
        fields = ['profile', 'post']

