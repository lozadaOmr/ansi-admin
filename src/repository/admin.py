from django.contrib import admin

from .models import Github, Gitlab

admin.site.register(Github)
admin.site.register(Gitlab)
