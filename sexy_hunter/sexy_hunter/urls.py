from django.conf.urls import patterns, url
urlpatterns = patterns('supermarkets.views',
    url(r'^$', 'supermarket_list', name='home'),
    url(r'^supermarkets/(?P<anyname>.*)/$', 'current_supermarket'),
    url(r'^add_supermarket/$', 'add_supermarket_page', name='add_supermarket'),
    url(r'^secret/(?P<anyname>.*)/$', 'add_items_from_scripts', name='secret'),
    # views for POST requests
    url(r'^add_new_supermarket/$', 'add_supermarket', name='add_page'),
    url(r'^add_item/$', 'add_item', name='add_item'),
    url(r'^about/$', 'about', name='about'),
)
