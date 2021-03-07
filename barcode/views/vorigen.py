"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 29 May 2020
--  Description: vorigen.py
--
--
======================================================================================
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
from barcode.models.morigen import Origen
from barcode.forms.forigen import OrigenForm 
#
#  name: class Crear
#
class Crear(SuccessMessageMixin, CreateView):
    model = Origen
    form_class = OrigenForm
    extra_context = {
        "section_title": "Crear Origen",
        "module_title": "Origen"
    }
    template_name = "origen/c_.html"
    success_message = "Creado Correctamente!"

    def get_success_url(self):
        return reverse("l_Origen")
#
#  name: class Listado
#
class Listado(ListView):
    model = Origen
    template_name = "origen/i_.html"
    queryset = Origen.objects.all().order_by('-created')
    context_object_name = 'Origen'
    paginate_by = 100
    extra_context = {
        "section_title": "Listado lugar de Origen",
        "module_title": "Origen"
    }
#
#  name: class Detalle
#
class Detalle(DetailView):
    model = Origen
    form_class = OrigenForm
    template_name = "origen/d_.html"

    def get_context_data(self, **kwargs):
        context = super(Detalle, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        extra_context = {
            "section_title": "Detalle lugar de Origen",
            "module_title": "Origen"
        }
        return context
#
#  name: class Actualizar
#
class Actualizar(SuccessMessageMixin, UpdateView):
    model = Origen
    form_class = OrigenForm
    # template_name = "update.html"
    template_name = "origen/u_.html"
    success_message = "Actualizado Correctamente!"
    # success_url ="/"

    def get_success_url(self):
        return reverse("l_Origen")
#
#  name: class Eliminar
#
class Eliminar(SuccessMessageMixin, DeleteView):
    model = Origen
    form = Origen
    fields = "__all__"

    def get_success_url(self):
        success_message = "Eliminado Correctamente!"
        messages.success(self.request, (success_message))
        return reverse("l_Origen")
#
#  name: class SearchResultsView
#
class SearchResultsView(ListView):
    model = Origen
    template_name = "origen/s_.html"
    extra_context = {
        "section_title": "Listado lugar de Origen",
        "module_title": "Origen"
    }
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Origen.objects.filter(
            Q(nombre__icontains=query) | Q(
                id_origen__icontains=query)
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
            "module_title": "Origen",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": Origen.objects.all()
        }
        pdf = render_to_pdf("origen/pl_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")
#
#  name: class GeneratePdfUnid
#
class GeneratePdfUnid(View):
    def get(self, request, *args, **kwargs):
        id = str
        id = kwargs["pk"]
        object_list = Origen.objects.filter(id_origen__icontains=id)
        now = timezone.now()
        emp = EmpresaDatos()
        data = {
            "section_title": "Detalle",
            "module_title": "Origen",
            "today": now,
            "empresa_nombre": emp.nombre,
            "empresa_rif": emp.rif,
            "empresa_direstado": emp.dir_estado,
            "empresa_dirciudad": emp.dir_ciudad,
            "empresa_direccion": emp.direccion,
            "empresa_postal": emp.postal,
            "context_pdf": object_list
        }
        pdf = render_to_pdf("origen/pu_.html", data)
        return HttpResponse(pdf, content_type="application/pdf")