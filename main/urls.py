from django.contrib import admin
from django.conf.urls import url
from main import views 
 
 
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^board/(?P<question_id>\d+)/$', views.question_detail, name='question_detail'),
    url(r'^board/question_create/$', views.question_create, name='question_create'), ## 추가 ##
    url(r'^board/question_modify/(?P<question_id>\d+)/$', views.question_modify, name='question_modify'),
    url(r'^board/question_delete/(?P<question_id>\d+)/$', views.question_delete, name='question_delete'),
    url(r'^vote/question/(?P<question_id>\d+)/$', views.vote_question, name='vote_question'),
    
] 

 