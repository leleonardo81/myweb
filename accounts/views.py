from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup_page.html', {'form':form})

def loggedin(request):
    if request.method ==  'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('HomePage:homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login_page.html', {'form':form})
    
def loggedout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('HomePage:homepage')