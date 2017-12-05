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

#retorna o produto escalar de 2 vetores
def produto_escalar():
    pass

#retorna o produto vetorial de 2 vetores
def produto_vetorial():
    pass