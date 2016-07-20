from django.conf.urls import url
from introduction import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^intro/$', views.intro, name='intro'),
]