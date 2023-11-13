from django.db   import  models
from django.contrib.auth  import get_user_model
from django.conf import  settings


class Projects( models.Model ):
    class Meta:
        verbose_name        = 'My-Project'
        verbose_name_plural = 'My-Projects'

    creator         = models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE )

    title           = models.CharField( max_length=100 ,help_text='Title of the projects')
    description     = models.CharField( max_length=600 ,help_text='Description of that projects')

    # images
    isometric_image = models.ImageField( upload_to='images/', help_text='Upload isometric view of the model.')
    front_image     = models.ImageField( upload_to='images/', help_text='Upload front view of the model.')
    side_image      = models.ImageField( upload_to='images/', help_text='Upload side view of the model.')
    top_image       = models.ImageField( upload_to='images/', help_text='(OPTIONAL) Upload top view of the model.', null=True,blank=True )
    bottom_image    = models.ImageField( upload_to='images/', help_text='(OPTIONAL) Upload bottom view of the model.', null=True,blank=True )

    # title of projects images in detail page
    isometric_image_title = models.CharField( max_length=50, help_text='(OPTIONAL) Title of projects images', null=True, blank=True )
    front_image_title     = models.CharField( max_length=50, help_text='(OPTIONAL) Title of projects images', null=True, blank=True )    
    side_image_title      = models.CharField( max_length=50, help_text='(OPTIONAL) Title of projects images', null=True, blank=True )     
    top_image_title       = models.CharField( max_length=50, help_text='(OPTIONAL) Title of projects images', null=True, blank=True )      
    bottom_image_title    = models.CharField( max_length=50, help_text='(OPTIONAL) Title of projects images', null=True, blank=True )       

    project_file          = models.FileField( upload_to ='project_file/', help_text='(OPTIONAL) Upload Your Project file.', null=True, blank=True )
    project_file_link     = models.URLField( max_length=100, null=True, blank=True, help_text='(OPTIONAL) For eg. github link' )
        
    def __str__( self ):
        return str( self.title ).capitalize()





