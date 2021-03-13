from Gerenciador import Gerenciador


gerenciador = Gerenciador.get_instance()

rodar = True
while rodar:

    try:
        print("""
                \r1) Reservar vôo
                \r2) Ver dados da reserva
                \r3) Sair""")
        entrada = int(input('> '))

        if entrada == 1:
            print("""
                \r1) SSA-BER (direto)
                \r2) SSA-BER (escala em FEN)
                \r3) MIA-SYD (direto)
                \r4) MIA-SYD (escala em BER e DXB)""")
            try:
                voo = int(input('> '))
                classe = input('qual classe do voo: ')
                num_voo = gerenciador.reservar(voo=voo, classe=classe)
                print(f"Reserva Realizada Nº {num_voo}")
            except Exception as error:
                print(error)
        elif entrada == 2:
            try:
                numero_reserva = str(input('entre com numero da reserva: '))
                dados = gerenciador.obter_dados_reserva(numero_reserva=numero_reserva)
                print(dados)
            except Exception as error:
                print(error)
        elif entrada == 3:
            rodar = False
        else:
            rodar = False
    except Exception as error:
        print(f"[ERROR]: {error}")
        rodar = False


