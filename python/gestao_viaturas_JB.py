# # matricula (str), marca, modelo, data
# 10-XY-20,Opel,Corsa XL,2019-10-15
# 20-PQ-15,Mercedes,300SL,2017-05-31

# Menu
#       1 - Listar Viaturas
#       2 - Pesquisar Viaturas
#       3 - Adicionar Viatura
#       4 - Remover Viatura
#       5 - Actualizar Catálogo
#       6 - Recarregar Catálogo
#       T - Terminar
# 
#       Opção  >>  

from datetime import date
import subprocess
import sys
from typing import TextIO

from python.gestao_viaturas_JB import InvalidProdAttribute

def main():
    while True:
       

        # 1. Exibir o menu
        print("1 - Listar Viaturas")
        print("2 - Pesquisar Viaturas")
        print("3 - Adicionar Viatura")
        print("4 - Remover Viatura")
        print("5 - Actualizar Catálogo")
        print("6 - Recarregar Catálogo")


        print("T. Terminar o programa")

        # 2. Ler opção
        opcao = input("> ")

        # 3. Analisar e executar a opção
        # if opcao == '1':
        #     montante = dec(input("Montante em Euros: "))
        #     print(f"Dólares -> {montante * cambio_eur_usd:.2f}")
        # elif opcao == '2':
        #     montante = dec(input("Montante em Dólares: "))
        #     print(f"Euros -> {montante / cambio_eur_usd:.2f}")
        # elif opcao.upper() == 'T':
        #     print("Programa vai terminar")
        #     break
        #:
    #:
#:

CSV_DEFAULT_DELIM = ','
DEFAULT_INDENTATION = 3



class viaturas:
    def __init__(
            self, 
            matricula: str,
            marca: str, 
            modelo: str,
            data: int
         
    ):
        if matricula < 0 or len(str(matricula)) != 9:
            raise ValueError(f'{matricula=} inválido (deve ser  xx-xx-xx)')
        if not marca:
           raise ValueError('Nome vazio')
        if not modelo:
           raise ValueError('Nome vazio')
        if data < 0:
            raise ValueError('Quantidade deve ser >= 0')



if __name__ == '__main__':
    main()
#: