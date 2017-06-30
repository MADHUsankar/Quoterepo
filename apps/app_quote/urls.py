from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^homepage$', views.homepage , name ='homepage'),
    url(r'^delquote/(?P<id>\d+)$', views.delquote , name ='delquote') ,
    url(r'^editquote/(?P<id>\d+)$', views.editquote , name ='editquote') ,
    url(r'^addfavquote/(?P<id>\d+)$', views.addfavquote , name ='addfavquote') ,
    url(r'^removefavquote/(?P<id>\d+)$', views.removefavquote , name ='removefavquote') ,
    url(r'^showuser/(?P<id>\d+)$', views.showuser , name ='showuser') ,
    url(r'^addquote$', views.addquote , name ='addquote')
    ]
     