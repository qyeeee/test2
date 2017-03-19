from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^contact/$', views.contactform, name='contact'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^', views.base, name='base'),


]
