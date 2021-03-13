class Quadrado:
    diag = 1.41

    def __init__(self, lado):
        self.lado = lado 

    def obter_area(self):
        resultado = pow(self.lado, 2)
        return resultado

    def obter_perimetro(self):
        resultado = 4 * self.lado
        return resultado

    def obter_diagonal(self):
        resultado = self.lado * Quadrado.diag
        return resultado
          

    @classmethod
    def atualizar_diag(cls, novo_valor):
        if novo_valor:
            cls.diag = novo_valor

    @property
    def lado(self):
        return self._lado

    @lado.setter
    def lado(self, new_lado):
        if new_lado:
            self._lado = new_lado