from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('nuevo/', views.crear_post, name='crear_post'),
    path('editar/<int:pk>/', views.editar_post, name = 'editar post'),
    path('eliminar/<int:pk>/', views.eliminar_post, name = 'eliminar post'),
]
