from django.db           import  models
from django.conf         import  settings


class Projects( models.Model ):
    '''Project database table model'''

    class Meta:
        verbose_name        = 'My-Project'
        verbose_name_plural = 'My-Projects'

    # Each user can have 9 projects max        
    POSITION_CHOICES = [ (str(x),f'Position - {x}') for x in range(1,10) ]

    creator         = models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE )
    title           = models.CharField( max_length=100 ,help_text='Title of the project')
    position        = models.CharField( max_length=1,
                                        choices=POSITION_CHOICES,
                                        verbose_name='Project position',
                                        help_text='Project position in Home page i.e. (1-9)' )

    description     = models.CharField( max_length=700 ,help_text='Description of that project')
    
    # Tools used for creating the project
    tools           = models.CharField( max_length=700 ,
                                        help_text='Tools used for creating this project (Separate tool by comma and not more than 5 tools)',
                                        null=True, blank=True )

    # images
    isometric_image       = models.ImageField( upload_to='images/', help_text='Upload isometric view of the model.')
    isometric_image_title = models.CharField( max_length=50, help_text='(OPTIONAL) Title of projects images', null=True, blank=True )

    front_image        = models.ImageField( upload_to='images/', help_text='Upload front view of the model.')
    front_image_title  = models.CharField( max_length=50, help_text='(OPTIONAL) Title of projects images', null=True, blank=True )

    side_image         = models.ImageField( upload_to='images/', help_text='(OPTIONAL) Upload side view of the model.',null=True, blank=True )
    side_image_title   = models.CharField( max_length=50, help_text='(OPTIONAL) Title of projects images', null=True, blank=True )

    def save( self, *args, **kwargs ):

        # Default position for new project
        if not self.id:
            self.position = '1'
        super().save( *args, **kwargs )


    def __str__( self ):
        return self.position + ' - ' + ( self.title ).capitalize()




