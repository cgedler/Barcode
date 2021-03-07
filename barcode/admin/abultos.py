"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 28 May 2020
--  Description: abultos.py
--
-- 
======================================================================================
"""
#
# Imports :
#
from django.contrib import admin
from barcode.models.mbultos import *
#
#  name: class Bultos Admin
#
class BultoAdmin(admin.ModelAdmin):
    list_display = (
        'id_bulto',
        'guias',
        'recolecta',
        'estado',
        'origen',
        'ruta',
        'destino',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['guias']
    empty_value_display = '-empty-'
admin.site.register(Bulto, BultoAdmin)