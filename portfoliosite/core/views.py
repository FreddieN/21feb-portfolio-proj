from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
import datetime
from django.views.generic import View

# Create your views here.


def index(request):
    # return HttpResponse(f"Hello, world. You're at my portfolio site. {datetime.datetime.now()}")
    context = {}
    context['projects'] = Project.objects.filter(published=True)
    return render(request, 'projectslisting.html', context)

class project_view(View):
    def get(self, request, project_id):
        context = {}
        context['project'] = Project.objects.get(pk=project_id)
        return render(request, 'project.html', context)
