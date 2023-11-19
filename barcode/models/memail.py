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
from .mcliente import Cliente
#  
#  name: class Email
#  
class Email(models.Model):
    # Id del Cliente Relacion
    email_cliente = models.ForeignKey(
        Cliente,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        verbose_name=u"Cliente",
        related_name='cliente_email',
        db_column='cliente')
    # Email
    email = models.EmailField(
        unique=True,
        max_length=254,
        null=True, 
        blank=False,
        default='Cliente@email.com',
        verbose_name=u"Email",
        help_text=u"Por favor ingrese el email parecido al ejemplo")
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
        related_name='email_modified_by',
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
        related_name='email_create_by',
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
        return super(Email, self).save(*args, **kwargs)
    #
    # Meta and String
    #
    def __str__(self):
        cadena = "{0} - {1}"
        return cadena.format(self.id, self.email)
    class Meta:
        db_table ='email'
        ordering = ['id']
