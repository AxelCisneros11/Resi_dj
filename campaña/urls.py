from django.urls import path
from . import views


urlpatterns = [
    path("index/", views.index, name="index"),
    path("agregar/", views.agregar, name="agregar"),
    path("eliminar/<int:campaña_id>/", views.eliminar, name="eliminar"),
    path("editar/<int:campaña_id>/", views.editar,  name="editar"),
]