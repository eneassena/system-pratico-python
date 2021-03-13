from Agencia import Agencia
from Localidade import *
from Reserva import Reserva
from Voo import Voo


class Gerenciador:
    _instancia = None

    @staticmethod
    def get_instance():
        if Gerenciador._instancia is None:
            Gerenciador._instancia = Gerenciador()
            return Gerenciador._instancia
        return Gerenciador._instancia

    def __init__(self):
        self.agencia = Agencia('Gaspazinho')
        self.voo1 = Voo(SSA(), BER())
        self.voo2 = Voo(SSA(), BER(), FEN())
        self.voo3 = Voo(MIA(), SYD())
        self.voo4 = Voo(MIA(), SYD(), BER(), DXB())
        self.voos_disponivel = {
            1: self.voo1, 2: self.voo2,
            3: self.voo3, 4: self.voo4
        }

    def reservar(self, voo: int, classe: str) -> int:
        if 1 <= voo <= 4:
            reserva = Reserva(self.voos_disponivel.get(voo), classe)
            return self.agencia.realizar_reserva(reserva=reserva)
        else:
            return -1

    def obter_dados_reserva(self, numero_reserva: str) -> str:
        return self.agencia.buscar_reserva(numero_reserva=numero_reserva)
