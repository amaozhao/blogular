from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogular.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
