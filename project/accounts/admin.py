from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'major', 'undergradNum', 'studentname')
    list_display_links = ('undergradNum', 'studentname')
    exclude = ('password',)                           # 사용자 상세 정보에서 비밀번호 필드를 노출하지 않음