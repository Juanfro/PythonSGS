'''
Created on 8 feb. 2019

@author: Juan Antonio Rodríguez
'''
from random import random, randint

""" Ejercicio 1
Escribe un programa que te permita jugar a una versión simplificada del juego Master Mind.
El juego consistirá en adivinar una cadena de números distintos. Al principio, el programa
debe pedir la longitud de la cadena (de 2 a 9 cifras). Después el programa debe ir pidiendo que
intentes adivinar la cadena de números. En cada intento, el programa informará de cuántos
números han sido acertados (el programa considerará que se ha acertado un número si
coincide el valor y la posición).
"""

fin = False

lista = []
listaUsuario = []


def mastermind():
    longitud = int(input("Elige la longitud de la lista de numeros\n"))
    # lista = []
    listaIncognito = []
    
    for x in range(longitud):
        lista.append(randint(0, 9))
        listaIncognito.append("?")
        
    print("DEBUG", lista)
    # print("DEBUG", listaIncognito)
    
    adivinar(longitud)

    
def adivinar(longitud):
    fin = False
    while not fin:
        
        print("Escribe", longitud, "numeros")
        listaUsuario.clear()
        
        contador = 0        
        while (contador) < longitud:
            print("Escribe el numero " , contador + 1)            
            numeroInput = input("")           
            numero = int(numeroInput)
            listaUsuario.append(numero)
           
            contador += 1
        
        print(listaUsuario)
        
        if(listaUsuario == lista):
            print("Has ganado")
            fin = True;
        else:
            print("has acertado", calcular_aciertos())
            print("Intentalo de nuevo")

            
def calcular_aciertos():
   
    aciertos = 0
    for x in range(len(lista)):
        if (lista[x] == listaUsuario[x]):
            aciertos += 1
    return aciertos

    
mastermind()

"""Ejercicio2
Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas
letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman
un poco y si no, que no riman.
"""


def rima():
    
    print("Ejercicio 2")
    
    palabra1 = input("Escribe la primera palabra\n")
    palabra2 = input("Escribe la segunda palabra\n")
    
    fin1 = palabra1[(len(palabra1) - 3):]
    fin2 = palabra2[(len(palabra2) - 3):]
    
    if fin1 == fin2:
        print(palabra1, "rima con", palabra2)
    elif ((fin1[1:]) == (fin2[1:])):
        print(palabra1, "rima un poco con", palabra2)
    else:
        print(palabra1, "no rima con", palabra2)


rima()
"""Ejercicio 3
Haz un programa que pida al usuario una cantidad de euros, una tasa de interés y un número
de años. Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos
esos años si cada año se aplica la tasa de interés introducida.

Recordar que un capital C de euros a un interés del x por cien durante n años se convierte en
C * (1 + x/100)n
(años). Probar el programa sabiendo que una cantidad de 10000 euros al 4.5%
de interés anual se convierte en 24117.14 euros al cabo de 20 años.
"""


def capital():
    capital = int(input("Escribe tu capital\n"))
    capitalInicial = capital
    interes = int(input("Escribe el interés\n"))
    duracion = int(input("Escribe la duracioión\n"))
    
    for x in range(duracion):
        capital = capital * (1 + (interes / 100))
        
    print("En", duracion, "años", capitalInicial, "con un interés de", interes, "se convierte en", capital)
    
    
capital()
