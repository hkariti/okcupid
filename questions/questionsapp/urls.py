from django.conf.urls import patterns, url

from questionsapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="index")
)
