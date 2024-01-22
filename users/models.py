from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import ValidationError


def validate_phone( value ):
    '''Check weather phone number is numeric and contain atleast ten characters'''

    if value.isdigit() and len(value) == 10:
        return value
    else:
        raise ValidationError('Mobile number should be numeric and must contain 10 digits')


class CustomUser( AbstractUser ):
    '''Override existing user table created by django'''

    class Meta:
        db_table            = 'users_customuser'
        verbose_name        = 'Account'
        verbose_name_plural = 'Accounts'


    education     = models.CharField( max_length=50,null=True,blank=True )
    birth_date    = models.DateField( null=True,blank=True )
    about_me      = models.CharField( max_length=300,null=True,blank=True )

    profile_pic   = models.ImageField( upload_to='profile_pic/', null=True, blank=True, 
                                       help_text='Upload your profile picture' )

    # new-fields added
    phone         = models.CharField( max_length=10, null=True, blank=True, 
                                      verbose_name='Mobile Number', 
                                      help_text='for eg. 7859499938',
                                      validators=[ validate_phone ] )

    address       = models.CharField( max_length=60, null=True, blank=True )
    github_link   = models.URLField( max_length=100, null=True, blank=True )
    linkedin_link = models.URLField( max_length=100, null=True, blank=True )

    resume_file   = models.FileField( upload_to='project_file/', null=True, blank=True, 
                                      help_text='Upload your updated resume.' )


    def __str__( self ):
        return str( self.username ).capitalize()


