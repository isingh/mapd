from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mapd.views.home', name='home'),
    # url(r'^mapd/', include('mapd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^auth', 'mapd.handlers.AuthHandler'),
    (r'^view', 'mapd.handlers.ViewHandler'),
    (r'^user', 'mapd.handlers.UserRequestHandler'),
    (r'.*', 'mapd.handlers.DefaultHandler'),
)
