from django import forms
from autoslug import AutoSlugField

from .models import Comment, Post

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class PostForm(forms.ModelForm):
    slug = AutoSlugField(populate_from='title')
    class Meta:
        model = Post
        fields = ('category', 'title', 'intro', 'body', 'status', 'image')