from django.conf.urls import url
from . import views

app_name = 'officialSite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about', views.about, name='about'),
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^clientshowcase', views.clientshowcase, name='clientshowcase'),
    url(r'^contacts', views.contacts, name='contacts'),
    url(r'^carousel', views.carousel, name='carousel'),
    url(r'^clients', views.clients, name='clients'),
]