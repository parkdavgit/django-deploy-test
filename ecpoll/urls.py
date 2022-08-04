from django.conf.urls import url
from ecpoll import views 

urlpatterns = [
    #url(r'^$', views.home, name='home'), Don't do this
    url(r'^$', views.index, name='index'),
    url(r'^user_list/$', views.user_list, name='user_list'),
    url(r'^polls_add/$', views.polls_add, name='polls_add'),
    url(r'^detail/(?P<poll_id>\d+)/$', views.poll_detail, name='detail'),
    url(r'^vote/(?P<poll_id>\d+)/$', views.poll_vote, name='vote'),
    url(r'^end_poll/(?P<poll_id>\d+)/$', views.endpoll, name='end_poll'),
   ] 

     