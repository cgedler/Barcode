"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 28 May 2020
--  Description: aruta.py
--
--
======================================================================================
"""
#
# Imports :
#
from django.contrib import admin
from barcode.models.mruta import *
#
#  name: class Ruta Admin
#
class RutaAdmin(admin.ModelAdmin):
    list_display = (
        'id_ruta',
        'nombre',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['nombre']
    empty_value_display = '-empty-'
admin.site.register(Ruta, RutaAdmin)