from . import views
from django.urls import include, path

app_name='member'
urlpatterns = [
    path('login/',views.login,name='login1'),
    path('logout/',views.logout,name='logout'),
]
