"""
======================== Copyright 2020 CORPYGEDLER ==================================
--  Author: Christopher Gedler <cgedler@gmail.com;cge.systemsolutions@gmail.com>
--  Create date: 30 Abril 2020
--  Description: cEmpresa.py
--
--  script file return object Empresa with data
======================================================================================
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