from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser( AbstractUser ):
    class Meta:
        db_table            = 'users_customuser'
        verbose_name        = 'Account'
        verbose_name_plural = 'Accounts'

    profile_pic = models.ImageField( upload_to='profile_pic/', null=True, blank=True, help_text='Upload your profile picture' )
    education   = models.CharField( max_length=50,null=True,blank=True )
    age         = models.PositiveSmallIntegerField( null=True,blank=True )
    birth_date  = models.DateField( null=True,blank=True )
    about_me    = models.CharField( max_length=300,null=True,blank=True )


    def __str__( self ):
        return str( self.username ).capitalize()


