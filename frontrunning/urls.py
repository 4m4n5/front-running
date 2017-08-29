from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_trade/$', views.add_trade, name='add_trade'),
]