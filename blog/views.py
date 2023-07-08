from django.shortcuts import render, redirect
from  .forms import PostForm, CommentForm, PostGoodForm , CommentGoodForm
from .models import Post,Comment

# Create your views here.
def frontpage(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontpage')

    form = PostForm
    posts = Post.objects.all().order_by('-id')
    context = {'form':form,'posts':posts}
    return render(request,"frontpage.html",context)


def postpage(request,post_id):

    post = Post.objects.get(id = post_id)
    
    if request.method == 'POST':
        if 'comment_button'  in request.POST:
            form = CommentForm(request.POST)
            if form.is_valid():
                commnet = form.save(commit=False)
                commnet.post = post
                commnet.save()
                return redirect('postpage', post_id = post.id)
            
        if 'post_good_button' in request.POST:  
            form = PostGoodForm(request.POST)
            if form.is_valid():
                postGood = form.save(commit=False)
                postGood.post =post
                postGood.log = 'いいね'
                postGood.save()
                return redirect('postpage', post_id = post.id)

        if 'comment_good_button' in request.POST:
            form = CommentGoodForm(request.POST)
            if form.is_valid():
                commentGood = form.save(commit=False)
                comment = Comment.objects.get(id = request.POST.get('comment_id'))
                commentGood.comment = comment
                commentGood.log = 'いいね'
                commentGood.save()
                return redirect('postpage', post_id = post.id)

    form = CommentForm
    formPostGood = PostGoodForm
    formCommentGood = CommentGoodForm
    context = {'post':post, 'form':form, 'formPostGood':formPostGood, 'formCommentGood':formCommentGood}
    return render(request,'postpage.html', context)