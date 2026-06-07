from django.contrib import admin
from .models import ContenidoAudiovisual
# Register your models here.

@admin.register(ContenidoAudiovisual)
class ContenidoAudiovisualAdmin (admin.ModelAdmin):
    list_display = ('titulo', 'anio', 'descripcion_corta', 'video')
    list_filter = ('anio',)
    search_fields = ('titulo', 'descripcion')
    fieldsets = (
        ('Información General', {
            'fields': ('titulo', 'descripcion')
        }),
        ('Clasificación y Archivo', {
            'fields': ('anio', 'video')
        })
    )

    def descripcion_corta(self, obj):
        if len(obj.descripcion)>50:
            return obj.descripcion[:50] + "..."
        return obj.descripcion

    descripcion_corta.short_description = "Descripción"