from django.conf.urls import url
from ansible.forms import AnsibleForm1, AnsibleForm2
from ansible.views import PlaybookWizard, PlaybookListView, PlaybookDetailView

urlpatterns = [
    url(r'^$', PlaybookListView.as_view(), name='playbook-list'),
    url(r'^(?P<pk>[-\w]+)/$', PlaybookDetailView.as_view(), name='playbook-detail'),
    url(r'^create/$', PlaybookWizard.as_view([AnsibleForm1, AnsibleForm2]))
]
