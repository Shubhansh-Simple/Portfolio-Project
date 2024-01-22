from django.contrib import admin
from .models        import Projects


class ProjectsAdmin( admin.ModelAdmin ):
    '''Override Admin site form for Project model'''

    #form = ProjectsForm
    ordering = ('position','id',)

    def get_queryset( self,request ):
      '''Staff user can see his own created data -->only<--'''

      query = super( ProjectsAdmin,self ).get_queryset( request )
        
      if not request.user.is_superuser:
          return query.filter( creator=request.user.id )   
      return query 


    def get_form( self, request, obj=None,**kwargs ):
        '''Hide some fields in admin form of project model.'''

        self.exclude = []

        # Fields which doesn not appear in CREATE project form in admin site
        if not obj:
            self.exclude.append('position')

        if not request.user.is_superuser:
            self.exclude.append('creator')

        return super( ProjectsAdmin,self ).get_form( request,obj,**kwargs )


    def save_model( self, request, obj, form, change):
        '''On save creator of project will login user'''

        obj.creator = request.user 
        super().save_model( request, obj, form, change )


admin.site.register( Projects,ProjectsAdmin )

