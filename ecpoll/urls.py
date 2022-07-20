from django.conf.urls import url
from main import views 

urlpatterns = [
    #url(r'^$', views.home, name='home'),
    url(r'^$', views.index, name='index'),
   ] 