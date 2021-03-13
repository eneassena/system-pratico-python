from dataclasses import dataclass


class Localidade:
    def __init__(self, nome: str, sigla: str, taxa_aeroporto: float):
        self.nome = nome
        self.sigla = sigla
        self.taxa_aeroporto = taxa_aeroporto


# Dataclass SSA, passando para o init da superclasse o nome “Salvador”, a sigla “SSA” e a taxa de 160,00.
@dataclass
class SSA(Localidade):
    def __init__(self):
        super().__init__("Salvador", "SSA", 160.00)


# Dataclass FEN, com os valores: F. Noronha, FEN e 180,00.
@dataclass
class FEN(Localidade):
    def __init__(self):
        super().__init__("F. Noronha", "FEN", 180.00)


# Dataclass MIA, com os valores: Miami, MIA e 200,00.
@dataclass
class MIA(Localidade):
    def __init__(self):
        super().__init__("Miami", "MIA", 200.00)


# Dataclass BER, com os valores: Berlim, BER e 220,00.
@dataclass
class BER(Localidade):
    def __init__(self):
        super().__init__("Berlim", "BER", 220.00)


# Dataclass SYD, com os valores: Sydney, SYD e 240,00.
@dataclass
class SYD(Localidade):
    def __init__(self):
        super().__init__("Sydney", "SYD", 240.00)


# Dataclass DXB, com os valores: Dubai, DXB e 300,00.
@dataclass
class DXB(Localidade):
    def __init__(self):
        super().__init__("Dubai", "DXB", 300.00)

