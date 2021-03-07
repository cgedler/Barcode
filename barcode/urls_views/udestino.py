"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 29 May 2020
--  Description: udestino.py
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
from barcode.views.vdestino import *

urlpatterns = [
    path("destino/", login_required(Listado.as_view()), name="l_Destino"),
    path("destino/crear", login_required(Crear.as_view()), name="c_Destino"),
    path("destino/detalle/<str:pk>", login_required(Detalle.as_view()), name="d_Destino"),
    path("destino/actualizar/<str:pk>", login_required(Actualizar.as_view()), name="u_Destino"),
    path("destino/eliminar/<str:pk>", login_required(Eliminar.as_view()), name="e_Destino"),
    path("destino/search", login_required(SearchResultsView.as_view()), name="s_Destino"),
    path("destino/pdf/", login_required(GeneratePdfList.as_view()), name="pl_Destino"),
    path("destino/pdf/<str:pk>", login_required(GeneratePdfUnid.as_view()), name="pu_Destino")
]