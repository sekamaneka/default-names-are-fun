from django.conf.urls import patterns, include, url
from django.contrib import admin
from supermarkets.models import Supermarket  
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sexy_hunter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'supermarkets.views.supermarket_list', name='home'),
    url(r'^supermarkets/(?P<anyname>.*)/$', 'supermarkets.views.current_supermarket'),
    url(r'^add_supermarket/$', 'supermarkets.views.add_supermarket_page',
    name='add_supermarket'),
    url(r'^secret/$',
    'supermarkets.views.secret_add_stuff_from_script_to_database'),
    # views for POST requests
    
    url(r'^add_new_supermarket/$', 'supermarkets.views.add_supermarket', name='add_page'),
    url(r'^add_item/$', 'supermarkets.views.add_item', name='add_item'),

)
