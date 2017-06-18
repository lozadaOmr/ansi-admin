from django.conf.urls import url

from . import views
from ansible.forms import AnsibleForm1, AnsibleForm2
from ansible.views import PlaybookWizard


named_forms = (
    ('1', AnsibleForm1),
    ('2', AnsibleForm2),
)
playbook_wizard = PlaybookWizard.as_view(
    named_forms,
    url_name='createstep',
)
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/(?P<step>.+)/$', playbook_wizard, name='createstep')
]
