from django.contrib import admin
from .models        import Projects

class CustomProjects( admin.ModelAdmin ):

    def get_queryset( self,request ):
      '''Staff user can see his own created data -->only<--'''

      query = super( CustomProjects,self ).get_queryset( request )
        
      if not request.user.is_superuser:
          #self.list_display = ( '__str__','email', )
          return query.filter( creator=request.user.id )   
      return query 


    def get_form( self,request,obj=None,**kwargs ):
        '''Hide creator-selection field in project model.'''

        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('creator')
        return super( CustomProjects,self ).get_form( request,obj,**kwargs )

    def save_model( self, request, obj, form, change):
        obj.creator = request.user
        super().save_model( request, obj, form, change )



admin.site.register( Projects,CustomProjects )

