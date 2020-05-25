# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:17:50 2020

@author: booed_000
"""
"""Ejercicios 1.3"""
"""1.3.1 funcion playera"""
def Hacer_Playera(talla, texto):
    print("Que sea de talla, " + talla + " mi playera.")
    print('Que diga, "' + texto + '"')
Hacer_Playera('Grande', 'Quiero pasar programacion avanzada')

print(" ")

"""1.3.2 tamaño y texto predeterminado"""

def Hacer_Playera(talla='Grande', texto='I love Python!'):
    print("Que sea talla " + talla + " mi camisa.")
    print('Que diga, "' + texto + '"')
Hacer_Playera()
Hacer_Playera(talla='Mediana')
Hacer_Playera('Chica', 'Arriba la programacion.')

print(" ")

"""1.3.3 Ciudades"""
def Descripcion_Ciudad(ciudad, pais='Mexico'):
    mensaje = ciudad.title() + " esta en " + pais + "."
    print(mensaje)
Descripcion_Ciudad('cdmx')
Descripcion_Ciudad('madrid', 'España')
Descripcion_Ciudad('puebla')