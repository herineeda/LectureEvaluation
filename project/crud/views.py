from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Lecture, Eval
# Create your views here.

def lecturelist(request):
    lectures = Lecture.objects
    return render(request, 'lecturelist.html', {'lectures' : lectures})

def write(request):
    return render(request, 'write.html')

def evallist(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    
    return render(request, 'evallist.html', {'lect' : lect})

def evaldetail(request, evals_id):
    evals = get_object_or_404(Eval, pk = evals_id)
    return render(request, 'evaldetail.html', {'evals' : evals})

def create(request):
    new_eval = Eval()
    new_eval.ratio_select = request.GET.get('ratio_select')
    new_eval.pub_date = timezone.datetime.now()
    new_eval.texts = request.GET.get('texts')
    new_eval.save()
    return redirect('/write/' + str(new_eval.id))

def eval_delete(request, evals_id):
    evals = Eval.objects.get(id = evals_id)
    evals.delete()
    return redirect('lecturelist')
