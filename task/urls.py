from django.conf.urls import url
from django.views.generic import UpdateView
from requests import request
from django.contrib.auth import views as auth_views


from .models import Athlete
#from .views.cbv.UpdateView import Task_update_time
from . import views
app_name = 'task'
'''
urlpatterns= [
    url(r'^$', views.index, name='index'),

    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]'''
urlpatterns = [
    url(r'index$', views.IndexView.as_view(), name='index'),
    url(r'test$', views.Testview, name='test'),
    url(r'monitor$', views.get_monitoring, name='monitor'),
    url(r'addnew$', views.add, name='addnew'),
    url(r'delete', views.delete_item, name='delete'),
    url(r'^update/(?P<pk>\d+)$', views.server_update, name='athlete_edit'),
    url(r'boot$', views.boot1, name='boot'),
    url(r'test$', views.test, name='test'),
    url(r'main$', views.main, name='main'),
    url(r'show$', views.show, name='show'),
    url(r'jquery$', views.jquery, name='jquery'),
    url(r'bootstarp$', views.bootstrap, name='bootstarp'),
    url(r'redis$', views.is_redis, name='redis'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'$', views.home, name='home'),

]