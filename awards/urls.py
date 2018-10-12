from django.conf.urls import url
from . import views


urlpatterns =[
    url(r'^$', views.loader, name='loader'),
    url(r'^home/', views.index, name='Awards')
]