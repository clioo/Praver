from django import forms
from django.contrib.auth import authenticate,get_user_model,login,logout
from django.contrib.auth.models import User
from django.core import validators
from apps.inmueble.models import Inmueble,ImagenesInmbueble

class InmuebleForm(forms.ModelForm):
    '''titulo = forms.CharField(label="Titulo de la propiedad",widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Ejemplo: Bonita casa amplia recién remodelada lista para habitar"}))
    descripcion = forms.CharField(label="Descripción de la propiedad",widget=forms.Textarea(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Características generales y principales atractivos de la propiedad"}))
    tipoInmueble = forms.CharField(label="Tipo de inmueble",widget=forms.Select(attrs={'class':'form-control col-lg-9 col-md-12'},choices=(('casa','Casa'),('depa',"Departamento"),('dupl',"Dúplex"),('ofic',"Oficina"),('loca',"Local comercial"))))
    antiguedad = forms.IntegerField(label="Antigüedad",widget=forms.NumberInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    recamaras = forms.IntegerField(label="Recamaras",widget=forms.NumberInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    estacionamiento = forms.IntegerField(label="Estacionamiento",widget=forms.NumberInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    banos = forms.IntegerField(label="Baños",widget=forms.NumberInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    mediosBanos = forms.IntegerField(label="Medios baños",widget=forms.NumberInput(attrs={'class':'form-control col-lg-9 col-md-12'}))
    tipoVenta = forms.MultipleChoiceField(label="Tipo de venta",widget=forms.CheckboxSelectMultiple,choices=(('vent',"Venta"),('rent',"Renta"),('tras',"Traspaso")))
    precioVenta = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Precio de venta"}))
    precioRenta = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Precio de renta"}))
    precioTraspaso = forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Precio de traspaso"}))
    metrosConstruidos = forms.FloatField(label="Dimensiones",widget=forms.NumberInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Metros construidos"}))
    metrosTotales = forms.FloatField(widget=forms.NumberInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Metros totales"}))
    calle = forms.CharField(label="Domicilio",widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Calle"}))
    numExt = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Número exterior"}))
    numInt = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Número interior(opcional)"}))
    codigoPostal = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control col-lg-9 col-md-12','placeholder':"Código postal"}))
    servicios = forms.MultipleChoiceField(label="Servicios del inmueble",widget=forms.CheckboxSelectMultiple,choices=(('gas',"Gas"),('aire',"Aire acondicionado"),('segu',"Seguridad privada"),('cale',"Calefacción"),('amu',"Amueblada")))
    estadoConservacion =forms.CharField(label="Estado de conservación",widget=forms.Select(attrs={'class':'form-control col-lg-9 col-md-12'},choices=(('buen',"Bueno"),('malo',"Malo"),('remod', "Para remodelar"),('vand', "Vandalizada"))))'''
    class Meta:
        model = Inmueble
        fields = []
        exclue = [
            'user',
            'titulo',
            'descripcion',
            'tipoInmueble',
            'antiguedad',
            'recamaras',
            'estacionamiento',
            'banos',
            'mediosBanos',
            'tipoVenta',
            'tipoRenta',
            'tirpoTraspaso',
            'precioVenta',
            'precioRenta',
            'precioTraspaso',
            'metrosConstruidos',
            'metrosTotales',
            'entidad',
            'municipio',
            'colonia',
            'calle',
            'numExt',
            'numInt',
            'codigoPostal',
            'mostrarMapa',
            'servicioGas',
            'servicioAire',
            'servicioSegu',
            'servicioCale',
            'servicioAmu',
            'estadoConservacion',
            'avisoDestacado'
        ]

class ImagenesForm(forms.ModelForm):
    class Meta:
        model = ImagenesInmbueble
        fields = ['imagen']
        exclude = [
            'inmueble'
        ]