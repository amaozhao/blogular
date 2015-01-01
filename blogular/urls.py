from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views import Home

urlpatterns = patterns(
    '',
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/', Home.as_view()),
    url(r'^user/', Home.as_view()),
    url(r'^tag/', Home.as_view()),
    url(r'^signin/', Home.as_view()),
)
