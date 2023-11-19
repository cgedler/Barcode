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
from django.http import HttpResponse, JsonResponse
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
from django.core import serializers
from crum import get_current_user
from crum import impersonate
from barcode.utils import *
from barcode.utils.cEmpresa import *
from barcode.models.mguia import Guia
from barcode.forms.fguia import GuiaForm, GuiaDForm
from barcode.models.mdestino import Destino
from barcode.models.mbultos import Bulto
from barcode.models.memail import Email
from barcode.models.morigen import *
from barcode.models.mcliente import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
#
#  name: class Crear
#
class Crear(SuccessMessageMixin, CreateView):
    model = Guia
    form_class = GuiaForm
    template_name = "guia/c_.html"
    success_message = "Creado Correctamente!"
    data_destino = serializers.serialize('json', Destino.objects.all(), fields=('id_destino','nombre','rutas'))
    extra_context = {
        "section_title": "Crear Guía",
        "module_title": "Guía",
        "data_destino": data_destino,
    }
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {} 
        try:
            if 'action' in request.POST:
                form = GuiaForm(request.POST)
                data = form.save()
                data['url'] = self.get_success_url()
            else :
                data_dict = json.loads(request.POST.get('ArrJson'))  
                if 'query_b' in data_dict:
                    query_a = data_dict['query_a']
                    query_b = data_dict['query_b']
                    result = Cliente.objects.filter(Q(tipo_persona__icontains=query_a) & Q(id_cliente__exact=query_b))
                    if result.count() == 0:
                        data = ""
                    else:
                        email = Email.objects.filter(Q(email_cliente__exact=query_b))
                        all_objects = [*email, *result]
                        data = serializers.serialize('json', all_objects)
                elif 'query_d' in data_dict:
                    query_c = data_dict['query_c']
                    query_d = data_dict['query_d']
                    result = Cliente.objects.filter(Q(tipo_persona__icontains=query_c) & Q(id_cliente__exact=query_d))
                    if result.count() == 0:
                        data = ""
                    else:
                        email = Email.objects.filter(Q(email_cliente__exact=query_d))
                        all_objects = [*email, *result]
                        data = serializers.serialize('json', all_objects)
        except Exception as e:
            data['errors'] = str(e)
        return JsonResponse(data, safe=False)
    def get_success_url(self):
        return reverse("l_Guia")
#
#  name: class Listado
#
class Listado(ListView):
    model = Guia
    template_name = "guia/i_.html"
    queryset = Guia.objects.filter(estado__contains="A").order_by('-created')
    context_object_name = 'Guía'
    paginate_by = 100
    extra_context = {
        "section_title": "Listado de Guías",
        "module_title": "Guía"
    }
#
#  name: class Detalle
#
class Detalle(DetailView):
    model = Guia
    form_class = GuiaDForm
    template_name = "guia/d_.html"
    def get_context_data(self, **kwargs):
        context = super(Detalle, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        extra_context = {
            "section_title": "Detalle de la Guía",
            "module_title": "Guía"
        }
        return context
#
#  name: class Actualizar
#
class Actualizar(SuccessMessageMixin, UpdateView):
    model = Guia
    form_class = GuiaDForm
    data_destino = serializers.serialize('json', Destino.objects.all(), fields=('id_destino','nombre','rutas'))
    extra_context = {
        "section_title": "Crear Guía",
        "module_title": "Guía",
        "data_destino": data_destino,
    }
    template_name = "guia/u_.html"
    success_message = "Actualizado Correctamente!"
    def get_success_url(self):
        return reverse("l_Guia")
#
#  name: class Eliminar
#
class Eliminar(SuccessMessageMixin, DeleteView):
    model = Guia
    form = Guia
    fields = "__all__"

    def get_success_url(self):
        success_message = "Eliminado Correctamente!"
        messages.success(self.request, (success_message))
        return reverse("l_Guia")
#
#  name: class SearchResultsView
#
class SearchResultsView(ListView):
    model = Guia
    template_name = "guia/s_.html"
    extra_context = {
        "section_title": "Listado de Guía",
        "module_title": "Guía"
    }
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Guia.objects.filter(
            Q(id__icontains=query)
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
            "module_title": "Guía",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": Guia.objects.all()
        }
        pdf = render_to_pdf("guia/pl_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
#
#  name: class GeneratePdfUnid
#
class GeneratePdfUnid(View):
    def get(self, request, *args, **kwargs):
        id = str
        id = kwargs["pk"]
        object_list = Guia.objects.filter(id__exact=id)
        now = timezone.now()
        emp = EmpresaDatos()
        data = {
            "section_title": "Detalle",
            "module_title": "Guía",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": object_list
        }
        pdf = render_to_pdf("guia/pu_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
#
#  name: class GenerateEtiquetas
#
class GenerateEtiquetasPdf(View):
    def get(self, request, *args, **kwargs):
        id = str
        id = kwargs["pk"]
        model = Bulto
        object_list = Bulto.objects.filter(guias__icontains=id)
        now = timezone.now()
        emp = EmpresaDatos()
        data = {
            "section_title": "Detalle",
            "module_title": "Guía",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": object_list
        }
        pdf = render_to_pdf("guia/etp_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
