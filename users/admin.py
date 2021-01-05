from django.contrib             import admin
from typing import Set
from django.contrib.auth.admin  import UserAdmin

from .forms                     import CustomUserChangeForm , CustomUserCreationForm
from .models                    import CustomUser

class CustomUserAdmin( UserAdmin ):
    add_form      = CustomUserCreationForm
    form          = CustomUserChangeForm
    model         = CustomUser
    
    NON_SUPER_USER_FIELD = ( 'Personal Info',   { 'fields' : ('first_name','last_name','email',),  }),
    ADDITIONAL_FIELD     = ( 'Additional Info', {'fields' :  ( 'profile_pic','age','education','about_me', ), }),
    

    def get_queryset( self,request ):
      '''Staff user can see his own data only'''

      query = super( CustomUserAdmin,self ).get_queryset( request )
        
      if not request.user.is_superuser:
          self.list_display = ( '__str__','email', )
          return query.filter( id=request.user.id )   
      return query 



    def get_fieldsets( self,request,obj=None ):
        '''For showing specific field to the non-super-user.'''

        if not obj:
            return self.add_fieldsets

        if not request.user.is_superuser:

            return self.NON_SUPER_USER_FIELD + self.ADDITIONAL_FIELD

        else:
            return UserAdmin.fieldsets + self.ADDITIONAL_FIELD



admin.site.register( CustomUser,CustomUserAdmin )




















