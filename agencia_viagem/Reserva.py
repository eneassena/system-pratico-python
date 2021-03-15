from cpt import create_key, create_key_voo

class Reserva:
    _isnumeric_auto = 0

    def __init__(self, voos, classe="X"):

        self.voos = voos
        self.classe = classe
        self.num_reserva: str = create_key()


    @property
    def classe(self):
        return self._classe

    @classe.setter
    def classe(self, new_class):
        if new_class == "X":
            self._classe = "Executivo"
        else:
            self._classe = "Econômica"

    def get_preco_final(self) -> float:
        preco_final: float = 0
        preco_final += self.voos.get_taxa()
        if self.classe == "Executivo":
            preco_final += 200
        return preco_final

    def get_info_reserva(self) -> str:
        texto = ""
        texto += f"\r{self.voos.get_info_voo()}\n"
        texto += f"\rReserva Voo: {self.num_reserva}º\n"
        texto += f"\rVoo Classe: {self.classe}\n"
        texto += f"\rValor Final: R$: {self.get_preco_final():.2f}\n"
        return texto
