class Circulo: 
    pi: float = 3.1415

    def __init__(self, raio: float):
        self.raio: float = raio
    
    def obter_area(self) -> float:
        # pi x raio²
        area: float = (Circulo.pi * pow(self.raio, 2)) 
        return area

    def obter_circunferencia(self) -> float : # Circunferência do Círculo: 2 x pi x raio
        circunferência: float = (2 * Circulo.pi * self.raio)
        return circunferência

    @classmethod 
    def atualizar_pi(cls, novo_valor: float) -> None:
        cls.pi: float = novo_valor