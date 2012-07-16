from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^reg/login/$','reg.views.do_logout'),
    url(r'^reg/logout/$','reg.views.do_login'),

)
