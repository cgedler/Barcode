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
