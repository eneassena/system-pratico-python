from Jogo import Jogo
from random import shuffle

class JogoCartas(Jogo):
    def __init__(self, nome:str, clas_etaria: int, preco: float, qtd_jogadores: int, deck: list):
        self._qtd_jogadores = qtd_jogadores
        self._deck = deck
        super().__init__(nome=nome, clas_etaria=clas_etaria, tipo=1, preco=preco)

    def embaralhar(self):
        shuffle(self._deck)
        return '; '.join(self._deck)

    def dados_jogo(self):
    	texto = ""
    	texto += f"\r{super().dados_jogo()} | "
    	texto += f"Qtd. Jogadores: {self._qtd_jogadores} | "
    	texto += f"Cartas: {self.embaralhar()}\n"
    	return texto
