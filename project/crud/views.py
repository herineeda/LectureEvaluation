from django.shortcuts import render
from .models import Lecture
# Create your views here.

def lecturelist(request):
    lectures = Lecture.objects
    return render(request, 'lecturelist.html', {'lectures' : lectures})

def write(request):
    return render(request, 'write.html')
