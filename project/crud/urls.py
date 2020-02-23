from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('lecturelist/', views.lecturelist, name = "lecturelist"),
    path('<int:lect_id>/', views.evallist, name = "evallist"),
    path('<int:lect_id>/write', views.write, name = "write"),
    path('create', views.create, name = "create"),
    path('<int:evals_id>/delete', views.eval_delete, name = "delete"),
    path('<int:evals_id>/edit', views.edit, name = "edit"),

    ]


