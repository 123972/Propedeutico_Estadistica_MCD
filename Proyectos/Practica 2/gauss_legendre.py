import math
import numpy as np

def n_0(limInf,limSup,funcion):
    pesos = np.array([2])
    nodos = np.array([0])
    sumatoria = pesos[0]*(funcion((1/2)*(((limSup-limInf)*nodos[0])+limInf+limSup)))
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def n_1(limInf,limSup,funcion):
    pesos = np.array([1,1])
    nodos = np.array([-np.sqrt(1/3),np.sqrt(1/3)])
    sumatoria = 0
    i = 0
    while i<len(pesos):
        sumatoria = sumatoria + (pesos[i]*(funcion((1/2)*(((limSup-limInf)*nodos[i])+limInf+limSup))))
        i = i + 1
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def n_2(limInf,limSup,funcion):
    pesos = np.array([5/9,8/9,5/9])
    nodos = np.array([-np.sqrt(3/5),0,np.sqrt(3/5)])
    sumatoria = 0
    i = 0
    while i<len(pesos):
        sumatoria = sumatoria + (pesos[i]*(funcion((1/2)*(((limSup-limInf)*nodos[i])+limInf+limSup))))
        i = i + 1
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def n_3(limInf,limSup,funcion):
    pesos = np.array([0.347855,0.652145,0.652145,0.347855])
    nodos = np.array([-0.861136,-0.339981,0.339981,0.861136])
    sumatoria = 0
    i = 0
    while i<len(pesos):
        sumatoria = sumatoria + (pesos[i]*(funcion((1/2)*(((limSup-limInf)*nodos[i])+limInf+limSup))))
        i = i + 1
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def n_4(limInf,limSup,funcion):
    pesos = np.array([0.236927,0.478629,0.568889,0.478629,0.236927])
    nodos = np.array([-0.90618,-0.538469,0,0.538469,0.90618])
    sumatoria = 0
    i = 0
    while i<len(pesos):
        sumatoria = sumatoria + (pesos[i]*(funcion((1/2)*(((limSup-limInf)*nodos[i])+limInf+limSup))))
        i = i + 1
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def default():
    return "Opcion Invalida"

def calcula_gauss_legendre(n, limInf, limSup, funcion):
    gl = {
        0: n_0(limInf,limSup,funcion),
        1: n_1(limInf,limSup,funcion),
        2: n_2(limInf,limSup,funcion),
        3: n_3(limInf,limSup,funcion),
        4: n_4(limInf,limSup,funcion),
    }
    return gl.get(n, default())
