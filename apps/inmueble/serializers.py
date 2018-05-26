from rest_framework import serializers
from apps.inmueble.models import Inmueble,ImagenesInmbueble

class InmuebleSerializer(serializers.ModelSerializer):
    imagenes = serializers.SerializerMethodField('obtenerImagenes')
    class Meta:
        model = Inmueble
        fields = '__all__'
    def obtenerImagenes(self,inmueble):
        imagenes = ImagenesInmbueble.objects.filter(inmueble=inmueble)
        serializer = ImagenesInmbuebleSerializer(imagenes,many=True,context=self.context)
        if serializer.data:
            return serializer.data
        return None

class ImagenesInmbuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenesInmbueble
        fields = '__all__'