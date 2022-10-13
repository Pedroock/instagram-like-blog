import imp
from django import forms
from .models import BlogPosts, BlogPostsLikes, BlogPostsComments

class BlogCreatePost(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Insert a description', 'rows': 8}))
    class Meta:
        model = BlogPosts
        fields = ['profile', 'image', 'desc']


class BlogPostsLikesForm(forms.ModelForm):
    class Meta:
        model = BlogPostsLikes
        fields = ['profile', 'post']


class BlogPostsCommentsForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insert a comment...'}))
    class Meta:
        model = BlogPostsComments
        fields = ['profile', 'post', 'comment']
