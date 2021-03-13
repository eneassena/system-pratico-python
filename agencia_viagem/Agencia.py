from Reserva import Reserva


class Agencia:
    def __init__(self, nome):
        self.nome = nome
        self.reservas = []

    def realizar_reserva(self, reserva: Reserva) -> str:
        self.reservas.append(reserva)
        return reserva.num_reserva

    def buscar_reserva(self, numero_reserva: str) -> str:
        if self.reservas:
            for res in self.reservas:
                if res.num_reserva == numero_reserva:
                    return res.get_info_reserva()
            else:
                return "Reserva não foi encontrada"
        else:
            return "Não há reservas cadastradas"


