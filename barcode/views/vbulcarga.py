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
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from datetime import date
from django.utils import timezone
from django.views.generic import TemplateView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core import serializers
from django.db.models import Q
from barcode.utils import *
from barcode.utils.cEmpresa import *
from barcode.models.mbultos import *
from barcode.models.morigen import *
from barcode.models.mruta import *
from barcode.models.mcamion import *
from barcode.models.mguia import *
from barcode.views.vbase import CountBultosRuta
from django.db.models import Count
#
# Function : Reporte Bultos Cargados
#
def cargados(request):
    labels1 = ['BNA','BQO','CCS','COR','LLS','MBO','MCY','MER','MIQ','OCC','OR1','OR2','PFO','POZ','SAN','VAL']
    TB1_BNA = CountBultosRuta(ruta='BNA', estado='0')
    TB1_BQO = CountBultosRuta(ruta='BQO', estado='0')
    TB1_CCS = CountBultosRuta(ruta='CCS', estado='0')
    TB1_COR = CountBultosRuta(ruta='COR', estado='0')
    TB1_LLS = CountBultosRuta(ruta='LLS', estado='0')
    TB1_MBO = CountBultosRuta(ruta='MBO', estado='0')
    TB1_MCY = CountBultosRuta(ruta='MCY', estado='0')
    TB1_MER = CountBultosRuta(ruta='MER', estado='0')
    TB1_MIQ = CountBultosRuta(ruta='MIQ', estado='0')
    TB1_OCC = CountBultosRuta(ruta='OCC', estado='0')
    TB1_OR1 = CountBultosRuta(ruta='OR1', estado='0')
    TB1_OR2 = CountBultosRuta(ruta='OR2', estado='0')
    TB1_PFO = CountBultosRuta(ruta='PFO', estado='0')
    TB1_POZ = CountBultosRuta(ruta='POZ', estado='0')
    TB1_SAN = CountBultosRuta(ruta='SAN', estado='0')
    TB1_VAL = CountBultosRuta(ruta='VAL', estado='0')
    data1 = [TB1_BNA, TB1_BQO, TB1_CCS, TB1_COR, TB1_LLS, TB1_MBO, TB1_MCY, TB1_MER, TB1_MIQ, TB1_OCC, TB1_OR1, TB1_OR2, TB1_PFO, TB1_POZ, TB1_SAN, TB1_VAL]

    labels2 = ['BNA','BQO','CCS','COR','LLS','MBO','MCY','MER','MIQ','OCC','OR1','OR2','PFO','POZ','SAN','VAL']
    TB2_BNA = CountBultosRuta(ruta='BNA', estado='1')
    TB2_BQO = CountBultosRuta(ruta='BQO', estado='1')
    TB2_CCS = CountBultosRuta(ruta='CCS', estado='1')
    TB2_COR = CountBultosRuta(ruta='COR', estado='1')
    TB2_LLS = CountBultosRuta(ruta='LLS', estado='1')
    TB2_MBO = CountBultosRuta(ruta='MBO', estado='1')
    TB2_MCY = CountBultosRuta(ruta='MCY', estado='1')
    TB2_MER = CountBultosRuta(ruta='MER', estado='1')
    TB2_MIQ = CountBultosRuta(ruta='MIQ', estado='1')
    TB2_OCC = CountBultosRuta(ruta='OCC', estado='1')
    TB2_OR1 = CountBultosRuta(ruta='OR1', estado='1')
    TB2_OR2 = CountBultosRuta(ruta='OR2', estado='1')
    TB2_PFO = CountBultosRuta(ruta='PFO', estado='1')
    TB2_POZ = CountBultosRuta(ruta='POZ', estado='1')
    TB2_SAN = CountBultosRuta(ruta='SAN', estado='1')
    TB2_VAL = CountBultosRuta(ruta='VAL', estado='1')
    data2 = [TB2_BNA, TB2_BQO, TB2_CCS, TB2_COR, TB2_LLS, TB2_MBO, TB2_MCY, TB2_MER, TB2_MIQ, TB2_OCC, TB2_OR1, TB2_OR2, TB2_PFO, TB2_POZ, TB2_SAN, TB2_VAL]
    
    labels3 = ['BNA','BQO','CCS','COR','LLS','MBO','MCY','MER','MIQ','OCC','OR1','OR2','PFO','POZ','SAN','VAL']
    TB3_BNA = CountBultosRuta(ruta='BNA', estado='2')
    TB3_BQO = CountBultosRuta(ruta='BQO', estado='2')
    TB3_CCS = CountBultosRuta(ruta='CCS', estado='2')
    TB3_COR = CountBultosRuta(ruta='COR', estado='2')
    TB3_LLS = CountBultosRuta(ruta='LLS', estado='2')
    TB3_MBO = CountBultosRuta(ruta='MBO', estado='2')
    TB3_MCY = CountBultosRuta(ruta='MCY', estado='2')
    TB3_MER = CountBultosRuta(ruta='MER', estado='2')
    TB3_MIQ = CountBultosRuta(ruta='MIQ', estado='2')
    TB3_OCC = CountBultosRuta(ruta='OCC', estado='2')
    TB3_OR1 = CountBultosRuta(ruta='OR1', estado='2')
    TB3_OR2 = CountBultosRuta(ruta='OR2', estado='2')
    TB3_PFO = CountBultosRuta(ruta='PFO', estado='2')
    TB3_POZ = CountBultosRuta(ruta='POZ', estado='2')
    TB3_SAN = CountBultosRuta(ruta='SAN', estado='2')
    TB3_VAL = CountBultosRuta(ruta='VAL', estado='2')
    data3 = [TB3_BNA, TB3_BQO, TB3_CCS, TB3_COR, TB3_LLS, TB3_MBO, TB3_MCY, TB3_MER, TB3_MIQ, TB3_OCC, TB3_OR1, TB3_OR2, TB3_PFO, TB3_POZ, TB3_SAN, TB3_VAL]
    
    origen_list = Origen.objects.all()
    ruta_list = Ruta.objects.all()
    camion_list = Camion.objects.all()
    context = {
        'origen_list': origen_list,
        'ruta_list': ruta_list,
        'camion_list': camion_list,
        'labels1': labels1,
        'data1': data1,
        'labels2': labels2,
        'data2': data2,
        'labels3': labels3,
        'data3': data3,
    }
    return render(request, 'bulto/i_.html', context)
