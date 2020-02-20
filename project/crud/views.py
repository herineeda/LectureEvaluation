from django.shortcuts import render, get_object_or_404
from .models import Lecture
# Create your views here.

def lecturelist(request):
    lectures = Lecture.objects
    return render(request, 'lecturelist.html', {'lectures' : lectures})

def write(request):
    return render(request, 'write.html')

def evallist(request, lect_id):
    lect = get_object_or_404(Lecture, pk = lect_id)
    return render(request, 'evallist.html', {'lect' : lect})




