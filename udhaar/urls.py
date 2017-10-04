from django.conf.urls import url
from django.contrib import admin


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^group/(?P<groupid>[0-9]+)/$',views.info,name='info'),
    url(r'^newgroup/',views.creategroup,name='newgroup'),
    url(r'^admin/', admin.site.urls),
]
