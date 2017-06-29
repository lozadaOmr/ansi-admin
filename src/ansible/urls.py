from django.conf.urls import url
from ansible.forms import AnsibleForm1, AnsibleForm2
from ansible.views import (
    PlaybookWizard, PlaybookListView, PlaybookDetailView,
)
from . import views


urlpatterns = [
    url(r'^create/$', PlaybookWizard.as_view([AnsibleForm1, AnsibleForm2])),
    url(r'^$', PlaybookListView.as_view(), name='playbook-list'),
    url(r'^(?P<pk>[-\w]+)/$', PlaybookDetailView.as_view(), name='playbook-detail'),
]
