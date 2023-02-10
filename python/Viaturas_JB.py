# 10-XY-20,Opel,Corsa XL,2019-10-15
# 20-PQ-15,Mercedes,300SL,2017-05-31
# 02-XM-01,Mercedes,280SE,2021-07-13
# 22-ZA-03,Ford,Fiesta,2021-02-15

from datetime import date
import subprocess
import sys
from typing import TextIO

from python.Viaturas_JB import InvalidProdAttribute

csv_default_delimiter= ','
DEFAULT_IDENTATION = 3

class Viatura:
    def __init__(self, matricula: str, marca: str):
        self.matricula = matricula
        self.marca = marca   
    
    def __str__(self) -> str:
        return f"Viatura [matricula{self.matricula}, marca:{self.marca}]"

def main():
    carro1 = Viatura("10-XY-20","Opel")

    print (carro1 )


    if __name__ == 'main':
        main()
