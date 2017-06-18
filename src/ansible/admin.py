from django.contrib import admin

from .models import Playbook

admin.site.register(Playbook)
admin.site.site_header = 'Ansible Admin'
admin.site.site_title = 'Ansible Admin'
admin.site.index_title = 'Admin Tool'
