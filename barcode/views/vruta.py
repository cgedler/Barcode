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
from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from datetime import date
from django.utils import timezone
from django.views.generic import TemplateView, View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from barcode.utils import *
from barcode.utils.cEmpresa import *
from barcode.models.mruta import Ruta
from barcode.forms.fruta import RutaForm 
#
#  name: class Crear
#
class Crear(SuccessMessageMixin, CreateView):
    model = Ruta
    form_class = RutaForm
    extra_context = {
        "section_title": "Crear Ruta",
        "module_title": "Ruta"
    }
    template_name = "ruta/c_.html"
    success_message = "Creado Correctamente!"

    def get_success_url(self):
        return reverse("l_Ruta")
#
#  name: class Listado
#
class Listado(ListView):
    model = Ruta
    template_name = "ruta/i_.html"
    queryset = Ruta.objects.all().order_by('-created')
    context_object_name = 'Ruta'
    paginate_by = 100
    extra_context = {
        "section_title": "Listado de Rutas",
        "module_title": "Ruta"
    }
#
#  name: class Detalle
#
class Detalle(DetailView):
    model = Ruta
    form_class = RutaForm
    template_name = "ruta/d_.html"

    def get_context_data(self, **kwargs):
        context = super(Detalle, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        extra_context = {
            "section_title": "Detalle de Ruta",
            "module_title": "Ruta"
        }
        return context
#
#  name: class Actualizar
#
class Actualizar(SuccessMessageMixin, UpdateView):
    model = Ruta
    form_class = RutaForm
    # template_name = "update.html"
    template_name = "ruta/u_.html"
    success_message = "Actualizado Correctamente!"
    # success_url ="/"

    def get_success_url(self):
        return reverse("l_Ruta")
#
#  name: class Eliminar
#
class Eliminar(SuccessMessageMixin, DeleteView):
    model = Ruta
    form = Ruta
    fields = "__all__"

    def get_success_url(self):
        success_message = "Eliminado Correctamente!"
        messages.success(self.request, (success_message))
        return reverse("l_Ruta")
#
#  name: class SearchResultsView
#
class SearchResultsView(ListView):
    model = Ruta
    template_name = "ruta/s_.html"
    extra_context = {
        "section_title": "Listado de Rutas",
        "module_title": "Ruta"
    }
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Ruta.objects.filter(
            Q(nombre__icontains=query) | Q(
                id_Ruta__icontains=query)
        )
        return object_list
#
#  name: class GeneratePdfList
#
class GeneratePdfList(View):
    def get(self, request, *args, **kwargs):
        emp = EmpresaDatos()
        now = timezone.now()
        data = {
            "section_title": "Listado",
            "module_title": "Ruta",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": Ruta.objects.all()
        }
        pdf = render_to_pdf("ruta/pl_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
#
#  name: class GeneratePdfUnid
#
class GeneratePdfUnid(View):
    def get(self, request, *args, **kwargs):
        id = str
        id = kwargs["pk"]
        object_list = Ruta.objects.filter(id_ruta__icontains=id)
        now = timezone.now()
        emp = EmpresaDatos()
        data = {
            "section_title": "Detalle",
            "module_title": "Ruta",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": object_list
        }
        pdf = render_to_pdf("ruta/pu_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
