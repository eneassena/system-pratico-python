from Jogo import Jogo 
from JogoCartas import JogoCartas 
from JogoEletronico import JogoEletronico 

def main():
	jogo = Jogo('Dominó', 2, 0, 20.00)
	jogo_cartas = JogoCartas('Yu-Gi-Oh', 12, 40.00, 2, ['Dark Hole', 'Exodia', 'Mirror Force', 'Slifer'])
	jogo_eletronico = JogoEletronico('GTA V', 18, 150.00, 'Aventura', ['Windows', 'PlayStation', 'XBox'])
	print(f'{jogo.dados_jogo()}')
	print(f'{jogo_cartas.dados_jogo()}')
	print(f'{jogo_eletronico.dados_jogo()}')

if __name__ == '__main__':
	main()