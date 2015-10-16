"""carrieocoyle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # gallery with optional trailing slash
    url(r'^gallery/?$', 'gallery.views.pieces'),
    # should match one or more of any character following the gallery
    url(r'^gallery/(.+)$', 'gallery.views.piece'),
    # blog
    #url(r'^blog/?$', 'blog.views.blog'),
    # individual blog post
    #url(r'^blog/(.+)$', 'blog.views.post'),
    # contact
    url(r'contact/?$', 'boringpages.views.contact'),
    # about
    url(r'^about/?$', 'boringpages.views.about'),
    # shop
    #url(r'^shop$', 'shop.views.store'),
    # home
    url(r'^/?', 'boringpages.views.home'),
]
if settings.DEBUG:
    urlpatterns += [
    # static files for development only; actual ones will be served by nginx
    url(r'^static/(?P<path>.*)$', views.serve),
    ]
