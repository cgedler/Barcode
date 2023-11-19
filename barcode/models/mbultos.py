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
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import model_to_dict
#
from .mguia import Guia
#
# Class : Bultos
#
class Bulto(models.Model):
    # Estados de la Guia
    ESTADO_CHOICES= [
        ('0','Lugar de Origen'),
        ('1','Viajando'),
        ('2','Lugar de Destino'),
        ('3','Entregado')
    ]
    # Id del Bulto
    id_bulto = models.CharField(
        max_length=20, 
        #primary_key=True, 
        verbose_name=u"Código del Bulto", 
        help_text=u"Por favor ingrese el código parecido al ejemplo")
    # Relacion con Guía
    guias = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name=u"N# Guía",
        db_column='guia_bulto')
    # Relacion con  Recolecta
    recolecta = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        verbose_name=u"N# Recolecta", 
        db_column='recolecta_bulto')
    # Estado del Bulto
    estado = models.CharField(
        max_length=1,
        choices=ESTADO_CHOICES,
        verbose_name=u"Estado",
        help_text=u"Por favor seleccione donde se encuentra el Bulto")
    # Relacion con Origen
    origen = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name=u"Origen",
        db_column='origen')
    # Relacion con Ruta
    ruta = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name=u"Ruta",
        db_column='ruta')
    # Relacion con Destino
    destino = models.CharField(
        max_length=40,
        null=True,
        blank=True,
        verbose_name=u"Destino",
        db_column='destino')
    # Relacion con Destinatario
    destinatario = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=u"Destinatario",
        db_column='destinatario')
    # Relacion con Camión
    camion = models.CharField(
        max_length=55,
        null=True,
        blank=True,
        verbose_name=u"Camión",
        db_column='camion')
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
        related_name='bulto_modified_by',
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
        related_name='bulto_create_by',
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
        return super(Bulto, self).save(*args, **kwargs)
    #
    # Meta and String
    #
    def __str__(self):
        cadena = "{0} - {1} - {2} - {3} - {4} - {5} - {6}"
        return cadena.format(self.id_bulto, self.guias, self.recolecta, self.estado, self.origen, self.destino, self.ruta)
    #
    class Meta:
        db_table ='bultos'
        ordering = ['id_bulto']
        indexes = [ models.Index(fields = ['id_bulto', 'guias', 'recolecta']),]

@receiver(post_save, sender=Guia)
def create_bulto(sender, instance, **kwargs):
    if kwargs['created']:
        i = int(instance.cantidad)
        co = str(instance.origen)
        cod_origen = co[0:3]
        cd = str(instance.destino)
        cod_destino = cd[0:3]
        cod_ruta = str(instance.ruta)
        idguia = str(instance.id)
        numero = str(instance.guia)
        recolecta = str(instance.recolecta)
        destinatario = str(instance.destinatario)
        for x in range(i):
            y = x + 1
            z = str(y)
            result = z.zfill(4)
            #numero_guia = numero.zfill(10)
            numero_guia = idguia.zfill(10)
            #print(numero_guia)
            # make Barcode
            codigo = cod_origen + cod_destino + numero_guia + result
            # Insert bulto
            new_bulto = Bulto.objects.create(id_bulto=codigo, guias=numero, recolecta=recolecta, estado='0', origen=co, ruta=cod_ruta, destino=cd, destinatario=destinatario) 
            new_bulto.save()

