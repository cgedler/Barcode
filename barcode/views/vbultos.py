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
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import View
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings
from barcode.models.mbultos import *
from barcode.models.mcamion import *
from barcode.models.mcliente import *
#
#  name: function cargar
#
def cargar(request):
    object_list = Camion.objects.all()
    context = {
        'object_list' : object_list,
    }
    return render(request, "bulto/c_.html", context)
#
#  name: function cargar
#
def descargar(request):
    return render(request, "bulto/d_.html")
#
#  name: function cargar
#
def entregar(request):
    return render(request, "bulto/e_.html")
#
#  name: CargarCamion 
#
class CargarCamion(SuccessMessageMixin, View):
    model = Bulto
    def get(self, request, *args, **kwargs):
        today = str(datetime.now())
        query = self.request.GET.get("q")
        var_camion = self.request.GET.get("camion")
        try:
            query_a = Bulto.objects.filter(id_bulto__icontains=query)
            valor_0 = query_a[0].estado 
            var_guia = query_a[0].guias
            query_m = Guia.objects.filter(guia__exact=var_guia)
            cantidad_guia = query_m[0].cantidad
            if valor_0 == '0':
                if int(cantidad_guia) <= 50:
                    Bulto.objects.filter(id_bulto__icontains=query).update(estado="1", camion=var_camion, modified=today)
                else:
                    Bulto.objects.filter(guias__exact=var_guia).update(estado="1", camion=var_camion, modified=today)
                count_bultos = CountBultos(num_guia=var_guia, estado="0")
                if count_bultos == 0:
                    if ValFirstMail(num_guia=var_guia):
                        pass
                    else:
                        query_c = Guia.objects.filter(guia__exact=var_guia)
                        correo_r = query_c[0].email_r
                        SendCorreo(sndemail=correo_r, msjhtml='Su envío se encuentra en ruta de transito.')
                        correo_d = query_c[0].email_d
                        SendCorreo(sndemail=correo_d, msjhtml='Su envío se encuentra en ruta de transito.')
                        Guia.objects.filter(guia__exact=var_guia).update(fmail=True)
                success_message = "Bulto cargado Correctamente!"
                return HttpResponseRedirect(self.get_success_url(success_message))
            else:  
                if ValFirstMail(num_guia=var_guia):
                    pass
                else:
                    query_c = Guia.objects.filter(guia__exact=var_guia)
                    correo_r = query_c[0].email_r
                    SendCorreo(sndemail=correo_r, msjhtml='Su envío se encuentra en ruta de transito.')
                    correo_d = query_c[0].email_d
                    SendCorreo(sndemail=correo_d, msjhtml='Su envío se encuentra en ruta de transito.')
                    Guia.objects.filter(guia__exact=var_guia).update(fmail=True)
                success_message = "El Bulto ya fue cargado Correctamente - Escanee otro Código!"
                return HttpResponseRedirect(self.get_success_url(success_message))
        except Exception as e:
            success_message = "Error al cargar el Bulto!!" + str(e)
            return HttpResponseRedirect(self.get_success_url(success_message))
    def get_success_url(self, success_message):
        messages.success(self.request, (success_message))
        return reverse("cargar")
#
#  name: DescargarCamion 
#
class DescargarCamion(SuccessMessageMixin, View):
    model = Bulto
    def get(self, request, *args, **kwargs):
        today = str(datetime.now())
        query = self.request.GET.get("q")
        try:
            query_a = Bulto.objects.filter(id_bulto__icontains=query)
            valor_0 = query_a[0].estado
            var_guia = query_a[0].guias
            query_m = Guia.objects.filter(guia__exact=var_guia)
            cantidad_guia = query_m[0].cantidad
            if valor_0 == '1':
                if int(cantidad_guia) <= 50:
                    Bulto.objects.filter(id_bulto__icontains=query).update(estado="2", modified=today)
                else:
                    Bulto.objects.filter(guias__exact=var_guia).update(estado="2", modified=today)
                count_bultos = CountBultos(num_guia=var_guia, estado="1")
                if count_bultos == 0:
                    if ValSecondMail(num_guia=var_guia):
                        pass
                    else:
                        query_c = Guia.objects.filter(guia__exact=var_guia)
                        correo_r = query_c[0].email_r
                        SendCorreo(sndemail=correo_r, msjhtml='Su envío se encuentra en proceso de entrega en la ciudad de destino.')
                        correo_d = query_c[0].email_d
                        SendCorreo(sndemail=correo_d, msjhtml='Su envío se encuentra en proceso de entrega en la ciudad de destino.')
                        Guia.objects.filter(guia__exact=var_guia).update(smail=True)
                success_message = "Bulto descargado Correctamente!"
                return HttpResponseRedirect(self.get_success_url(success_message))
            else:  
                if ValSecondMail(num_guia=var_guia):
                    pass
                else:
                    query_c = Guia.objects.filter(guia__exact=var_guia)
                    correo_r = query_c[0].email_r
                    SendCorreo(sndemail=correo_r, msjhtml='Su envío se encuentra en proceso de entrega en la ciudad de destino.')
                    correo_d = query_c[0].email_d
                    SendCorreo(sndemail=correo_d, msjhtml='Su envío se encuentra en proceso de entrega en la ciudad de destino.')
                    Guia.objects.filter(guia__exact=var_guia).update(smail=True)
                success_message = "El Bulto ya fue descargado Correctamente - Escanee otro Código!"
                return HttpResponseRedirect(self.get_success_url(success_message))
        except Exception as e:
            success_message = "Error al descargar el Bulto!!" + str(e)
            return HttpResponseRedirect(self.get_success_url(success_message))
    def get_success_url(self, success_message):
        messages.success(self.request, (success_message))
        return reverse("descargar")
