from django.contrib import admin

from .models import Playbook, Registry

admin.site.register(Playbook)
admin.site.register(Registry)
