from django.contrib import admin
from board.models import Freeboard

# 자유게시판
@admin.register(Freeboard)
class FreeboardAdmin(admin.ModelAdmin):
    list_display = ['f_no','f_title','f_createdate']