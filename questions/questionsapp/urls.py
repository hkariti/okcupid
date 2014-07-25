from django.conf.urls import patterns, url

from questionsapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index"),
    url(r'^success(?:/(?P<user>[0-9]+))?$', views.index, name="success"),
    url(r'^details(?:/(?P<questions>.*))?', views.details, name="details"),
    url(r'^add_user$', views.add_user, name="add_user"),
)
