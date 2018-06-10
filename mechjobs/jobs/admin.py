from django.contrib import admin
from .models import Job
from .models import PostedJob
from .	models import Email
# Register your models here.
admin.site.register(Job)
admin.site.register(PostedJob)
admin.site.register(Email)