import numpy as np
import sys

def criaMatriz(instancia):
    caminho = rf'C:\Users\55199\Desktop\CMAC03 - ALGORITMOS EM GRAFOS\prototipo\instancias\{instancia}.txt'
    with open(caminho, 'rb') as f:
        mat = np.loadtxt(f)
    return mat

def resultado(mat):
    r = str(instancia) + str(mat.shape)
    return r

def salvaResultado(r):
    arq = open(rf'C:\Users\55199\Desktop\CMAC03 - ALGORITMOS EM GRAFOS\prototipo\resultado.txt','w')
    arq.writelines(r + "\n")
    arq.close()

if __name__ == "__main__":
    instancia = sys.argv[1]
    matriz = criaMatriz(instancia)
    res = resultado(matriz)
    salvaResultado(res)
