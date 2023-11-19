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
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField, Select, NumberInput
from barcode.models.mguia import Guia
from barcode.models.mcliente import Cliente
from barcode.models.morigen import Origen
from barcode.models.musersuc import USucursal
from barcode.models.mdestino import Destino
from barcode.models.mruta import Ruta
import json
#
#  name: class GuiaForm
#
class GuiaForm(forms.ModelForm):
    class Meta:
        model = Guia
        fields = ['guia', 'recolecta', 'cantidad', 'origen', 'ruta', 'remitente', 'email_r', 'destinatario', 'email_d', 'destino']
        widgets = {
            'remitente': Select(attrs={'id':'remitente'}),
            'email_r': Select(attrs={'id':'email_r'}),
            'email_d': Select(attrs={'id':'email_d'}),
            'destinatario': Select(attrs={'id':'destinatario'})
        }
        
    def __init__(self, *args, **kwargs):
        super(GuiaForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['errors'] = form.errors
                #print('error' + data)
        except Exception as e:
            data['errors'] = str(e)
        return data

#
#  name: class GuiaForm
#
class GuiaDForm(forms.ModelForm):
    class Meta:
        model = Guia
        fields = ['guia', 'recolecta', 'cantidad', 'origen', 'ruta', 'remitente', 'destinatario', 'destino']
    def __init__(self, *args, **kwargs):
        super(GuiaDForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
