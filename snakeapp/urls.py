from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'snakeapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'snake.views.home', name='home'),
    url(r'^snake/$', 'snake.views.snake', name='snake'),
    url(r'^admin/', include(admin.site.urls)),
)
