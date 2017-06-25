from django.conf.urls import url

from . import views
from ansible.forms import AnsibleForm1, AnsibleForm2
from ansible.views import PlaybookWizard, Login

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', Login.as_view()),
    url(r'^create/$', PlaybookWizard.as_view([AnsibleForm1, AnsibleForm2]))
]
