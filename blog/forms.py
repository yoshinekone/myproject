from django import forms
from .models import Post,Comment,PostGood, CommentGood

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']

class PostGoodForm(forms.ModelForm):
    class Meta:
        model = PostGood
        fields = []

class CommentGoodForm(forms.ModelForm):
    class Meta:
        model = CommentGood
        fields = []