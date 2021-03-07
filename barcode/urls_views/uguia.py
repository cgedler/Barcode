"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 29 May 2020
--  Description: uguia.py
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
from barcode.views.vguia import *
from barcode.excel_views.exbultos import *

urlpatterns = [
    path("guia/", login_required(Listado.as_view()), name="l_Guia"),
    path("guia/crear", login_required(Crear.as_view()), name="c_Guia"),
    path("guia/detalle/<str:pk>", login_required(Detalle.as_view()), name="d_Guia"),
    path("guia/actualizar/<str:pk>", login_required(Actualizar.as_view()), name="u_Guia"),
    path("guia/eliminar/<str:pk>", login_required(Eliminar.as_view()), name="e_Guia"),
    path("guia/search", login_required(SearchResultsView.as_view()), name="s_Guia"),
    path("guia/pdf/", login_required(GeneratePdfList.as_view()), name="pl_Guia"),
    path("guia/pdf/<str:pk>", login_required(GeneratePdfUnid.as_view()), name="pu_Guia"),
    path("guia/etiqueta/<str:pk>", login_required(GenerateEtiquetasPdf.as_view()), name="etp_Guia"),
    path("guia/excel/<str:pk>", GenerateEtiquetas.as_view(), name="ex_Guia")
]