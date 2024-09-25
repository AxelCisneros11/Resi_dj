from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("msjAgregar/", views.msjAgregar, name="msjAgregar"),
    path("msjEliminar/<int:mensaje_id>/", views.msjEliminar, name="msjEliminar"),
    path("msjEditar/<int:mensaje_id>/", views.msjEditar,  name="msjEditar"),
]