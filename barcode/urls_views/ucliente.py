"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 29 May 2020
--  Description: ucliente.py
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
from barcode.views.vcliente import *

urlpatterns = [
    path("cliente/", login_required(Listado.as_view()), name="l_Cliente"),
    path("cliente/crear", login_required(Crear.as_view()), name="c_Cliente"),
    path("cliente/detalle/<str:pk>", login_required(Detalle.as_view()), name="d_Cliente"),
    path("cliente/actualizar/<str:pk>", login_required(Actualizar.as_view()), name="u_Cliente"),
    path("cliente/eliminar/<str:pk>", login_required(Eliminar.as_view()), name="e_Cliente"),
    path("cliente/search", login_required(SearchResultsView.as_view()), name="s_Cliente"),
    path("cliente/pdf/", login_required(GeneratePdfList.as_view()), name="pl_Cliente"),
    path("cliente/pdf/<str:pk>", login_required(GeneratePdfUnid.as_view()), name="pu_Cliente")
]