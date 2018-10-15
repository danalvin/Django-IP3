from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns =[
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', views.loader, name='loader'),
    url(r'^project/(\d+)', views.project, name='project'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^home/', views.index, name='Awards'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^search/', views.search_results, name='search')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)