from django.shortcuts import render
from django.db.models import Q # filter 조건을 or로 묶기 위해서 사용
from django.core.paginator import Paginator # pagination을 하기 위해서 가져옴
from crud.models import Lecture, Evals # lecture 가져오기

# 홈 화면 + 강의평을 4개씩 보여주기
def home(request):
    evalList = Evals.objects.order_by('pub_date').reverse().all()
    paginator = Paginator(evalList, 4)
    page = request.GET.get('page')
    evals = paginator.get_page(page)
    return render(request, 'home.html', {'evals':evals})

# 모든 강의를 이름 순으로 보여주기
def showLecture(request):
    lectures = Lecture.objects.order_by('lectureName')
    return render(request, 'lecturelist.html', {'lectures':lectures})

# 전공 강의만 보여주기
def filteringM(request):
    lectures = Lecture.objects.filter(separation__icontains='전공')
    return render(request, 'lecturelist.html', {'lectures':lectures})

# 교양 강의만 보여주기
def filteringL(request):
    lectures = Lecture.objects.filter(separation__icontains='교양')
    return render(request, 'lecturelist.html', {'lectures':lectures})

# 검색 결과 보여주기
def searchResult(request):
        texts = request.GET.get('txt')
        try:
            result = Lecture.objects.filter(Q(lectureName__icontains=texts) | Q(professor__icontains=texts))
        except:
            result = Lecture.objects.all()
        return render(request, 'searchResult.html', {'result':result})
