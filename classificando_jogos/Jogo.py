class Jogo :
    _tipos_jogo = ["Jogo Eletrônico", "Jogo de Cartas", "Outro"]

    def __init__(self, nome: str, tipo: int,  clas_etaria: int, preco: float):
        self._nome = nome
        self._clas_etaria = clas_etaria
        self._tipo = tipo
        self.preco = preco 

    @property
    def tipo(self) -> int:
        return self._tipo

    @tipo.setter
    def tipo(self, value: int):
        if 0 <= value <= 2:
            self._tipo: int = value

    @property
    def preco(self) -> float:
        return self._preco

    @preco.setter
    def preco(self, value: float):
        if self._clas_etaria >= 0:
             
            if self._clas_etaria < 12:
                self._preco: float = value
            elif self._clas_etaria <= 17:
                self._preco: float = (value + (value * 0.05))
            elif self._clas_etaria >= 18:
                self._preco: float = (value + (value * 0.10))
        else: 
            raise Exception("clas_etaria invalido")

    def dados_jogo(self) -> str:
        texto: str = ""
        texto += f"\nNome: {self._nome} | Preço R$ {self.preco:.2f} | Tipo Jogo: {Jogo._tipos_jogo[self._tipo]}\n"
        return texto
