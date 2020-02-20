
from django.contrib import admin
from django.urls import path, include 
import crud.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', crud.views.lecturelist, name = "lecturelist"),
    path('lecture/', include('crud.urls')),
]
