from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from .models import CustomUser

class CustomUserCreationForm( UserCreationForm ):
    '''Adding field in create form of user'''

    class Meta( UserCreationForm.Meta ):
        model  = CustomUser
        fields = UserCreationForm.Meta.fields + ('education','profile_pic',)


class CustomUserChangeForm( UserChangeForm ):
    '''Overriding the update form of User'''

    class Meta:
        model  = CustomUser
        fields = UserChangeForm.Meta.fields









