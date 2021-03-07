"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 15 Septiembre 2020
--  Description: aemail.py
--
--  script file that 
======================================================================================
"""
#
# Imports :
#
from django.contrib import admin
from barcode.models.memail import *
#
#  name: class cliente Admin
#
class EmailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_cliente',
        'email',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['id']
    empty_value_display = '-empty-'
admin.site.register(Email, EmailAdmin)