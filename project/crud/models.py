from django.db import models

# Create your models here.

# 강의 정보
class Lecture(models.Model):
    lectureName = models.CharField(max_length=200)
    professor = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    separation = models.CharField(max_length=10)

    def __str__(self):
        return self.lectureName
