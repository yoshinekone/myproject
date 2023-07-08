from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class PostGood(models.Model):
    post = models.ForeignKey(Post,related_name='goods',on_delete=models.CASCADE)
    log = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments',on_delete=models.CASCADE)
    body = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class CommentGood(models.Model):
    comment = models.ForeignKey(Comment,related_name='goods',on_delete=models.CASCADE)
    log = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)