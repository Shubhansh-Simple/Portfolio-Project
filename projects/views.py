from django.shortcuts     import get_object_or_404,render
from django.http          import Http404
from django.contrib.auth  import get_user_model
from django.views.generic import ListView , DetailView
from .models              import Projects

##-------------------FOR Me

class MineProjectListView( ListView ):
    '''Project List for special url i.e. for portfolio owner'''

    model               = Projects
    template_name       = 'project_list.html'
    context_object_name = 'project_lists'
    special_user        = 'shubhanshu'

    def get_queryset(self):
        '''Getting the my details from model'''

        requested_user  = self.special_user
        obj             = get_object_or_404( get_user_model(),username=requested_user )

        # class variable
        self.USER_EDUCATION = obj.education
        self.USER_EMAIL     = obj.email
        
        if obj:
            ProjectList = Projects.objects.filter( creator=obj.id ).order_by('position')

            # Preparing the tools of each project
            for eachProject in ProjectList:
                if eachProject.tools:
                    eachProject.tools = eachProject.tools.split(', ')
            return ProjectList
        raise Http404('User not exist')

    def get_context_data( self,**kwargs ):
        '''Sending current username as empty to template.'''

        context                   = super( MineProjectListView,self ).get_context_data( **kwargs )

        # For checking the site-owner or normal user
        context['user_url']       = ''

        context['owner_name']     = 'Shubhanshu'
        context['user_email']     = self.USER_EMAIL
        context['user_education'] = self.USER_EDUCATION
        return context


class MineProjectDetailView( DetailView ):
    '''Project Details for special url i.e. for portfolio owner'''

    model               = Projects
    template_name       = 'project_detail.html'
    context_object_name = 'project_detail'
    special_user        = 'shubhanshu'

    def get_object( self,queryset=None ):

        requested_user  = self.special_user
        obj             = get_object_or_404( get_user_model(),username=requested_user )
        project_id      = self.kwargs['pk']

        if requested_user and project_id:
            obj_project      = get_object_or_404( Projects,creator=obj.id,id=project_id )

            # Description data splitted by comma
            self.DESCRIPTION = obj_project.description.split('. ')
            return obj_project

        raise Http404('Project not found')


    def get_context_data( self,**kwargs ):
        '''Sending current username as empty to template.'''

        context               = super( MineProjectDetailView,self ).get_context_data( **kwargs )
        context['user_url']   = ''
        context['owner_name'] = 'Shubhanshu'
        context['description_split'] = self.DESCRIPTION
        return context


##-------------------FOR OTHER USERS

class ProjectListView( ListView ):
    '''Project List based on url's username'''

    model               = Projects
    template_name       = 'project_list.html'
    context_object_name = 'project_lists'

    def get_queryset(self):
        '''Getting the user from model after recieving it from url'''

        requested_user  = self.kwargs['username']
        obj             = get_object_or_404( get_user_model(),username=requested_user )

        # class variable
        self.USER_EMAIL     = obj.email
        self.USER_EDUCATION = obj.education

        if obj:
            return Projects.objects.filter( creator=obj.id ).order_by('position')
        raise Http404('User not exist')

    def get_context_data( self,**kwargs ):
        '''Sending current username from url to template.'''

        context                   = super( ProjectListView,self ).get_context_data( **kwargs )
        context['user_url']       = self.kwargs['username']
        context['user_email']     = self.USER_EMAIL
        context['user_education'] = self.USER_EDUCATION
        return context


class ProjectDetailView( DetailView ):
    '''Detail of projects based on id and username both from url.'''

    model               = Projects
    template_name       = 'project_detail.html'
    context_object_name = 'project_detail'

    def get_object( self,queryset=None ):

        requested_user = self.kwargs['username']
        obj            = get_object_or_404( get_user_model(),username=requested_user )
        project_id     = self.kwargs['pk']

        if requested_user and project_id:
            obj_project      =  get_object_or_404( Projects,creator=obj.id,id=project_id )
            self.DESCRIPTION = obj_project.description.split('.')
            return obj_project

        raise Http404('Project not found')


    def get_context_data( self,**kwargs ):
        '''Sending current username from url to template.'''

        context               = super( ProjectDetailView,self ).get_context_data( **kwargs )
        context['user_url']   = self.kwargs['username']
        context['description_split'] = self.DESCRIPTION
        return context


# Custom error view
def error_404_view( request,exception ):
    return render( request, '404.html' )

def error_500_view( request ):
    return render( request, '500.html')


# AMUL BILLING (3/3)
# Html file exist in template folder of this folder
def amul_view( request ):
    return render( request, 'amul.html' )


# Icecream bill maker (3/3)
# Html file exist in template folder of this folder
def icecream_bill_maker_view( request ):
    return render( request, 'icecreamBillMaker.html' )



# Icecream orderer (3/3)
# Html file exist in template folder of this folder
def icecream_orderer_view( request ):
    return render( request, 'icecreamOrderer.html' )










