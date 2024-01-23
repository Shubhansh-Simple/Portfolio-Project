from django.views.generic import DetailView
from django.shortcuts     import get_object_or_404
from .models              import CustomUser

##-------------------FOR Me
class MineProfileView( DetailView ):
    '''Profile Page for me'''

    model               = CustomUser
    template_name       = 'profile_template.html'
    context_object_name = 'unique_user'
    special_user        = 'shubhanshu'
   
    
    def get_object( self,queryset=None ):
        '''Extract special_user from the database'''

        user_name    = self.special_user
        self.CREATOR = get_object_or_404(CustomUser, username=user_name)
        return self.CREATOR


    def get_context_data( self,**kwargs ):
        '''Setting user_url for special_user'''

        context                   = super( MineProfileView,self ).get_context_data( **kwargs )
        context['user_url']       = ''
        return context


##-------------------FOR OTHER USERS
class ProfileView( DetailView ):
    '''Profile Page of the user based on url'''

    model               = CustomUser
    template_name       = 'profile_template.html'
    context_object_name = 'unique_user'
   
    
    def get_object( self,queryset=None ):
        '''Extract user from the database'''

        user_name    = self.kwargs['username']
        self.CREATOR = get_object_or_404(CustomUser, username=user_name)
        return self.CREATOR


    def get_context_data( self,**kwargs ):
        '''Setting user_url for an ordinary user'''

        context                   = super( ProfileView,self ).get_context_data( **kwargs )
        context['user_url']       = self.kwargs['username']
        return context


