from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #url(r'^task/<int:taskId>/$', views.is_done, name='is_done'),
    url(r'^task/(?P<pk>[0-9]+)/$', views.is_done, name='is_done'),
]