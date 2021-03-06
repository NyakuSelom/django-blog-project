from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'selomblog.views.home', name='home'),
    #url(r'^selomblog/', include('selomblog.urls')),
    url(r'^blog/',include('blog.urls')),
    url(r'^reg/',include('reg.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root' : settings.STATIC_ROOT,}),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
