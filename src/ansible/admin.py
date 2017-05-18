from django.contrib import admin

from .models import Playbook, Registry, Repository

admin.site.register(Playbook)
admin.site.register(Registry)
admin.site.register(Repository)
admin.site.site_header = 'Ansible Admin'
