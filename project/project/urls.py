"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # 앱에 포함된 urls.py에 저장된 url 사용
import search.views # 검색 기능

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', search.views.home, name='home'), # 첫 화면
    path('search/', include('search.urls')), # search 앱에 있는 urls.py에 url 설계
]