#
#  name: class Bultosxcargar
#
class Bultosxcargar(View):
    model = Bulto
    def get(self, request, *args, **kwargs):
        today = date.today()
        query_a = self.request.GET.get('origen1')
        query_b = self.request.GET.get('ruta1')
        results = Bulto.objects.filter(Q(origen__icontains=query_a) & Q(ruta__icontains=query_b) & Q(estado='0') & Q(modified__contains=today))
        total_bultos_cargados = results.count()
        result_dict = {}
        keys_dict = []
        total_bultos_guia = ""
        for result in results:
            if not result.guias in keys_dict:
                keys_dict.append(result.guias) 
        result_dict = dict.fromkeys(keys_dict)
        total_guias_cargados = str(len(keys_dict))
        for key in result_dict:
            datos_guia = []
            result_guia = Guia.objects.filter(Q(guia__exact=key))
            for result_b in result_guia:
                datos_guia.append(result_b.cantidad) 
                result_bultos = results.filter(guias=key)
                total_bultos_guia = result_bultos.count()
                datos_guia.append(total_bultos_guia)
                result_dict[key] = datos_guia
        emp = EmpresaDatos()
        now = timezone.now()
        data = {
            'section_title': 'Total de Bultos por cargar : ' + str(total_bultos_cargados),
            'module_title': 'Reporte',
            'today': now,
            'empresa_nombre': emp.nombre,
            'empresa_rif': emp.rif,
            'empresa_direstado': emp.dir_estado,
            'empresa_dirciudad': emp.dir_ciudad,
            'empresa_direccion': emp.direccion,
            'empresa_postal': emp.postal,
            'ruta': 'Ruta : ' + query_b,
            'guias': result_dict,
            'total_guias': total_guias_cargados,
            'total_bultos': total_bultos_cargados,
            'total_bultos_guia': total_bultos_guia
        }
        pdf = render_to_pdf('bulto/pl_xC.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#
#  name: class Bultoscargados
#
class Bultoscargados(View):
    model = Bulto
    def get(self, request, *args, **kwargs):
        today = date.today()
        query_a = self.request.GET.get('origen2')
        query_b = self.request.GET.get('ruta2')
        results = Bulto.objects.filter(Q(origen__icontains=query_a) & Q(ruta__icontains=query_b) & Q(estado='1') & Q(modified__contains=today))
        total_bultos_cargados = results.count()
        result_dict = {}
        keys_dict = []
        total_bultos_guia = ""
        for result in results:
            if not result.guias in keys_dict:
                keys_dict.append(result.guias) 
        result_dict = dict.fromkeys(keys_dict)
        total_guias_cargados = str(len(keys_dict))
        for key in result_dict:
            datos_guia = []
            result_guia = Guia.objects.filter(Q(guia__exact=key))
            for result_b in result_guia:
                datos_guia.append(result_b.cantidad) 
                result_bultos = results.filter(guias=key)
                total_bultos_guia = result_bultos.count()
                datos_guia.append(total_bultos_guia)
                result_dict[key] = datos_guia
        emp = EmpresaDatos()
        now = timezone.now()
        data = {
            'section_title': 'Total de Bultos ya cargados : ' + str(total_bultos_cargados),
            'module_title': 'Reporte',
            'today': now,
            'empresa_nombre': emp.nombre,
            'empresa_rif': emp.rif,
            'empresa_direstado': emp.dir_estado,
            'empresa_dirciudad': emp.dir_ciudad,
            'empresa_direccion': emp.direccion,
            'empresa_postal': emp.postal,
            'ruta': 'Ruta : ' + query_b,
            'guias': result_dict,
            'total_guias': total_guias_cargados,
            'total_bultos': total_bultos_cargados,
            'total_bultos_guia': total_bultos_guia
        }
        pdf = render_to_pdf('bulto/pl_C.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
#
#  name: class Bultosxcamion
#
class Bultosxcamion(View):
    model = Bulto
    def get(self, request, *args, **kwargs):
        today = date.today()
        query_a = self.request.GET.get('origen3')
        query_b = self.request.GET.get('camion')
        results = Bulto.objects.filter(Q(origen__icontains=query_a) & Q(camion__icontains=query_b) & Q(estado='1') & Q(modified__contains=today))
        total_bultos_cargados = results.count()
        result_dict = {}
        keys_dict = []
        total_bultos_guia = ""
        for result in results:
            if not result.guias in keys_dict:
                keys_dict.append(result.guias) 
        result_dict = dict.fromkeys(keys_dict)
        total_guias_cargados = str(len(keys_dict))
        for key in result_dict:
            datos_guia = []
            result_guia = Guia.objects.filter(Q(guia__exact=key))
            for result_b in result_guia:
                datos_guia.append(result_b.cantidad) 
                result_bultos = results.filter(guias=key)
                total_bultos_guia = result_bultos.count()
                datos_guia.append(total_bultos_guia)
                result_dict[key] = datos_guia
        emp = EmpresaDatos()
        now = timezone.now()
        data = {
            'section_title': 'Total de Bultos cargados : ' + str(total_bultos_cargados),
            'module_title': 'Reporte',
            'today': now,
            'empresa_nombre': emp.nombre,
            'empresa_rif': emp.rif,
            'empresa_direstado': emp.dir_estado,
            'empresa_dirciudad': emp.dir_ciudad,
            'empresa_direccion': emp.direccion,
            'empresa_postal': emp.postal,
            'ruta': 'Camión : ' + query_b,
            'guias': result_dict,
            'total_guias': total_guias_cargados,
            'total_bultos': total_bultos_cargados,
            'total_bultos_guia': total_bultos_guia
        }
        pdf = render_to_pdf('bulto/pl_xCam.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
