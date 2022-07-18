from . import views
from django.urls import include, path

app_name='fboard'
urlpatterns = [
    path('fList/',views.fList,name='fList'),
    path('<str:f_no>/fView/',views.fView,name='fView'),
    path('fWrite/',views.fWrite,name='fWrite'),
    path('<str:f_no>/fDelete/',views.fDelete,name='fDelete'),
    path('<str:f_no>/fUpdate/',views.fUpdate,name='fUpdate'),
    path('<str:f_no>/fReply/',views.fReply,name='fReply'),

]
