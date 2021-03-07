"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 28 May 2020
--  Description: acliente.py
--
--
======================================================================================
"""
#
# Imports :
#
from django.contrib import admin
from barcode.models.mcliente import *
#
#  name: class cliente Admin
#
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'id_cliente',
        'tipo_persona',
        'nombre',
        'celular',
        'telefono',
        'origen',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['id_cliente']
    empty_value_display = '-empty-'
admin.site.register(Cliente, ClienteAdmin)