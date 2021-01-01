from django.shortcuts import render
from projects.models import ProjectModel

# Create your views here.


def project_index(request):
    projects = ProjectModel.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = ProjectModel.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project':project})