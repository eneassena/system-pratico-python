from random import choice, randint


def create_key() -> str:
    script = ""
    letras = 'abcdefghijlmnopqrstuvxzkwy'
    for x in range(1, 11, 1):

        numeros = randint(1, 10)
        l_esclhida = choice(letras)
        script += f'{numeros}{l_esclhida}'
    return script


def create_key_voo():
    numeros = randint(10000,100000)
    return numeros
