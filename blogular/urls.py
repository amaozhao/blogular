from django.conf.urls import patterns, include, url
from django.contrib import admin

from blog.views import Home

urlpatterns = patterns(
    '',
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
#     url(r'^accounts/', include('allauth.urls')),
    url(r'^posts', Home.as_view()),
    url(r'^post', Home.as_view()),
    url(r'^users', Home.as_view()),
    url(r'^tags', Home.as_view()),
    url(r'^find', Home.as_view()),
    url(r'^following', Home.as_view()),
    url(r'^followed', Home.as_view()),
    url(r'^signin', Home.as_view()),
)
