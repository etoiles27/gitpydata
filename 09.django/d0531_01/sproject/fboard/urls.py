from django.urls import include,path
from . import views

app_name='fboard'
urlpatterns = [
    # 리스트,검색
    path('<int:nowpage>/<str:category>/<str:searchword>/fList/',views.fList,name='fList'),
    path('<int:nowpage>/<str:category>/<str:searchword>/fWrite/',views.fWrite,name='fWrite'),
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fView',views.fView,name='fView'),
    # 답글쓰기
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fReply',views.fReply,name='fReply'),
    # 삭제
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fDelete',views.fDelete,name='fDelete'),
    # 수정
    path('<int:nowpage>/<str:category>/<str:searchword>/<str:f_no>/fUpdate',views.fUpdate,name='fUpdate'),
    path('event/',views.event,name='event'),
    path('event_view/',views.event_view,name='event_view'),
    path('commList/',views.commList,name='commList'),
    path('commWrite/',views.commWrite,name='commWrite'),
    path('commDelete/',views.commDelete,name='commDelete'),
    path('commUpdateOk/',views.commUpdateOk,name='commUpdateOk'),
    path('<int:nowpage>/<str:category>/<str:searchword>/fList2/',views.fList2,name='fList2'),
    path('chart01/',views.chart01,name='chart01'),
    path('chart_data/',views.chart_data,name='chart_data'),
    
]
