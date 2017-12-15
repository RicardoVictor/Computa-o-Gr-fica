#from Vertice import Vertice

#retorna vetor unitario
def normalizar(vetor):
    mod_vetor = modulo(vetor)
    vetor[0] /= mod_vetor
    vetor[1] /= mod_vetor
    vetor[2] /= mod_vetor

    return vetor

#retorna o modulo de um vetor
def modulo(vetor):
    return (vetor[0]**2 + vetor[1]**2 + vetor[2]**2)**0.5

#retorna o produto escalar de 2 vetores do tipo list
def produto_escalar(vetor1, vetor2):
    return vetor1[0] * vetor2[0] + vetor1[1] * vetor2[1] + vetor1[2] * vetor2[2]
    
#retorna o produto vetorial de 2 vetores
def produto_vetorial():
    pass