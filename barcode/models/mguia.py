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
from django.core.validators import RegexValidator
from django.forms import model_to_dict
#
#from .mremitente import Remitente
#from .mdestinatario import Destinatario
from .mcliente import Cliente
from .morigen import Origen
from .mdestino import Destino
from .mruta import Ruta
#  
#  name: class Guia
#  
class Guia(models.Model):
    # Estados de la Guia
    ESTADO_CHOICES= [
        ('A','Activa'),
        ('I','Inactiva')
    ]
    # Guía
    guia = models.CharField(
        unique=True,
        max_length=10,
        null=True,
        blank=True,
        validators=[RegexValidator(r'^\d{1,10}$')],
        verbose_name=u"Número de Guía", 
        help_text=u"Por favor ingrese solo el número")
    # Recolecta
    recolecta = models.CharField(
        unique=True,
        max_length=10,
        null=True,
        blank=True,
        validators=[RegexValidator(r'^\d{1,10}$')],
        verbose_name=u"Número de Recolecta", 
        help_text=u"Por favor ingrese solo el número")
    # Estado de la Guía
    estado = models.CharField(
        max_length=1,
        default='A',
        choices=ESTADO_CHOICES,
        verbose_name=u"Estado",
        help_text=u"Por favor seleccione el estado de la guía")
    # Cantidad
    cantidad = models.CharField(
        max_length=4,
        validators=[RegexValidator(r'^\d{1,4}$')],
        verbose_name=u"Cantidad de Bultos/Paquetes", 
        help_text=u"Por favor ingrese solo el número")
    # Id del Remitente Relacion
    remitente = models.ForeignKey(
        Cliente,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=u"Remitente",
        related_name='remitente_guia',
        db_column='remitente')
    # Email-Remitente
    email_r = models.EmailField(
        max_length=254,
        null=True, 
        blank=True,
        default='Cliente@email.com',
        verbose_name=u"Email Remitente",
        help_text=u"Por favor ingrese el email parecido al ejemplo")
    # Id del Destinatario Relacion
    destinatario = models.ForeignKey(
        Cliente,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=u"Destinatario",
        related_name='destinatario_guia',
        db_column='destinatario')
    # Email-Destinatario
    email_d = models.EmailField(
        max_length=254,
        null=True, 
        blank=True,
        default='Cliente@email.com',
        verbose_name=u"Email Destinatario",
        help_text=u"Por favor ingrese el email parecido al ejemplo")
    # Relacion con Ruta
    ruta = models.ForeignKey(
        Ruta,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=u"Ruta",
        related_name='ruta_guia',
        db_column='ruta')
    # Relacion con Origen
    origen = models.ForeignKey(
        Origen,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=u"Sucursal - Origen",
        related_name='origen_guia',
        db_column='origen')
    # Relacion con Destino
    destino = models.ForeignKey(
        Destino,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=u"Destino",
        related_name='destino_guia',
        db_column='destino')
    # Primer Email
    fmail = models.BooleanField(
        null=True,
        blank=True,
        default=False, 
        verbose_name=u"F-Mail")
    # Segundo Email
    smail = models.BooleanField(
        null=True,
        blank=True,
        default=False, 
        verbose_name=u"S-Mail")
    # Tercero Email
    tmail = models.BooleanField(
        null=True,
        blank=True,
        default=False, 
        verbose_name=u"T-Mail")
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
        related_name='guia_modified_by',
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
        related_name='guia_create_by',
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
        return super(Guia, self).save(*args, **kwargs)
    #
    # Meta and String
    #
    def __str__(self):
        cadena = "{0} - {1} - {2} - {3} - {4} - {5} - {6} - {7}"
        return cadena.format(self.id, self.guia, self.recolecta, self.estado, self.cantidad, self.origen, self.destino, self.ruta)
    class Meta:
        db_table ='guia'
        ordering = ['id']
        #indexes = [ models.Index(fields = ['id', 'guia', 'recolecta']),]
