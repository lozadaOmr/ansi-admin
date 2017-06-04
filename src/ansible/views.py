from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Github, Gitlab, Playbook
from .forms import RepositoryForm

def index(request):
    return HttpResponse("200")

def create(request):
    form = RepositoryForm()
    return render(request, 'ansible/create.html', {'form': form})

