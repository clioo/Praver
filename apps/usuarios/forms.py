#coding: utf-8
from django import forms
from apps.usuarios.models import Profile
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.models import User
from apps.usuarios.models import Profile
from django.core import validators


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario",widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    def clean(self,*args,**kwargs):
        username = str(self.cleaned_data.get('username')).lower()
        password = self.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        print(username)
        print(password)
        if username == "none" or password == None:
            raise forms.ValidationError("Necesita introducir ambos campos")
        elif not user:
            raise forms.ValidationError("El usuario o la contraseña son incorrectos")
        return super(LoginForm,self).clean(*args,**kwargs)

class RegistrarForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [

        ]
        exclude = [
            'username',
            'email',
            'password',
        ]

class RegistrarAgenteForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            
        ]
        exclude = [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'sexo',
            'telefono',
            'telefono2',
            'tipo',
            'user',
        ]

