from django.conf.urls import url
from ecpoll import views 

urlpatterns = [
    #url(r'^$', views.home, name='home'), Don't do this
    url(r'^$', views.index, name='index'),
    url(r'^user_list/$', views.user_list, name='user_list'),
    url(r'^add/$', views.polls_add, name='add'),
   ] 