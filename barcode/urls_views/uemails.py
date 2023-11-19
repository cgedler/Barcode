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
