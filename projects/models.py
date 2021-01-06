from django.db   import  models
from django.contrib.auth  import get_user_model
from django.conf import  settings


class Projects( models.Model ):

    creator         = models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    title           = models.CharField( max_length=100 ,help_text='Title of the projects')
    description     = models.CharField( max_length=500 ,help_text='Description of that projects')
    isometric_image = models.ImageField( upload_to='images/', help_text='Upload isometric view of the model.')
    front_image     = models.ImageField( upload_to='images/', help_text='Upload front view of the model.')
    side_image      = models.ImageField( upload_to='images/', help_text='Upload side view of the model.')
    top_image       = models.ImageField( upload_to='images/', help_text='Upload top view of the model.(OPTIONAL)', null=True,blank=True )
    bottom_image    = models.ImageField( upload_to='images/', help_text='Upload bottom view of the model.(OPTIONAL)', null=True,blank=True )
    project_file    = models.FileField( upload_to ='project_file/', help_text='Upload Your Project file.')


    def total_projects( self ):
        return Projects.objects.all().count()
        
    def __str__( self ):
        return str( self.title ).capitalize()





