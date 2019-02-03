from django.shortcuts import render, redirect
from . import forms
from .models import Friend
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def check_exist(now_user):
    for frend in Friend.objects.all():
        if frend.username == now_user:
            return True
    return False
            
def friendlist(request):
    response = {
        'friend' : Friend.objects.order_by('name'),
        'already' : check_exist(request.user),
    } 
    return render(request, 'Friends/friend.html', response)


def friend_detail(request, slug):
    frend = Friend.objects.get(username=User.objects.get(username=slug))
    return render(request, 'Friends/detail.html', {'friend':frend})

@login_required(login_url="/accounts/login")
def add_friend(request):
    if request.method == 'POST':
        form = forms.FriendForm(request.POST)
        if form.is_valid():
            a=form.save(commit=False)
            a.username = request.user 
            a.name =  form.cleaned_data['name'].capitalize()
            a.save()
            return redirect('Friends:friend') 
    else:
        now_user = request.user
        for friend in Friend.objects.all():
            if friend.username == now_user :
                return redirect("Friends:detail", request.user)
        form = forms.FriendForm()
    return render(request, 'Friends/add_friend.html', {'form':form})

