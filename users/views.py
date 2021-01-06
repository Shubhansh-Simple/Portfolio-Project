from django.views.generic import DetailView
from projects.models      import Projects
from .models              import CustomUser
from django.conf          import settings

class ProfileView( DetailView ):
    model               = CustomUser
    template_name       = 'profile_template.html'
    context_object_name = 'unique_user'


    def get_object( self,queryset=None ):
        '''Extract user from database from url username.'''

        user_name = self.kwargs['username'].lower()
        return CustomUser.objects.get( username=user_name )


    def get_context_data( self,**kwargs ):
        '''How many projects done by this user.'''

        context                   = super( ProfileView,self ).get_context_data( **kwargs )
        context['total_projects'] = Projects.objects.all().count()
        return context


