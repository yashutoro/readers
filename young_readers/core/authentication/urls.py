from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'core.authentication.views.home'),
    url(r'^login/$', 'core.authentication.views.userLogin'),
    url(r'^register/$', 'core.authentication.views.userRegister'),
    url(r'^logout/$', 'core.authentication.views.userLogout'),
)
