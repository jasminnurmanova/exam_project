from django import forms
from .models import CustomUser

class CustomUserRegisterForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields=['username','first_name','last_name','email','image','address','password']