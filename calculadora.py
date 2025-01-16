def soma(a,b):
    return a + b

def dividir(a,b):
    if b!=0:
        return a/b
    else:
        return "Não é um numero"

def multiplicar(a, b):
    valor = a * b
    if a == 1 or b == 1:
        return "Voce multiplicou o numero por 1"
    elif a == 0 or b == 0:
        return "Voce multiplicou o numero por 0"
    return valor



def subtrair(a,b):
    valor = a-b
    if a < 0 or b < 0:
        return "Voce subtraiu por um numero negativo"
    else:
        return valor
    