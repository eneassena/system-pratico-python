from random import choice, randint


def create_key() -> str:
    script = ""
    letras = 'abcdefghijlmnopqrstuvxzkwy'
    for x in range(1, 11, 1):
        numeros = randint(1, 10)
        l_esclhida = choice(letras)
        script += f'{numeros}{l_esclhida}'
    return script


def create_key_voo() -> int:
    inicio, fim = 10000,100000
    numeros = randint(inicio, fim)
    return numeros


def view_key_reserva(keys_reservas_voos: dict) -> str:
    saida = ""
    if keys_reservas_voos:
        for x in keys_reservas_voos: 
            saida += f"Voo: {x} - {keys_reservas_voos[x]}\n"
    return saida
    

def add_key_reserva(key_data: dict, key_index: int, value_key: str) -> bool:
    if 1 <= key_index <= 4:
        key_data[key_index].append(value_key)
        return True
    return False