from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sexy_hunter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'supermarkets.views.supermarket_list', name='home'),
    url(r'^add_page/$', 'supermarkets.views.add_supermarket', name='add_page'),    
)
