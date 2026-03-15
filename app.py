#nesse arquivo ficam todas as ações que se relacionam a classe restaurante criada em outro arquivo.

from Modelos.Restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')

restaurante_praca.receber_avaliacao('Alice', 5)
restaurante_praca.receber_avaliacao('Bob', 7)
restaurante_praca.receber_avaliacao('Charlie', 10)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()