from django.urls import path
from . import views # 같은 폴더에 있는 views.py 가져오기


urlpatterns = [
   path('lecture', views.showLecture, name='showLecture'), # 모든 강의를 보여주는 페이지 경로
   path('lecture/major', views.filteringM, name='filteringM'), # 전공 강의만 보여줌
   path('leture/liberalArts', views.filteringL, name='filteringL'), # 교양 강의만 보여줌
   path('result', views.searchResult, name='searchResult'),
# 검색 결과를 보여주는 페이지 경로
]