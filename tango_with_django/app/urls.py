from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<slug>[\w\-]+)/$', views.show_category, name='show_category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
    url(r'^about/$', views.about, name='about'),
]
