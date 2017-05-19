from django.contrib import admin

from .models import Project

admin.site.register(Project)
admin.site.site_header = 'Repository Admin'
admin.site.site_title = 'Repository Admin'
admin.site.index = 'Repository Tool'
