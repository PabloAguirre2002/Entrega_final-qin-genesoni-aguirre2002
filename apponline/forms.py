from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apponline.models import Avatar 

class CarterasFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.CharField(max_length=50)
    stock = forms.IntegerField()

class CamperasFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.CharField(max_length=50)
    stock = forms.IntegerField()

class ZapatosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.CharField(max_length=50)
    stock = forms.IntegerField()

class AccesoriosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    codigo = forms.CharField(max_length=50)
    stock = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']


class AvatarFormulario(forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']




