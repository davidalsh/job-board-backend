from django.contrib import admin

from jobs.models import Job, Category

admin.site.register(Job)
admin.site.register(Category)
