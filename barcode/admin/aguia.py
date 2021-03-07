"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 28 May 2020
--  Description: aguia.py
--
--
======================================================================================
"""
#
# Imports :
#
from django.contrib import admin
from barcode.models.mguia import *
#
#  name: class Guia Admin
#
class GuiaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'guia',
        'recolecta',
        'estado',
        'cantidad',
        'remitente',
        'destinatario',
        'ruta',
        'origen',
        'destino',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['id']
    empty_value_display = '-empty-'
admin.site.register(Guia, GuiaAdmin)