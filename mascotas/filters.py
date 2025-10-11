import django_filters
from .models import Mascota

class MascotaFilter(django_filters.FilterSet):
    class Meta:
        model = Mascota
        fields = {
            'nombre_mascota': ['icontains'],  # filtro que busca coincidencias en el nombre
            'raza_mascota': ['icontains'],
            'edad_mascota': ['exact', 'lt', 'gt'],  # exacto, menor que, mayor que
        }
