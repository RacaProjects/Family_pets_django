from django.db import models

# Create your models here.
class Mascota(models.Model):
    fecha_registro = models.DateTimeField(auto_now_add=True)
    nombre_mascota = models.CharField(max_length=50)
    raza_mascota = models.CharField(max_length=50)
    edad_mascota = models.IntegerField()
    tamano_mascota = models.CharField(max_length=50)
    fundacion = models.CharField(max_length=100, blank=True, null=True)  # <<< campo agregado
    detalles_adicionales = models.TextField(blank=True)
    foto_mascota = models.ImageField(upload_to='fotos_mascotas/', blank=True, null=True)

    def __str__(self):
        return self.nombre_mascota
    
class Meta:
    db_table = 'Mascotas' # Colocamos el nombre de la tabla