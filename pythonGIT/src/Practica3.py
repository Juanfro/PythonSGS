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
    #print("DEBUG", listaIncognito)
    
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
