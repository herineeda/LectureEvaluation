from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth
# from .models import Profile

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['email'], password=request.POST['password1'])
            auth.login(request, user) #로그인 하는 함수
            return redirect('main')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')

def logout(request):
    auth.logout(request)
    return redirect('main')