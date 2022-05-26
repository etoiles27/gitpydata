from . import views
from django.urls import include, path

app_name='product'
urlpatterns = [
    path('pList/',views.pList,name='pList'),
    path('pWrite/',views.pWrite,name='pWrite'),
    path('pIndex/',views.pIndex,name='pIndex'),
    path('<str:p_no>/pView/',views.pView,name='pView'),
]
