from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_posts, name='lista_posts'),
    path('nuevo/', views.crear_post, name='crear_post'),
]
