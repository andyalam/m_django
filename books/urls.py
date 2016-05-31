from django.conf import settings
from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^search/$', views.search),
    url(r'^meta/$', views.display_meta),
    url(r'^contact/$', views.contact),
]
