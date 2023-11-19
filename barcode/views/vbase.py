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
from datetime import date, datetime
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from barcode.models.mbultos import *
from barcode.models.morigen import *
#
# Function : Index
#
def index(request):
    object_list = Origen.objects.all()
    context = {
        'object_list' : object_list,
    }
    return render(request, 'index.html', context)
#
# Function : CountBultosSucursal
#
def CountBultosSucursal(origen, estado):
    today = date.today()
    query = Bulto.objects.filter(Q(origen__icontains=origen) & Q(estado=estado) & Q(modified__contains=today))
    total = query.count()
    return total
#
# Function : CountBultosRuta
#
def CountBultosRuta(ruta, estado):
    today = date.today()
    query = Bulto.objects.filter(Q(ruta__icontains=ruta) & Q(estado=estado) & Q(modified__contains=today))
    total = query.count()
    return total
#
# Function : CountBultosMes
#
def CountBultosMes(mes, estado):
    today = date.today()
    #print(today.year)
    query = Bulto.objects.filter(Q(estado=estado) & Q(modified__month=mes) & Q(modified__year=today.year))
    total = query.count()
    return total
#
# Function : CountBultosYear
#
def CountBultosYear(year, estado):
    query = Bulto.objects.filter(Q(estado=estado) & Q(modified__year=year))
    total = query.count()
    return total
#
# Function : Home DashBoard
#
def home(request):
    model = Bulto
    labels1 = ['BNA', 'BQO', 'CCS', 'COR', 'MIQ', 'MBO', 'MCY', 'POZ', 'PFO', 'SAN', 'VAL']
    TB_BNA = CountBultosSucursal(origen="BNA", estado="0")
    TB_BQO = CountBultosSucursal(origen="BQO", estado="0")
    TB_CCS = CountBultosSucursal(origen="CCS", estado="0")
    TB_COR = CountBultosSucursal(origen="COR", estado="0")
    TB_MIQ = CountBultosSucursal(origen="MIQ", estado="0")
    TB_MBO = CountBultosSucursal(origen="MBO", estado="0")
    TB_MCY = CountBultosSucursal(origen="MCY", estado="0")
    TB_POZ = CountBultosSucursal(origen="POZ", estado="0")
    TB_PFO = CountBultosSucursal(origen="PFO", estado="0")
    TB_SAN = CountBultosSucursal(origen="SAN", estado="0")
    TB_VAL = CountBultosSucursal(origen="VAL", estado="0")
    data1 = [TB_BNA, TB_BQO, TB_CCS, TB_COR, TB_MIQ, TB_MBO, TB_MCY, TB_POZ, TB_PFO, TB_SAN, TB_VAL]
    
    labels2 = ['BNA','BQO','CCS','COR','LLS','MBO','MCY','MER','MIQ','OCC','OR1','OR2','PFO','POZ','SAN','VAL']
    TB2_BNA = CountBultosRuta(ruta="BNA", estado="0")
    TB2_BQO = CountBultosRuta(ruta="BQO", estado="0")
    TB2_CCS = CountBultosRuta(ruta="CCS", estado="0")
    TB2_COR = CountBultosRuta(ruta="COR", estado="0")
    TB2_LLS = CountBultosRuta(ruta="LLS", estado="0")
    TB2_MBO = CountBultosRuta(ruta="MBO", estado="0")
    TB2_MCY = CountBultosRuta(ruta="MCY", estado="0")
    TB2_MER = CountBultosRuta(ruta="MER", estado="0")
    TB2_MIQ = CountBultosRuta(ruta="MIQ", estado="0")
    TB2_OCC = CountBultosRuta(ruta="OCC", estado="0")
    TB2_OR1 = CountBultosRuta(ruta="OR1", estado="0")
    TB2_OR2 = CountBultosRuta(ruta="OR2", estado="0")
    TB2_PFO = CountBultosRuta(ruta="PFO", estado="0")
    TB2_POZ = CountBultosRuta(ruta="POZ", estado="0")
    TB2_SAN = CountBultosRuta(ruta="SAN", estado="0")
    TB2_VAL = CountBultosRuta(ruta="VAL", estado="0")
    data2 = [TB2_BNA, TB2_BQO, TB2_CCS, TB2_COR, TB2_LLS, TB2_MBO, TB2_MCY, TB2_MER, TB2_MIQ, TB2_OCC, TB2_OR1, TB2_OR2, TB2_PFO, TB2_POZ, TB2_SAN, TB2_VAL]
    
    labels3 = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    TB_ENE = CountBultosMes(mes="01", estado="0")
    TB_FEB = CountBultosMes(mes="02", estado="0")
    TB_MAR = CountBultosMes(mes="03", estado="0")
    TB_ABR = CountBultosMes(mes="04", estado="0")
    TB_MAY = CountBultosMes(mes="05", estado="0")
    TB_JUN = CountBultosMes(mes="06", estado="0")
    TB_JUL = CountBultosMes(mes="07", estado="0")
    TB_AGO = CountBultosMes(mes="08", estado="0")
    TB_SEP = CountBultosMes(mes="09", estado="0")
    TB_OCT = CountBultosMes(mes="10", estado="0")
    TB_NOV = CountBultosMes(mes="11", estado="0")
    TB_DIC = CountBultosMes(mes="12", estado="0")
    data3 = [TB_ENE, TB_FEB, TB_MAR, TB_ABR, TB_MAY, TB_JUN, TB_JUL, TB_AGO, TB_SEP, TB_OCT, TB_NOV, TB_DIC]

    today = date.today()
    labels4 = [str(today.year), str(today.year - 1), str(today.year - 2), str(today.year - 3), str(today.year - 4)]
    TB_YA = CountBultosYear(year=str(today.year), estado="0")
    TB_LY = CountBultosYear(year=str(today.year - 1), estado="0")
    TB_Y3 = CountBultosYear(year=str(today.year - 2), estado="0")
    TB_Y4 = CountBultosYear(year=str(today.year - 3), estado="0")
    TB_Y5 = CountBultosYear(year=str(today.year - 4), estado="0")
    data4 = [TB_YA, TB_LY, TB_Y3, TB_Y4, TB_Y5]
 
    return render(request, 'home.html',  {
        'labels1': labels1,
        'data1': data1,
        'labels2': labels2,
        'data2': data2,
        'labels3': labels3,
        'data3': data3,
        'labels4': labels4,
        'data4': data4,
        })
#
#  name: class SearchResultsView
#
class SearchResultsView(ListView):
    model = Bulto
    template_name = "s_.html"
    def get_queryset(self):
        query_a = self.request.GET.get("origen")
        query_b = self.request.GET.get("q")
        object_list = Bulto.objects.filter(Q(guias__exact=query_b) & Q(origen__contains=query_a)
            | Q(recolecta__exact=query_b) & Q(origen__contains=query_a)
            #Q(guia_id__icontains=query) | Q(id_bulto__icontains=query)
            )
        return object_list
