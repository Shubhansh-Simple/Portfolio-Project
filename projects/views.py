from django.shortcuts     import get_list_or_404,get_object_or_404
from django.http          import Http404
from django.contrib.auth  import get_user_model
from django.views.generic import ListView , DetailView
from .models              import Projects       


class ProjectListView( ListView ):
    '''List based on url's username '''

    model               = Projects
    template_name       = 'project_list.html'
    context_object_name = 'project_lists'

    def get_queryset(self):

        requested_user  = self.kwargs['username'].lower()
        obj             = get_object_or_404( get_user_model(),username=requested_user )
        self.USER_EMAIL = obj.email

        if obj:
            return get_list_or_404( Projects,creator=obj.id )
        raise Http404('User not exist')

    def get_context_data( self,**kwargs ):
        context               = super( ProjectListView,self ).get_context_data( **kwargs )
        context['user_url']   = self.kwargs['username'].lower()
        context['user_email'] = self.USER_EMAIL
        return context


class ProjectDetailView( DetailView ):
    model               = Projects
    template_name       = 'project_detail.html'
    context_object_name = 'project_detail'
    
    def get_object( self,queryset=None ):

        requested_user = self.kwargs['username']
        obj             = get_object_or_404( get_user_model(),username=requested_user )
        project_id  = self.kwargs['pk']

        if requested_user and project_id:
            return get_object_or_404( Projects,creator=obj.id,id=project_id )
        raise Http404('Project not found')


    def get_context_data( self,**kwargs ):
        context               = super( ProjectDetailView,self ).get_context_data( **kwargs )
        context['user_url']   = self.kwargs['username'].lower()
        return context








