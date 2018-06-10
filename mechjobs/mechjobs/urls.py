from django.contrib import admin
from django.conf.urls import url,include
from jobs.views import contact

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',include('jobs.urls')),
    url(r'^jobs/',include('jobs.urls')),
    url(r'^about/',contact),
    #url(r'^signup/',include('jobs.urls')),
]
