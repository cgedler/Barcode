"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 29 May 2020
--  Description: uruta.py
--
--
======================================================================================
"""
#
# Imports :
#
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from barcode.views.vruta import *

urlpatterns = [
    path("ruta/", login_required(Listado.as_view()), name="l_Ruta"),
    path("ruta/crear", login_required(Crear.as_view()), name="c_Ruta"),
    path("ruta/detalle/<str:pk>", login_required(Detalle.as_view()), name="d_Ruta"),
    path("ruta/actualizar/<str:pk>", login_required(Actualizar.as_view()), name="u_Ruta"),
    path("ruta/eliminar/<str:pk>", login_required(Eliminar.as_view()), name="e_Ruta"),
    path("ruta/search", login_required(SearchResultsView.as_view()), name="s_Ruta"),
    path("ruta/pdf/", login_required(GeneratePdfList.as_view()), name="pl_Ruta"),
    path("ruta/pdf/<str:pk>", login_required(GeneratePdfUnid.as_view()), name="pu_Ruta")
]