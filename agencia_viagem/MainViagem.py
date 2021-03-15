from Gerenciador import Gerenciador
from cpt import *
from os import  system
from time import sleep

# declaração de variaveis ambiente
gerenciador = Gerenciador.get_instance()
exception_error = ""
rodar = True
porta65 = True
keys_reservas_voos = { 
    1:[], 2: [], 3: [], 4: []
}
 
while rodar:
    try: # inicio do sistema
        porta65 = True
        print("""
                \r1) Reservar vôo
                \r2) Ver dados da reserva
                \r3) Ferramentas
                \r4) Sair""")
        entrada = int(input('> '))

        if entrada == 1: # registra um novo voos exibindo um menu e capturando dados do teclado
            print("""
                \r1) SSA-BER (direto)
                \r2) SSA-BER (escala em FEN)
                \r3) MIA-SYD (direto)
                \r4) MIA-SYD (escala em BER e DXB)""")
            try:
                voo = int(input('> '))
                classe = input('qual classe do voo: ')
                num_voo = gerenciador.reservar(voo=voo, classe=classe)
                if add_key_reserva(keys_reservas_voos, voo, num_voo):
                    print(f"Reserva Realizada Nº {num_voo}")

            except Exception as error:
                exception_error = error
        elif entrada == 2: # permite ver os voos que estão reservados
            try:
                numero_reserva = str(input('entre com numero da reserva: '))
                dados = gerenciador.obter_dados_reserva(numero_reserva=numero_reserva)
                print(f'Info do Voo: {dados}')
                
            except Exception as error:
                exception_error = error
        elif entrada == 3: # permite ver os códigos das reservas
            while porta65:
                try:
                    print(f"\nKeys Reservas:\n{view_key_reserva(keys_reservas_voos)}")
                    entrada = int(input("0) Voltar\n> "))
                    if entrada == 0: porta65 = False
                except Exception as error:
                    exception_error = error
        elif entrada == 4: # opção de saida do sistema
            rodar = False
        else: # se a opção estiver errada ou entrada invalida o sistema finaliza a execução
            rodar = False
    except Exception as error: # captura os error e salva na variavel e finaliza a execução
        exception_error = error
        rodar = False
    
    # se houver é no sistema ele é exibido aqui    
    if exception_error: print(f"[ERROR]: {exception_error}")
    
    # aqui o sistema da 5 segundos de espera apois isso limpa a tela a volta ao menu
    sleep(5)
    system('cls') or None



