from rest_framework import serializers
from apps.inmueble.models import Inmueble,ImagenesInmbueble,Localidades
from django.contrib.auth.models import User
from apps.usuarios.models import Profile
class InmuebleSerializer(serializers.ModelSerializer):
    imagenes = serializers.SerializerMethodField('obtenerImagenes')
    descripciones = serializers.SerializerMethodField('obtenerDescripciones')
    datosVendedor = serializers.SerializerMethodField('obtenerDatosVendedor')
    class Meta:
        model = Inmueble
        fields = '__all__'
    def obtenerImagenes(self,inmueble):
        imagenes = ImagenesInmbueble.objects.filter(inmueble=inmueble)
        serializer = ImagenesInmbuebleSerializer(imagenes,many=True,context=self.context)
        if serializer.data:
            return serializer.data
        return None
    def obtenerDescripciones(self, inmueble):
        localidad = Localidades.objects.filter(id=inmueble.colonia)
        serializer = DescripcionLocalidades(localidad,many=True,context=self.context)
        return serializer.data
    def obtenerDatosVendedor(self,inmueble):
        perfil = Profile.objects.filter(user=inmueble.user.id)
        serializer = ProfileSerializer(perfil,many=True,context=self.context)
        return serializer.data



class ImagenesInmbuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenesInmbueble
        fields = '__all__'
class LocalidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Localidades
        fields = '__all__'
class DescripcionLocalidades(serializers.Serializer):
    d_ciudad = serializers.CharField(max_length=30)
    d_asenta = serializers.CharField(max_length=30)
    D_mnpio = serializers.CharField(max_length=30)
    d_estado = serializers.CharField(max_length=30)

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email']

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField('obtenerEmail')
    class Meta:
        model = Profile
        fields= '__all__'
    def obtenerEmail(request,user):
        usuario = User.objects.get(id=user.user.id)
        serializer = EmailSerializer(usuario)
        print(usuario.email)
        return usuario.email

    
