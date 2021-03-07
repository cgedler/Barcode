"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 28 May 2020
--  Description: mdestino.py
--
--  
======================================================================================
"""
#
# Imports :
#
from django.db import models
from crum import get_current_user
from django.utils import timezone
from django.utils.html import format_html
from django.forms import model_to_dict
#
from .mruta import Ruta
#  
#  name: class Destino
#  
class Destino(models.Model):
    # Id del Destino
    id_destino = models.CharField(
        max_length=3, 
        primary_key=True, 
        default='D01', 
        verbose_name=u'Código del Destino', 
        help_text=u'Por favor ingrese el código parecido al ejemplo') 
    # Nombre del Cargo
    nombre = models.CharField(
        max_length=150,
        null=True, 
        blank=True,
        verbose_name=u'Nombre del Destino')
    # Relacion con Origen
    rutas = models.ForeignKey(
        Ruta,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=u'Ruta',
        related_name='ruta_destino',
        db_column='ruta')
    # Modificado fecha actual
    modified = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=u'Modificado')
    # Modificado por
    modified_by = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        default=None,
        on_delete=models.DO_NOTHING,
        related_name='Destino_modified_by',
        verbose_name=u'Modificado por',
        db_column='modified_by')
    # Creado campo de fecha automatico fecha actual
    created = models.DateTimeField(auto_now_add=True, verbose_name=u'Creado')
    # Creado por
    created_by = models.ForeignKey(
        'auth.User',
        blank=True,
        null=True,
        default=get_current_user,
        on_delete=models.DO_NOTHING,
        related_name='Destino_create_by',
        verbose_name=u'Creado por',
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
        return super(Destino, self).save(*args, **kwargs)
    #
    # Meta and String
    #
    def __str__(self):
        cadena = "{0} - {1}"
        return cadena.format(self.id_destino, self.nombre)
    
    class Meta:
        db_table = 'destino'
        ordering = ['id_destino']
