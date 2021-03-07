"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 29 May 2020
--  Description: ucamion.py
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
from barcode.views.vcamion import *

urlpatterns = [
    path("Camion/", login_required(Listado.as_view()), name="l_Camion"),
    path("Camion/crear", login_required(Crear.as_view()), name="c_Camion"),
    path("Camion/detalle/<str:pk>", login_required(Detalle.as_view()), name="d_Camion"),
    path("Camion/actualizar/<str:pk>", login_required(Actualizar.as_view()), name="u_Camion"),
    path("Camion/eliminar/<str:pk>", login_required(Eliminar.as_view()), name="e_Camion"),
    path("Camion/search", login_required(SearchResultsView.as_view()), name="s_Camion"),
    path("Camion/pdf/", login_required(GeneratePdfList.as_view()), name="pl_Camion"),
    path("Camion/pdf/<str:pk>", login_required(GeneratePdfUnid.as_view()), name="pu_Camion")
]