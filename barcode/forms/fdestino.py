"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 29 May 2020
--  Description: fdestino.py
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
from barcode.models.mdestino import Destino
#
#  name: class DestinoForm
#
class DestinoForm(forms.ModelForm):
    class Meta:
        model = Destino
        fields = ['id_destino', 'nombre', 'rutas']

    def __init__(self, *args, **kwargs):
        super(DestinoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })