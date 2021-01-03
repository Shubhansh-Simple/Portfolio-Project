from django.contrib             import admin
from django.contrib.auth.admin  import UserAdmin

from .forms                     import CustomUserChangeForm , CustomUserCreationForm
from .models                    import CustomUser

class CustomUserAdmin( UserAdmin ):
    add_form      = CustomUserCreationForm
    form          = CustomUserChangeForm
    model         = CustomUser

    def get_queryset( self,request ):
      '''Staff user can see his own data only'''

      query = super( CustomUserAdmin,self ).get_queryset( request )
        
      if not request.user.is_superuser:
          self.list_display = ( '__str__','email', )
          return query.filter( id=request.user.id )   
      return query 

    
    def get_fieldsets( self,request,obj=None ):
        '''Show specific field to the Non superuser.'''

        if not obj:
            return self.add_fieldsets

        if not request.user.is_superuser:
            '''I want to show only this fields.'''

            return ( 'Personal Info' , { 'fields' : ( 'first_name','last_name','email','age','profile_pic','about_me' )}),

        else:
            super().get_fieldsets( request,obj )



#UserAdmin.fieldsets += ('Custom Field',{'fields' : ( 'age','education','about_me','profile_pic')}),
#print( UserAdmin.fieldsets )


admin.site.register( CustomUser,CustomUserAdmin )
