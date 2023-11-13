from django.views.generic import DetailView
from projects.models      import Projects
from .models              import CustomUser

##-------------------FOR Me
class MineProfileView( DetailView ):
    '''Profile Page for me specially'''

    model               = CustomUser
    template_name       = 'profile_template.html'
    context_object_name = 'unique_user'
    special_user        = 'shubhanshu'
   
    
    def get_object( self,queryset=None ):
        '''Extract user from database from url username.'''

        user_name    = self.special_user

        # class variable
        print("Error is there\n\n")
        # class variable
        self.CREATOR = CustomUser.objects.get( username=user_name )  
        return self.CREATOR


    def get_context_data( self,**kwargs ):
        '''How many projects done by this user.'''

        context                   = super( MineProfileView,self ).get_context_data( **kwargs )
        context['user_url']       = ''
        return context


##-------------------FOR OTHER USERS

class ProfileView( DetailView ):
    '''Profile Page of the user based on url.'''

    model               = CustomUser
    template_name       = 'profile_template.html'
    context_object_name = 'unique_user'
   
    
    def get_object( self,queryset=None ):
        '''Extract user from database from url username.'''

        user_name    = self.kwargs['username']

        # class variable
        print("Error is here\n\n")
        self.CREATOR = CustomUser.objects.get( username=user_name )  
        return self.CREATOR


    def get_context_data( self,**kwargs ):
        '''How many projects done by this user.'''

        context                   = super( ProfileView,self ).get_context_data( **kwargs )
        context['user_url']       = self.kwargs['username']
        return context


