from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Lecture, Evals
# Create your views here.

def lecturelist(request):
    lectures = Lecture.objects
    return render(request, 'lecturelist.html', {'lectures' : lectures})

def write(request):
    return render(request, 'write.html')

#강의 당 평가글 목록
def evallist(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    
    return render(request, 'evallist.html', {'lect' : lect})

#평가글 자세히 보기
def evaldetail(request, evals_id):
    evals = get_object_or_404(Evals, pk = evals_id)
    return render(request, 'evaldetail.html', {'evals' : evals})

#평가글 전송
def create(request):
    new_eval = Evals()
    new_eval.title = request.POST['title']
    #new_eval.ratio_select = request.GET.get('ratio_select')
    new_eval.pub_date = timezone.datetime.now()
    new_eval.body = request.POST['body']
    new_eval.save()
    return redirect('/write/' + str(new_eval.id))

#평가글 삭제
def eval_delete(request, evals_id):
    evals = Evals.objects.get(id = evals_id)
    evals.delete()
    return redirect('lecturelist')

#평가글 수정
def edit(request, evals_id):

    evaledit = Evals.objects.get(pk = evals_id)
    
    if request.method == "POST":
        evaledit.title = request.POST['title']
        evaledit.pub_date = timezone.datetime.now()
        evaledit.body = request.POST['body']
        evaledit.save()
        return redirect('/write/' + str(evaledit.id))
    return render(request, 'edit.html', {'evaledit' : evaledit})


        