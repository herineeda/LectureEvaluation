from django.shortcuts import render
from django.db.models import Q # filter 조건을 or로 묶기 위해서 사용
from crud.models import Lecture # lecture 가져오기

# 홈 화면 보여주기
def home(request):
    return render(request, 'home.html')

# 모든 강의를 이름 순으로 보여주기
def showLecture(request):
    subject = Lecture.objects.order_by('lectureName')
    return render(request, 'showLecture.html', {'subject':subject})

# 전공 강의만 보여주기
def filteringM(request):
    subject = Lecture.objects.filter(separation__icontains='전공')
    return render(request, 'showLecture.html', {'subject':subject})

# 교양 강의만 보여주기
def filteringL(request):
    subject = Lecture.objects.filter(separation__icontains='교양')
    return render(request, 'showLecture.html', {'subject':subject})

# 검색 결과 보여주기
def searchResult(request):
        texts = request.GET.get('txt')
        try:
            result = Lecture.objects.filter(Q(lectureName__icontains=texts) | Q(professor__icontains=texts))
        except:
            result = Lecture.objects.all()
        return render(request, 'searchResult.html', {'result':result})
