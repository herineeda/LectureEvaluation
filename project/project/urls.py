from django.contrib import admin
from django.urls import path, include 
import crud.views
import search.views # 검색 기능

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search.views.home, name='home'), # 첫 화면
    path('lecture/', include('crud.urls')),
    path('search/', include('search.urls')), # search 앱에 있는 urls.py에 url 설계
    path('accounts/', include('accounts.urls')),
    path('write/<int:evals_id>', crud.views.evaldetail, name = "evaldetail"),
]