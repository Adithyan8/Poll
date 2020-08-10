from django.urls import include, path
from . import views

appname = 'queans'

urlpatterns = [
    path('',views.Qlist.as_view(),name="qlist"),
    path('<int:pk>/',views.Qdetail.as_view(),name="qdetail"),
    path('create',views.Qcreate.as_view(),name="qcreate"),
    path('<int:pk>/update/',views.Qupdate.as_view(),name="qupdate"),
    path('<int:pk>/delete/',views.Qdelete.as_view(),name="qdelete"),
    path('<int:id>/vote/',views.Qvote,name="qvote"),
]