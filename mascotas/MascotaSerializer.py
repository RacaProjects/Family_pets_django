from rest_framework import serializers
from .models import Mascota

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = [
            'id',                  
            'fecha_registro',
            'nombre_mascota',
            'raza_mascota',
            'edad_mascota',
            'tamano_mascota',
            'fundacion',
            'detalles_adicionales',
            'foto_mascota'
        ]
