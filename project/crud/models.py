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

class Eval(models.Model):
    ratio_choice = (
        ('학점느님', '학점느님'), ('골고루', '골고루'), ('깐깐징어', '깐깐징어'),
        ('F 박격포', 'F 박격포'),
    )

    ratio_select = models.CharField(max_length = 10, choices = ratio_choice)
    pub_date = models.DateTimeField('date published')
    texts = models.TextField()


