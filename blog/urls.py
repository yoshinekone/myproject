from django.urls import path
from .views import frontpage,postpage

urlpatterns = [
    path("",frontpage, name = "frontpage"),
    path("postpage/<slug:post_id>/",postpage,name = 'postpage')
]
