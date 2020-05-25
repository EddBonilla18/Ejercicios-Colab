# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:05:47 2020

@author: booed_000
"""

def Menu():
    """Funcion que Muestra el Menu"""
    print """************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir"""
def Calculadora():
    """Funcion Para Calcular Operaciones Aritmeticas"""
    Menu()
    opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        num1 = int(input("Ingrese Numero\n"))
        num2 = int(input("Ingrese Otro Numero\n"))
        if (opc==1):
            print "La Suma es:", num1+num2
            opc = int(input("Selecione Opcion\n"))
        elif(opc==2):
            print "La Resta es:",num1-num2
            opc = int(input("Selecione Opcion\n"))
        elif(opc==3):
            print "La Multiplicacion es:",num1*num2
            opc = int(input("Selecione Opcion\n"))
        elif(opc==4):
            try:
              print "La Division es:", num1/num2
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError:
              print "No se Permite la Division Entre 0"
              opc = int(input("Selecione Opcion\n"))
Calculadora()


"""1.6.2 piramide de numeros"""
print("Ingrese el numero de filas para la piramide")
num = input()

for i in range(num):
  # print(i)
  print(' ' * (num - i - 1) + "*" * (2 * i + 1))
  

  
