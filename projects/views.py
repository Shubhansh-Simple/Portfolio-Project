from django.shortcuts     import get_object_or_404
from django.http          import Http404
from django.contrib.auth  import get_user_model
from django.views.generic import ListView , DetailView
from .models              import Projects       

##-------------------FOR Me

class MineProjectListView( ListView ):
    '''Project List for me specially'''

    model               = Projects
    template_name       = 'project_list.html'
    context_object_name = 'project_lists'
    special_user        = 'shubhanshu'

    def get_queryset(self):

        requested_user  = self.special_user
        obj             = get_object_or_404( get_user_model(),username=requested_user )
        
        # class variable
        self.USER_EMAIL = obj.email                 

        if obj:
            return Projects.objects.filter( creator=obj.id )
        raise Http404('User not exist')

    def get_context_data( self,**kwargs ):
        '''Sending current username from url to template.'''

        context               = super( MineProjectListView,self ).get_context_data( **kwargs )
        context['user_url']   = ''
        context['user_email'] = self.USER_EMAIL
        return context


class MineProjectDetailView( DetailView ):
    '''Project Detail for me specially'''

    model               = Projects
    template_name       = 'project_detail.html'
    context_object_name = 'project_detail'
    special_user        = 'shubhanshu'
    
    def get_object( self,queryset=None ):

        requested_user   = self.special_user
        obj              = get_object_or_404( get_user_model(),username=requested_user )
        project_id       = self.kwargs['pk']


        if requested_user and project_id:
            obj_project      = get_object_or_404( Projects,creator=obj.id,id=project_id )
            self.DESCRIPTION = obj_project.description.split('. ')
            return obj_project

        raise Http404('Project not found')


    def get_context_data( self,**kwargs ):
        '''Sending current username from url to template.'''

        context                      = super( MineProjectDetailView,self ).get_context_data( **kwargs )
        context['user_url']          = ''
        context['owner_name']        = 'Shubhanshu'
        context['description_split'] = self.DESCRIPTION
        return context


##-------------------FOR OTHER USERS

class ProjectListView( ListView ):
    '''Project List based on url's username '''

    model               = Projects
    template_name       = 'project_list.html'
    context_object_name = 'project_lists'

    def get_queryset(self):

        requested_user  = self.kwargs['username'] 
        obj             = get_object_or_404( get_user_model(),username=requested_user )
        
        # class variable
        self.USER_EMAIL = obj.email                 

        if obj:
            return Projects.objects.filter( creator=obj.id )
        raise Http404('User not exist')

    def get_context_data( self,**kwargs ):
        '''Sending current username from url to template.'''

        context               = super( ProjectListView,self ).get_context_data( **kwargs )
        context['user_url']   = self.kwargs['username']
        context['user_email'] = self.USER_EMAIL
        return context


class ProjectDetailView( DetailView ):
    '''Detail of projects based on id and username both from url.'''

    model               = Projects
    template_name       = 'project_detail.html'
    context_object_name = 'project_detail'
    
    def get_object( self,queryset=None ):

        requested_user  = self.kwargs['username']
        obj             = get_object_or_404( get_user_model(),username=requested_user )
        project_id      = self.kwargs['pk']

        if requested_user and project_id:
            obj_project      =  get_object_or_404( Projects,creator=obj.id,id=project_id )
            self.DESCRIPTION = obj_project.description.split('.')
            return obj_project

        raise Http404('Project not found')


    def get_context_data( self,**kwargs ):
        '''Sending current username from url to template.'''

        context                      = super( ProjectDetailView,self ).get_context_data( **kwargs )
        context['user_url']          = self.kwargs['username']
        context['description_split'] = self.DESCRIPTION
        return context








