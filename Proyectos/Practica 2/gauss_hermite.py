import math
import numpy as np

def n_1(limInf,limSup,funcion):
    pesos = np.array([0.886227,0.886227])
    nodos = np.array([-0.707107,0.707107])
    sumatoria = 0
    i = 0
    while i<len(pesos):
        sumatoria = sumatoria + (pesos[i]*(funcion((1/2)*(((limSup-limInf)*nodos[i])+limInf+limSup))))
        i = i + 1
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def n_2(limInf,limSup,funcion):
    pesos = np.array([0.295409,1.181636,0.295409])
    nodos = np.array([-1.224745,0,1.224745])
    sumatoria = 0
    i = 0
    while i<len(pesos):
        sumatoria = sumatoria + (pesos[i]*(funcion((1/2)*(((limSup-limInf)*nodos[i])+limInf+limSup))))
        i = i + 1
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def n_3(limInf,limSup,funcion):
    pesos = np.array([0.0813128,0.804914,0.804914,0.0813128])
    nodos = np.array([-1.650680,-0.524648,0.524648,1.650680])
    sumatoria = 0
    i = 0
    while i<len(pesos):
        sumatoria = sumatoria + (pesos[i]*(funcion((1/2)*(((limSup-limInf)*nodos[i])+limInf+limSup))))
        i = i + 1
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def n_4(limInf,limSup,funcion):
    pesos = np.array([0.0199532,0.0393619,0.945308,0.0393619,0.0199532])
    nodos = np.array([-2.020183,-0.958572,0,0.958572,2.020183])
    sumatoria = 0
    i = 0
    while i<len(pesos):
        sumatoria = sumatoria + (pesos[i]*(funcion((1/2)*(((limSup-limInf)*nodos[i])+limInf+limSup))))
        i = i + 1
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def n_5(limInf,limSup,funcion):
    pesos = np.array([0.00453001,0.157067,0.724629,0.724629,0.157067,0.00453001])
    nodos = np.array([-2.350605,-1.335849,-0.436077,0.436077,1.335849,2.350605])
    sumatoria = 0
    i = 0
    while i<len(pesos):
        sumatoria = sumatoria + (pesos[i]*(funcion((1/2)*(((limSup-limInf)*nodos[i])+limInf+limSup))))
        i = i + 1
    resultado = ((limSup-limInf)/2)*sumatoria
    return resultado

def default():
    return "Opcion Invalida"

def calcula_gauss_hermite(n, limInf, limSup, funcion):
    gl = {
        1: n_1(limInf,limSup,funcion),
        2: n_2(limInf,limSup,funcion),
        3: n_3(limInf,limSup,funcion),
        4: n_4(limInf,limSup,funcion),
        5: n_5(limInf,limSup,funcion),
    }
    return gl.get(n, default())
