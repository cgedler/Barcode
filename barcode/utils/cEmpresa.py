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
import os
import io
import json
#
# Class : Empresa
#
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#
class EmpresaDatos(object):
    # Atributos:
    def __init__(self):
        json_data = os.path.join(BASE_DIR, 'JSON/Empresa.json')
        with open(json_data) as json_file:
            data = json.load(json_file)
        for p in data['empresa']:
            self.nombre = p['nombre']
            self.rif = p['rif']
            self.celular = p['celular']
            self.telefono = p['telefono']
            self.email =  p['email']
            self.dir_estado = p['direstado']
            self.dir_ciudad = p['dirciudad']
            self.dir_municipio = p['dirmunicipio']
            self.dir_parroquia = p['dirparroquia']
            self.direccion = p['direccion']
            self.website =  p['website']
            self.postal = p['postal']
            self.notas = p['notas']      
    # Metodos :
    # str
    def __str__(self):
        cadena = self.rif + ", " + self.nombre
        return cadena
