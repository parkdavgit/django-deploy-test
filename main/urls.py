from django.contrib import admin
from django.conf.urls import url
from main import views 
 
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^board/(?P<question_id>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^board/question_create/$', views.question_create, name='question_create'), ## 추가 ##
     
] 

 