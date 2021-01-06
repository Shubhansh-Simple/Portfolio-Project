from django.contrib             import admin
from django.contrib.auth.admin  import UserAdmin

from .forms                     import CustomUserChangeForm , CustomUserCreationForm
from .models                    import CustomUser

class CustomUserAdmin( UserAdmin ):
    '''Entire Admin Site Based.'''

    add_form      = CustomUserCreationForm
    form          = CustomUserChangeForm
    model         = CustomUser

    ''' 
    Fields you want to show on creating the new user through admin site.

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email')
			}
        ),
    )
    ''' 
    
    # CLEAN CODE
    NON_SUPER_USER_FIELD = ( 'Personal Info',   { 'fields' : ('first_name','last_name','email',),  }),

    # CustomUserModel Fields
    ADDITIONAL_FIELD     = ( 'Additional Info', {'fields' :  ( 'profile_pic','age','education','about_me', ), }),
    

    def get_queryset( self,request ):
      '''Staff user can see his own data only'''

      query = super( CustomUserAdmin,self ).get_queryset( request )
        
      if not request.user.is_superuser:
          self.list_display = ( '__str__','email', )
          return query.filter( id=request.user.id )   
      return query 



    def get_fieldsets( self,request,obj=None ):
        '''For showing limited field to the non-super-user.'''

        if not obj:
            return self.add_fieldsets

        if not request.user.is_superuser:
            '''Show limited field to non-superuser'''

            return self.NON_SUPER_USER_FIELD + self.ADDITIONAL_FIELD

        else:
            '''Show all fields to superuser with additional one.'''
            return UserAdmin.fieldsets + self.ADDITIONAL_FIELD


admin.site.register( CustomUser,CustomUserAdmin )




















