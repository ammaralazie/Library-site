from django import forms
from django.contrib.auth.models import User
from .models import Profile
class EditProfile(forms.ModelForm):
    
    class Meta:
        model=Profile
        fields=['first_name','last_name','avatar','describtion']
        #widgets={'avatar':forms.(attrs={'class':'profile__image'}),}



