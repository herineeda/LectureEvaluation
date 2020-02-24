from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Profile
# from .models import Profile

# Create your views here.
def signup(request):
    if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                email = request.POST["email"]
                if User.objects.filter(username=email).exists():
                    #return HttpResponse("이미 존재하는 이메일입니다.")
                    return render(request, 'sameEmail.html')
            # try:
            #     if User.objects.filter(username=email).exists():
            #         raise emailError
            # except emailError:
            #     return HttpResponse("이미 존재하는 이메일입니다.")
                else:
                    user = User.objects.create_user(username=request.POST['email'], password=request.POST['password1'])
                    major = request.POST["major"]
                    undergradNum = request.POST["undergradNum"]
                    studentname = request.POST.get('studentname', '')
                    #studentname = request.POST["studentname"]
                    profile = Profile(email=email, user=user, major=major, undergradNum=undergradNum, studentname=studentname)
                    profile.save()
                    auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend') #로그인 하는 함수
                    return redirect('home')
    return render(request, 'signup.html')  


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def main(request):
    return render(request, 'main.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

# def confirmId(request):
#     if request.POST['password1'] == request.POST['password2']: