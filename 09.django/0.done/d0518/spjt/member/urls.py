from . import views
from django.urls import path, include

app_name='member'
urlpatterns = [
    path('memberList/', views.memberList, name='memberList'),
    path('login/', views.login, name='login'),
    path('list/', views.list, name='list'),
]