#
#  name: EntregarBulto 
#
class EntregarBulto(SuccessMessageMixin, View):
    model = Bulto
    def get(self, request, *args, **kwargs):
        today = str(datetime.now())
        query = self.request.GET.get("q")
        try:
            query_a = Bulto.objects.filter(id_bulto__icontains=query)
            valor_0 = query_a[0].estado
            var_guia = query_a[0].guias
            query_m = Guia.objects.filter(guia__exact=var_guia)
            cantidad_guia = query_m[0].cantidad
            if valor_0 == '2':
                if int(cantidad_guia) <= 50:
                    Bulto.objects.filter(id_bulto__icontains=query).update(estado="3", modified=today)
                else:
                    Bulto.objects.filter(guias__exact=var_guia).update(estado="3", modified=today)
                count_bultos = CountBultos(num_guia=var_guia, estado="2")
                if count_bultos == 0:
                    if ValThirdMail(num_guia=var_guia):
                        pass
                    else:
                        query_c = Guia.objects.filter(guia__exact=var_guia)
                        correo_r = query_c[0].email_r
                        SendCorreo(sndemail=correo_r, msjhtml='Su envío fue entregado al Cliente.')
                        Guia.objects.filter(guia__exact=var_guia).update(tmail=True)
                        Guia.objects.filter(guia__exact=var_guia).update(estado="I")
                success_message = "Bulto entregado Correctamente!"
                return HttpResponseRedirect(self.get_success_url(success_message))
            else:
                if ValThirdMail(num_guia=var_guia):
                    pass
                else:
                    query_c = Guia.objects.filter(guia__exact=var_guia)
                    correo_r = query_c[0].email_r
                    SendCorreo(sndemail=correo_r, msjhtml='Su envío fue entregado al Cliente.')
                    Guia.objects.filter(guia__exact=var_guia).update(tmail=True)
                    Guia.objects.filter(guia__exact=var_guia).update(estado="I")
                success_message = "El Bulto ya fue entregado Correctamente - Escanee otro Código!"
                return HttpResponseRedirect(self.get_success_url(success_message))
        except Exception as e:
            success_message = "Error al entregar el Bulto!!" + str(e)
            return HttpResponseRedirect(self.get_success_url(success_message))
    def get_success_url(self, success_message):
        messages.success(self.request, (success_message))
        return reverse("entregar")
#
# Function : SendCorreo
#
def SendCorreo(sndemail, msjhtml):
    try:
        email = sndemail
        message = MIMEMultipart('alternative')
        message['Subject'] = 'Notificación de su envío por FLETES GAG'
        message['From'] = settings.EMAIL_HOST_USER
        message['To'] = email
        html = msjhtml
        content = MIMEText(html, 'plain')
        message.attach(content)
        server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
        server.starttls()
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
        server.sendmail(
            settings.EMAIL_HOST_USER, email, message.as_string()
        )
        server.quit()
    except Exception as e:
        print(str(e))
#
# Function : ValFirstMail
#
def ValFirstMail(num_guia):
    query = Guia.objects.filter(guia__exact=num_guia)
    val_fmail = query[0].fmail
    if val_fmail == True:
        return True
    else:
        return False
#
# Function : ValSecondMail
#
def ValSecondMail(num_guia):
    query = Guia.objects.filter(guia__exact=num_guia)
    val_smail = query[0].smail
    if val_smail == True:
        return True
    else:
        return False
#
# Function : ValThirdMail
#
def ValThirdMail(num_guia):
    query = Guia.objects.filter(guia__exact=num_guia)
    val_tmail = query[0].tmail
    if val_tmail == True:
        return True
    else:
        return False
#
# Function : CountBultos
#
def CountBultos(num_guia, estado):
    query = Bulto.objects.filter(Q(guias__icontains=num_guia) & Q(estado=estado))
    total = query.count()
    return total
