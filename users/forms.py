from django import forms
from .models import CustomUser

class CustomUserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('__all__')



class UserEditForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False)
    profile_photo = forms.ImageField(required=False, widget=forms.ClearableFileInput())

    class Meta:
        model = CustomUser
        exclude = ['password']
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'profile_photo', 'title', 'address', 'username', 'password']