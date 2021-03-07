"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 29 May 2020
--  Description: fguia.py
--
--
======================================================================================
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