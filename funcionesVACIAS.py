from principal import *
from configuracion import *
from funcionesSeparador import *

import random
import math

def lectura(archivo, lista):
    f=archivo.readlines()
    for linea in f:
        lista.append(linea)


def actualizar(silabasEnPantalla,posiciones,listaDeSilabas):
    silaba=nuevaSilaba(listaDeSilabas)
    silabasEnPantalla.append(silaba)
    x=random.randrange(0,ANCHO-20)
    y=0
    pos=[x,y]
    posiciones.append(pos)



def nuevaSilaba(silabas):
    n=random.randrange(len(silabas))
    pal=silabas[n]
    return pal.lower()

def quitar(candidata, silabasEnPantalla, posiciones):
    pass

def dameSilabas(candidata):
    pass


def esValida(candidata, silabasEnPantalla, lemario):
    pass

def Puntos(candidata):
        pass

def procesar(candidata, silabasEnPantalla, posiciones, lemario):
    pass
