from rest_framework import serializers
from apps.inmueble.models import Inmueble,ImagenesInmbueble,Localidades

class InmuebleSerializer(serializers.ModelSerializer):
    imagenes = serializers.SerializerMethodField('obtenerImagenes')
    descripciones = serializers.SerializerMethodField('obtenerDescripciones')
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
