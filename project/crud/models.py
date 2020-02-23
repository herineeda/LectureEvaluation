from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# 강의 정보
class Lecture(models.Model):
    lectureName = models.CharField(max_length=200)
    professor = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    separation = models.CharField(max_length=10)

    def __str__(self):
        return self.lectureName

class Evals(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    lect = models.ForeignKey(Lecture, on_delete = models.CASCADE)
    title = models.CharField(max_length = 20)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()


    def summary(self):
        return self.body[:50]



    
