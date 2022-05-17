
from . import views
from django.urls import path, include

app_name='students'
urlpatterns = [

    path('register/',views.register, name='register'),

]
