from . import views
from django.urls import include, path

app_name='fboard'
urlpatterns = [

    path('<int:nowpage>/<str:category>/<str:searchword>/fList/',views.fList,name='fList'),
    path('<int:nowpage>/fWrite/',views.fWrite,name='fWrite'),
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fView/',views.fView,name='fView'),
    path('<int:nowpage>/<str:f_no>/fReply/',views.fReply,name='fReply'),
    path('<int:nowpage>/<str:f_no>/fDelete/',views.fDelete,name='fDelete'),
    path('<int:nowpage>/<str:f_no>/fUpdate/',views.fUpdate,name='fUpdate'),

]
