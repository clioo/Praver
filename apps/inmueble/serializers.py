from rest_framework import serializers
from apps.inmueble.models import Inmueble,ImagenesInmbueble

class InmuebleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inmueble
        fields = '__all__'