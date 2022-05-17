from . import views
from django.urls import path, include

app_name='students'
urlpatterns = [
    path('stuWrite/',views.stuWrite,name='stuWrite'),
    path('stuList/',views.stuList,name='stuList'),
    path('<str:name>/stuView/',views.stuView,name='stuView'),
    # path('stuWriteOK/',views.stuWriteOK,name='stuWriteOK'),
]
