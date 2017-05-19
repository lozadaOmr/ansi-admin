from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Project

def index(request):
    return HttpResponse("200")
