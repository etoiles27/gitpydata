from . import views
from django.urls import path, include

app_name='member'
urlpatterns = [
    path('mlist/', views.mlist, name='mlist'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
