from django.conf.urls import url,include
from . import views


urlpatterns=[
url(r'^$',views.index,name="index"),
url(r'^post/',views.post,name="post"),
url(r'^summary/(?P<id>\d+)/',views.summary,name="summary"),
url(r'^search/$',views.search,name="search"),
url(r'^gpa/$',views.gpa,name="gpa"),
url(r'^search/jobs/summary/(?P<id>\d+)/$',views.summary,name="summary"),
url(r'^gpa/jobs/summary/(?P<id>\d+)/$',views.summary,name="summary"),
url(r'^nogpa/$',views.nogpa,name="nogpa"),
url(r'^nogpa/jobs/summary/(?P<id>\d+)/$',views.summary,name="summary"),
url(r'^contact/$',views.contact,name="contact"),
url(r'^donate/$',views.donate,name="donate"),
url(r'^addemail/$',views.addemail,name="addemail"),
]