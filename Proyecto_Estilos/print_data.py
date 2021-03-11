#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
from IPython.display import display

#Departamentos de Colombia
deptos = {
    '0' : 'Amazonas', '1' : 'Antioquia', '2' : 'Arauca', '3' : 'Atlántico',
    '4' : 'Bogotá D.C.', '5' : 'Bolívar', '6' : 'Boyacá', '7' : 'Caldas',
    '8' : 'Caquetá', '9' : 'Casanare',  '10' : 'Cauca', '11' : 'Cesar', 
    '12' : 'Chocó', '13' : 'Córdoba', '14' : 'Cundinamarca', '15' : 'Guainía',
    '16' : 'Huila', '17' : 'La Guajira', '18' : 'Magdalena', '19' : 'Meta', 
    '20' : 'Nariño', '21' : 'Norte de Santander', '22' : 'Putumayo', '23' : 'Quindío',
    '24' : 'Risaralda',  '25' : 'Archipiélago de San Andrés Providencia y Santa Catalina', 
    '26' : 'Santander', '27' : 'Sucre', '28' : 'Tolima', '29' : 'Valle del Cauca',
    '30' : 'Vaupés', '31' : 'Vichada', '32' : 'SALIR'
}

def printdeptos():
    print("{:<10} {:<20}".format("Código", "Nombre departamento"))
    for i in deptos: 
        print ("{:<10} {:<20}".format(i, deptos.get(i)))

#Dar formato a los datos cuando salen como lista
def displaylist(registros):
    print("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format("Ciudad", "Departamento", "Edad", "Tipo", "Estado", "Pais de procedencia"))
    for i in registros: 
        out = "{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}".format(i.get_ciudad(), i.get_departamento(), i.get_edad(), i.get_tipo(), i.get_estado(), i.get_pais_procedencia())
        print(out)

#Imprimir la información como dataframe 
def displaydf(dataframe, cols = None, rows = None):
    dataframe = dataframe[['ciudad_de_ubicaci_n', 'departamento', 'edad', 'tipo', 'estado', 'pa_s_de_procedencia']]
    with pd.option_context("display.max_columns", cols):
        with pd.option_context("display.max_rows", rows):
            display(dataframe)
    return True