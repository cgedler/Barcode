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
