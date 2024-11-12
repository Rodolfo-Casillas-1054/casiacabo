from django.urls import path
from enmarcados_app import views

urlpatterns = [
    path('', views.Inicio_vista, name='Inicio_vista'),
    path('RegistrarMateria/' ,views.RegistrarMateria, name='RegistrarMateria' ),
    path("SeleccionarMateria/<codigo>",views.SeleccionarMateria,name="SeleccionarMateria"),
    path("EditarMateria/",views.EditarMateria,name="EditarMateria"),
    path("BorrarMateria/<codigo>",views.BorrarMateria,name="BorrarMateria")
]