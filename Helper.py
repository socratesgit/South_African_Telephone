from CSVReader import CSVReader
import os
import re

class Helper:

    __perfect_match = re.compile('^27[0-9]{9}$')
    __manca_prefisso = re.compile('^[0-9]{9}$')
    __prefisso_sbagliato = re.compile('^[0-9]{11}$')
    __contiene_altro = re.compile('27[0-9]{9}')


    def __init__(self,file):
        if not os.path.isfile(file):
            CSVReader('data.csv').dump_lista_numeri_non_validi()
        with open(file,'r') as f:
            self.__lista = f.read().splitlines()
    
    def lista_numeri_senza_prefisso(self):
        return [item for item in self.__lista if self.__manca_prefisso.match(item)]
    
    def lista_numeri_contengono_altro(self):
        return [item for item in self.__lista if self.__contiene_altro.match(item)]

    def lista_numeri_prefisso_sbagliato(self):
        return [item for item in self.__lista if self.__prefisso_sbagliato.match(item)]

    def riparatore(self):
        if os.path.isfile('numeri_riparati.txt'):
            os.remove('numeri_riparati.txt')   
         

if __name__ == '__main__':
    helper = Helper('numeri_non_validi.txt')
    print(helper.lista_numeri_senza_prefisso()[0:5])
    lista = helper.lista_numeri_prefisso_sbagliato()[0:5]
    for item in lista:
        print("27"+item[2:])
    
