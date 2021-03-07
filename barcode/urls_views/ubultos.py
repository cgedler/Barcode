"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 29 May 2020
--  Description: ubulto.py
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
from barcode.views.vbultos import *
from barcode.views.vbulcarga import *

urlpatterns = [
    path('bulto/carga', login_required(cargar), name='cargar'),
    path("bulto/cargar", login_required(CargarCamion.as_view()), name="c_Bulto"),
    path('bulto/descarga', login_required(descargar), name='descargar'),
    path("bulto/descargar", login_required(DescargarCamion.as_view()), name="d_Bulto"),
    path('bulto/entrega', login_required(entregar), name='entregar'),
    path("bulto/entregar", login_required(EntregarBulto.as_view()), name="e_Bulto"),
    path('bulto/cargados', login_required(cargados), name='cargados'),
    path("bulto/pdf/", login_required(Bultosxcargar.as_view()), name="pl_xCargar"),
    path("bulto/pdf1/", login_required(Bultoscargados.as_view()), name="pl_xCargados"),
    path("bulto/pdf2/", login_required(Bultosxcamion.as_view()), name="pl_xCamion"),
]