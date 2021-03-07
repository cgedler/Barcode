"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 17 Septiembre 2020
--  Description: uemails.py
--
--  script file that 
======================================================================================
"""
#
# Imports :
#
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from barcode.views.vemails import *

urlpatterns = [
    path("emails/", login_required(Listado.as_view()), name="l_Email"),
    path("emails/crear", login_required(Crear.as_view()), name="c_Email"),
    path("emails/detalle/<str:pk>", login_required(Detalle.as_view()), name="d_Email"),
    path("emails/actualizar/<str:pk>", login_required(Actualizar.as_view()), name="u_Email"),
    path("emails/eliminar/<str:pk>", login_required(Eliminar.as_view()), name="e_Email"),
    path("emails/search", login_required(SearchResultsView.as_view()), name="s_Email"),
    path("emails/pdf/<str:pk>", login_required(GeneratePdfUnid.as_view()), name="pu_Email")
]