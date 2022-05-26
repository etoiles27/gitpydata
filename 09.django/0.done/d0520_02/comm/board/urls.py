from . import views
from django.urls import include, path

app_name='board'
urlpatterns = [
    path('fList/',views.fList,name='fList'),
    path('fWrite/',views.fWrite,name='fWrite'),
]
