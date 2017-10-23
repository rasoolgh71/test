from django.conf.urls import url
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
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'athlete$', views.add, name='create_athlete'),
    url(r'boot$', views.boot1, name='boot'),
    url(r'test$', views.test, name='test'),
    url(r'main$', views.main, name='main'),
    url(r'show$', views.show, name='show'),
url(r'index$', views.index, name='index'),

    url(r'$', views.home, name='home'),

    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]