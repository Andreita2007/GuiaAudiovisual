from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_materias, name='inicio'),
    path('guias/<str:anio>/', views.ver_materia, name='ver_materia'),
    ]