from . import views
from django.urls import path, include

app_name="students"
urlpatterns = [
    path('stuList/', views.stuList, name='stuList'),
    path('stuWrite/', views.stuWrite, name='stuWrite'),
    path('stuWriteOk/', views.stuWriteOk, name='stuWriteOk'),
    path('<str:s_no>/stuView/', views.stuView, name='stuView'),
    path('<str:s_no>/stuUpdate/', views.stuUpdate, name='stuUpdate'),
    path('stuUpdateOk/', views.stuUpdateOk, name='stuUpdateOk'),
    path('<str:s_no>/stuDelete/', views.stuDelete, name='stuDelete'),

]
