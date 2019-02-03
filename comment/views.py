from django.shortcuts import render, redirect
from .import forms
from .models import Comment, Reply, Like
from django.contrib.auth.decorators import login_required

def comment_listed(request):
    response = {
         'comment' : Comment.objects.all(),
         'form' : forms.CreateCommentForm(),
         'reply_form' : forms.CreateReplyForm(),
         'likes' : len(Like.objects.all()),
         'first3like' : Like.objects.all()[:3],
         'restlike' : len(Like.objects.all())-3,
    }
    return render(request, 'comment/comments_page.html', response)

@login_required(login_url="/accounts/login")
def comment_create(request):
    comment_form = forms.CreateCommentForm(request.POST)
    if request.method == "POST" and comment_form.is_valid():
        a= comment_form.save(commit=False)
        a.username = request.user
        a.save()
    return redirect('comment:comment')
  
@login_required(login_url="/accounts/login")
def replying(request, comment_id):
    reply_form = forms.CreateReplyForm(request.POST)
    if request.method == "POST" and reply_form.is_valid():
        Reply.objects.create(
            username = request.user,
            reply_message = reply_form.cleaned_data['replies'],
            comment = Comment.objects.get(id=comment_id),
        )        
    return redirect('comment:comment')

@login_required(login_url="/accounts/login")
def liking(request):
    usr = request.user
    for like in Like.objects.all():
        if like.username == usr:
            return redirect('comment:comment')
    Like.objects.create(
        username = request.user
    )
    return redirect('comment:comment')