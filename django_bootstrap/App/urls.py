from django.urls import path
from App import views

urlpatterns = [
    path('index/', views.inicio),
    path('cursos/', views.cursos),
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables)
]
