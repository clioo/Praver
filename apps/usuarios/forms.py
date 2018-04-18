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
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if not user:
            raise forms.ValidationError("El usuario no existe")
        if not user.check_password(password):
            raise forms.ValidationError("El usuario o la contraseña son incorrectos")
        return super(LoginForm,self).clean(*args,**kwargs)

class RegistrarForm(forms.ModelForm):
    username=forms.CharField(label="Nombre de usuario", widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    email = forms.EmailField(label="Correo",widget=forms.TextInput(attrs={'class':'form-control col-md-6'}))
    email2=forms.EmailField(label="Confirmar electrónico",widget=forms.TextInput(attrs={'class':'form-control col-md-6'}))
    password=forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    password2=forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    class Meta:
        model = User
        fields = [
        'username',
        'email',
        'email2',
        'password',
        'password2'
        ]
   
    def clean(self,*args,**kwargs):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if password != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        if email != email2:
            raise forms.ValidationError("Los correos no coinciden")
            if User.objects.get(email=email):
                raise forms.ValidationError("Ya existe ese correo electrónico")
            pass
        return super(RegistrarForm,self).clean(*args,**kwargs)

class RegistrarAgenteForm(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    apellidoPaterno = forms.CharField(label="Apellido paterno", widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    apellidoMaterno = forms.CharField(label="Apellido materno", widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    sexo = forms.ChoiceField(widget=forms.RadioSelect(),choices=(('M', 'Masculino'),('F', 'Femenino')))
    telefono = forms.CharField(label="Número de teléfono", widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    telefono2 = forms.CharField(label="Número de teléfono 2 (Opcional)", widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    class Meta:
        model = Profile
        fields = [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'sexo',
            'telefono',
            'telefono2'
        ]
        exclude = [
            'tipo',
            'user'
        ]
    def clean(self,*args,**kwargs):
        
        return super(RegistrarAgenteForm,self).clean(*args,**kwargs)

