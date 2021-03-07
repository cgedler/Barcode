"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 04 Junio 2020
--  Description: ausersuc.py
--
--  script file that 
======================================================================================
"""
#
# Imports :
#
from django.contrib import admin
from barcode.models.musersuc import *
#
#  name: class USucursal Admin
#
class USucursalAdmin(admin.ModelAdmin):
    list_display = (
        'usuario',
        'sucursal',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
admin.site.register(USucursal, USucursalAdmin)