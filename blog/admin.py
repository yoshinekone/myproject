from django.contrib import admin
from .models import Post,PostGood,Comment, CommentGood
# Register your models here.

admin.site.register(Post)
admin.site.register(PostGood)
admin.site.register(Comment)
admin.site.register(CommentGood)