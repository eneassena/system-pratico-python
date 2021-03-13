"""
Classe JogoEletronico (herda de Jogo)
No inicializador, chama o init da superclasse, passando nome, clas_etaria, tipo
(sempre 0), preco. Além disso, possui dois atributos privados: categoria e plataformas
(lista com as plataformas para as quais o jogo foi desenvolvido).

Possui o método listar_plataformas(). A primeira coisa que o método faz é ordenar
alfabeticamente as plataformas. Para isso, basta chamar o método sort(), nativo para
toda lista. Em seguida, o método deve retornar uma string com todas as plataformas
(já em ordem alfabética) e separadas por ponto-e-vírgula.

Sobrescreve o método dados_jogo() da superclasse. Retorna uma string com as informações
da superclasse, além da categoria do jogo e plataformas (já ordenadas alfabeticamente!).


"""

from Jogo import Jogo

class JogoEletronico(Jogo):
	def __init__(self, nome:str, clas_etaria: int, preco: float, categoria: str, plataformas: list):
		super().__init__(nome=nome, clas_etaria=clas_etaria, tipo=0, preco=preco)
		self._categoria = categoria
		self._plataformas = plataformas

	def listar_plataformas(self):
		texto = ""
		if self._plataformas:
			self._plataformas.sort()
			for p in self._plataformas:
				texto += f"{p}; "
			return texto

	def dados_jogo(self):
		texto = "\r"
		texto += f"{super().dados_jogo()} | "
		texto += f"Categoria: {self._categoria} | "
		texto += f"Plataforma(s): {self.listar_plataformas()}"
		return texto
 