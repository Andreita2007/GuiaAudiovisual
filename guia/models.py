from django.db import models

# Create your models here.

class ContenidoAudiovisual(models.Model):
    OPCIONES_ANIO = [
        ('2', 'Segundo Año'),
        ('4', 'Cuarto Año'),
    ]
    
    titulo = models.CharField(max_length=200, verbose_name="Título del Video")
    descripcion = models.TextField(verbose_name="Párrafo Informativo")
    video_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="Enlace de Youtube")
    anio = models.CharField(max_length=10, choices=OPCIONES_ANIO, verbose_name="Año Escolar")
    imagen = models.ImageField(upload_to='guia_fotos/', blank=True, null=True, verbose_name = "Imagen Explicativa")
    
    def __str__(self):
        return f"{self.titulo} - {self.get_anio_display()}"