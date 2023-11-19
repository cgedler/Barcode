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
from barcode.utils import *
from barcode.utils.cEmpresa import *
from barcode.models.memail import Email
from barcode.forms.femail import EmailForm
from barcode.models.mcliente import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 
#
#  name: class Crear
#
class Crear(SuccessMessageMixin, CreateView):
    model = Email
    form_class = EmailForm
    extra_context = {
        "section_title": "Crear Emails",
        "module_title": "Email"
    }
    template_name = "emails/c_.html"
    success_message = "Creado Correctamente!"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {} 
        try:
            if 'action' in request.POST:
                form = EmailForm(request.POST)
                data = form.save()
                data['url'] = self.get_success_url()
            else :
                data_dict = json.loads(request.POST.get('ArrJson'))  
                query_a = data_dict['query_a']
                query_b = data_dict['query_b']
                result = Cliente.objects.filter(Q(tipo_persona__icontains=query_a) & Q(id_cliente__exact=query_b))
                if result.count() == 0:
                    data = ""
                else:
                    data = serializers.serialize('json', result, fields=('id_cliente','nombre'))
        except Exception as e:
            data['errors'] = str(e)
        return JsonResponse(data, safe=False)

    def get_success_url(self):
        return reverse("l_Email")
#
#  name: class Listado
#
class Listado(ListView):
    model = Email
    template_name = "emails/i_.html"
    queryset = Email.objects.all().order_by('-created')
    context_object_name = 'email'
    paginate_by = 100
    extra_context = {
        "section_title": "Listado de Emails",
        "module_title": "Email"
    }
#
#  name: class Detalle
#
class Detalle(DetailView):
    model = Email
    form_class = EmailForm
    template_name = "emails/d_.html"

    def get_context_data(self, **kwargs):
        context = super(Detalle, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        extra_context = {
            "section_title": "Detalle Email",
            "module_title": "Email"
        }
        return context
#
#  name: class Actualizar
#
class Actualizar(SuccessMessageMixin, UpdateView):
    model = Email
    form_class = EmailForm
    # template_name = "update.html"
    template_name = "emails/u_.html"
    success_message = "Actualizado Correctamente!"
    # success_url ="/"

    def get_success_url(self):
        return reverse("l_Email")
#
#  name: class Eliminar
#
class Eliminar(SuccessMessageMixin, DeleteView):
    model = Email
    form = EmailForm
    fields = "__all__"

    def get_success_url(self):
        success_message = "Eliminado Correctamente!"
        messages.success(self.request, (success_message))
        return reverse("l_Email")
#
#  name: class SearchResultsView
#
class SearchResultsView(ListView):
    model = Email
    template_name = "emails/s_.html"
    extra_context = {
        "section_title": "Listado de Emails",
        "module_title": "Email"
    }
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Email.objects.filter(Q(id__contains=query) #Q(email_cliente__exact=query) |
        )
        return object_list
#
#  name: class GeneratePdfUnid
#
class GeneratePdfUnid(View):
    def get(self, request, *args, **kwargs):
        id = str
        id = kwargs["pk"]
        object_list = email.objects.filter(id__icontains=id)
        now = timezone.now()
        emp = EmpresaDatos()
        data = {
            "section_title": "Detalle",
            "module_title": "Email",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": object_list
        }
        pdf = render_to_pdf("emails/pu_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
