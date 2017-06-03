from django.contrib import admin

from .models import Github, Gitlab, Playbook, Registry

admin.site.register(Playbook)
admin.site.register(Registry)
admin.site.register(Github)
admin.site.register(Gitlab)
admin.site.site_header = 'Ansible Admin'
admin.site.site_title = 'Ansible Admin'
admin.site.index_title = 'Admin Tool'
