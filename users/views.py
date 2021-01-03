from django.views.generic import DetailView
from projects.models      import Projects
from .models              import CustomUser
from django.conf          import settings

class ProfileView( DetailView ):
    model               = CustomUser
    queryset            = CustomUser.objects.get( id=2 )
    template_name       = 'profile_template.html'
    context_object_name = 'unique_user'


    def get_object( self ):
        '''For multiple user we modify this method.'''

        return CustomUser.objects.get( id=2 )


    def get_context_data( self,**kwargs ):
        context                   = super( ProfileView,self ).get_context_data( **kwargs )
        context['total_projects'] = Projects.objects.all().count()
        return context


