from django import forms
from .models import CustomUser

def user_exists(username):
    user=CustomUser.objects.filter(username=username)
    if user:
        raise forms.ValidationError('Bu username mavjud')
    else:
        return username



class CustomUserRegisterForm(forms.ModelForm):
    password1=forms.CharField(label='password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    class Meta:
        model= CustomUser
        fields=['username','first_name','last_name','email','image','address']

    def clean(self):
        data = super().clean()
        if data.get('password1')!=data.get('password2'):
            raise forms.ValidationError('Parollar mos emas')
        return data

    def clean_username(self):
        username=self.cleaned_data['username']
        user_exists(username)


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model= CustomUser
        fields=['username','first_name','last_name','email','image','address']
