from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^about/$', views.about, name='about'),
]
