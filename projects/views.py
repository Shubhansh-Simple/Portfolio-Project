from django.shortcuts     import render
from django.views.generic import ListView , DetailView
from .models              import Projects       

class ProjectListView( ListView ):
    model               = Projects
    template_name       = 'project_list.html'
    context_object_name = 'project_lists'


class ProjectDetailView( DetailView ):
    model               = Projects
    template_name       = 'project_detail.html'
    context_object_name = 'project_detail'







