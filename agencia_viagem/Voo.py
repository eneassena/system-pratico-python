from cpt import *
from Localidade import Localidade


class Voo:
    _isincremente: int = 0
    _numeros_voos = []

    def __init__(self, origem, destino, *escala):
        self.num_voo = create_key_voo()
        Voo._numeros_voos.append(self.num_voo)

        self.origem: Localidade = origem
        self.destino: Localidade = destino
        self.escala = tuple(escala)

    """
        Retorna o valor da taxa dos voos
         
    """
    def get_taxa(self) -> float:
        taxa: float = 0.0

        taxa += self.origem.taxa_aeroporto
        taxa += self.destino.taxa_aeroporto
        if self.escala:
            for voos in self.escala:
                taxa += voos.taxa_aeroporto
            # taxa /= len(self.escala)
        return taxa

    def get_info_voo(self) -> str:
        texto, escalas = "", ""
        texto += f"Vôo: {self.num_voo}\n"
        if self.escala:
            lista = []
            for esc in self.escala:
                lista.append(esc.nome)
            escalas = ', '.join(lista)
            texto += f"Origem: {self.origem.nome} | Destino: {self.destino.nome} | Escala: {escalas}"
        else:
            texto += f"Origem: {self.origem.nome} | Destino: {self.destino.nome}"
        return texto

