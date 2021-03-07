"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 16 Septiembre 2020
--  Description: femail.py
--
--  script file that 
======================================================================================
"""
#
# Imports :
#
from django import forms
from django.forms import ModelForm
from django.forms import Textarea, CharField, TextInput, ChoiceField, Select, NumberInput, EmailInput
from barcode.models.memail import Email
from barcode.models.mcliente import Cliente
#
# Class : Email_Form
#
class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email_cliente', 'email']
        widgets = {
            'email_cliente': Select(attrs={'id':'email_cliente'}),
            #'email': EmailInput(attrs=={'id':'email'}),

        }

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
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
        except Exception as e:
            data['errors'] = str(e)
        return data