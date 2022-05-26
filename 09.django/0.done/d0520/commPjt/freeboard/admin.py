from django.contrib import admin
from freeboard.models import Freeboard
# Register your models here.

# admin.site.register(Freeboard)
@admin.register(Freeboard)
class FreeboardAdmin(admin.ModelAdmin):
    list_display = ['f_no','f_title','f_createdate']