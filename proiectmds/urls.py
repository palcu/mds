from django.conf.urls import include, url
from django.contrib import admin

from teme import views
from . import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses', views.courses, name='courses'),
    url(r'^teachers', views.teachers, name='teachers'),
    url(r'^admin/', include(admin.site.urls))
]
