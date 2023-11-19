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
from django.db import models
from crum import get_current_user
from django.utils import timezone
from django.utils.html import format_html
#
from .morigen import Origen
#
# Class : Cliente
#
class Cliente(models.Model):
    # Tipo de Persona
    TIPOPERSONA_CHOICES = [
        ('V','Natural'),
        ('J','Jurídica')
    ]
    # Id del Cliente
    id_cliente = models.IntegerField(
        primary_key=True,
        verbose_name=u"Cédula",
        help_text=u"Por favor ingrese solo el número")
    # Selecciona el tipo
    tipo_persona = models.CharField(
        max_length=1,
        choices=TIPOPERSONA_CHOICES,
        verbose_name=u"Tipo de persona",
        help_text=u"Por favor seleccione el tipo")
    # Nombre
    nombre = models.CharField(
        max_length=200,
        verbose_name=u"Nombre")
    # Celular
    celular = models.CharField(
        max_length=45,
        null=True, 
        blank=True,
        default='(0424)-000-00.00',
        verbose_name=u"Celular",
        help_text=u"Por favor ingrese el celular parecido al ejemplo")
    # Telefono
    telefono = models.CharField(
        max_length=45,
        null=True, 
        blank=True,
        default='(0212)-000-00.00',
        verbose_name=u"Teléfono",
        help_text=u"Por favor ingrese el teléfono parecido al ejemplo")
    # Relacion con Origen
    origen = models.ForeignKey(
        Origen,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=u"Sucursal",
        related_name='origen_cliente',
        db_column='origen')
    # Modificado fecha actual
    modified = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=u"Modificado")
    # Modificado por
    modified_by = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        default=None,
        on_delete=models.DO_NOTHING,
        related_name='cliente_modified_by',
        verbose_name=u"Modificado por",
        db_column='modified_by')
    # Creado campo de fecha automatico fecha actual
    created = models.DateTimeField(auto_now_add=True, verbose_name=u"Creado")
    # Creado por
    created_by = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        default=get_current_user,
        on_delete=models.DO_NOTHING,
        related_name='cliente_create_by',
        verbose_name=u"Creado por",
        db_column='created_by')
    #
    # Colored Fields
    #
    def col_modified(self):
        return format_html(
            '<span style="color: #0091EA;">{0}</span>',
            self.modified
        )
    col_modified.short_description = 'Modificado el'

    def col_modified_by(self):
        return format_html(
            '<span style="color: #F57C00;">{0}</span>',
            self.modified_by
        )
    col_modified_by.short_description = 'Modificado por'

    def col_created(self):
        return format_html(
            '<span style="color: #0091EA;">{0}</span>',
            self.created
        )
    col_created.short_description = 'Creado el'

    def col_created_by(self):
        return format_html(
            '<span style="color: #558B2F;">{0}</span>',
            self.created_by
        )
    col_created_by.short_description = 'Creado por'
    #
    # Save method :
    #
    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        self.modified = timezone.now()
        return super(Cliente, self).save(*args, **kwargs)
    #
    # Meta and String
    #
    def NombreCliente(self):
       cadena = "{0} - {1}"
       return cadena.format(self.id_cliente, self.nombre)
    
    def __str__(self):
        return self.NombreCliente()

    class Meta:
        db_table ='cliente'
        ordering = ['id_cliente']
        indexes = [ models.Index(fields = ['id_cliente']),]
