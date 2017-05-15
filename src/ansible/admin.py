from django.contrib import admin

from .models import Project, Registry

admin.site.register(Project)
admin.site.register(Registry)
