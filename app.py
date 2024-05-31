from modelos.restaurante import Restaurante
from modelos.cardapio.prato import Prato
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melância', 5.0, 'Grande')
bebida_suco.aplicaro_desconto()
prato_paozinho = Prato('Paozinho', 2.0, 'O melhor pão da cidade')
prato_paozinho.aplicaro_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    # Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()