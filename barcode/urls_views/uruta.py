"""
 * Author: Christopher Gedler <cgedler@gmail.com>
 * Version: 1.0
 * Last Change: 28.05.2020 
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
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
