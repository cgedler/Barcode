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
from django.contrib import admin
from barcode.models.morigen import *
#
#  name: class Origen Admin
#
class OrigenAdmin(admin.ModelAdmin):
    list_display = (
        'id_origen',
        'nombre',
        'col_modified',
        'col_modified_by',
        'col_created',
        'col_created_by',
    )
    search_fields = ['nombre']
    empty_value_display = '-empty-'
admin.site.register(Origen, OrigenAdmin)
