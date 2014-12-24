from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from poll import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'classified.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.poll),
    url(r'^display/$', views.display),
    url(r'^get_hostname/$', views.get_hostname),
    url(r'^disclosure/$', views.disclosure),
   

)
