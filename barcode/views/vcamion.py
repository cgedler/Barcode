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
from barcode.models.mcamion import Camion
from barcode.forms.fcamion import CamionForm 
#
#  name: class Crear
#
class Crear(SuccessMessageMixin, CreateView):
    model = Camion
    form_class = CamionForm
    extra_context = {
        "section_title": "Crear Camión",
        "module_title": "Camión"
    }
    template_name = "camion/c_.html"
    success_message = "Creado Correctamente!"

    def get_success_url(self):
        return reverse("l_Camion")
#
#  name: class Listado
#
class Listado(ListView):
    model = Camion
    template_name = "camion/i_.html"
    queryset = Camion.objects.all().order_by('-created')
    context_object_name = 'Camion'
    paginate_by = 100
    extra_context = {
        "section_title": "Listado de Camiones",
        "module_title": "Camión"
    }
#
#  name: class Detalle
#
class Detalle(DetailView):
    model = Camion
    form_class = CamionForm
    template_name = "camion/d_.html"

    def get_context_data(self, **kwargs):
        context = super(Detalle, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        extra_context = {
            "section_title": "Detalle del Camión",
            "module_title": "Camión"
        }
        return context
#
#  name: class Actualizar
#
class Actualizar(SuccessMessageMixin, UpdateView):
    model = Camion
    form_class = CamionForm
    # template_name = "update.html"
    template_name = "camion/u_.html"
    success_message = "Actualizado Correctamente!"
    # success_url ="/"

    def get_success_url(self):
        return reverse("l_Camion")
#
#  name: class Eliminar
#
class Eliminar(SuccessMessageMixin, DeleteView):
    model = Camion
    form = Camion
    fields = "__all__"

    def get_success_url(self):
        success_message = "Eliminado Correctamente!"
        messages.success(self.request, (success_message))
        return reverse("l_Camion")
#
#  name: class SearchResultsView
#
class SearchResultsView(ListView):
    model = Camion
    template_name = "camion/s_.html"
    extra_context = {
        "section_title": "Listado de Camiones",
        "module_title": "Camión"
    }
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Camion.objects.filter(
            Q(nombre__icontains=query) | Q(
                id_camion__icontains=query)
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
            "module_title": "Camión",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": Camion.objects.all()
        }
        pdf = render_to_pdf("camion/pl_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
#
#  name: class GeneratePdfUnid
#
class GeneratePdfUnid(View):
    def get(self, request, *args, **kwargs):
        id = str
        id = kwargs["pk"]
        object_list = Camion.objects.filter(id_camion__icontains=id)
        now = timezone.now()
        emp = EmpresaDatos()
        data = {
            "section_title": "Detalle",
            "module_title": "Camión",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": object_list
        }
        pdf = render_to_pdf("camion/pu_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
