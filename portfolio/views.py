from django.views.generic import ListView, DetailView
from .models import Project


class ProjectList(ListView):
    template_name = 'portfolio/project_list.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetail(DetailView):
    template_name = 'portfolio/project_detail.html'
    model = Project
    context_object_name = 'project'
