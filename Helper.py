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
    
    def ripara_senza_prefisso(self,numero_senza_prefisso):
        return "27"+numero_senza_prefisso;
    
    def ripara_contiene_altro(self,numero_contiene_altro):
        return re.search(self.__contiene_altro,numero_contiene_altro).group()
    
    def ripara_prefisso_sbagliato(self,numero_prefisso_sbagliato):
        return "27"+numero_prefisso_sbagliato[2:]

    def dump_numeri_riparati(self):
        if os.path.isfile('numeri_riparati.txt'):
            os.remove('numeri_riparati.txt')  
        numeri_senza_prefisso = self.lista_numeri_senza_prefisso()
        numeri_contengono_altro = self.lista_numeri_contengono_altro()
        numeri_prefisso_sbagliato = self.lista_numeri_prefisso_sbagliato()
        numeri_non_validi_count = len(self.__lista)
        numeri_riparati_count = len(numeri_senza_prefisso) + len(numeri_contengono_altro) + len(numeri_prefisso_sbagliato)
        with open('numeri_riparati.txt','w') as f:
            f.write("---- RIPARATORE ----\n\n")
            f.write("Nel file 'numeri_non_validi.txt' si trovavano %d numeri non validi.\n" % numeri_non_validi_count)
            f.write("Sono riuscito a ripararne %d.\n\n" % numeri_riparati_count)
            f.write("I seguenti %d numeri ho assunto fossero numeri privi di prefisso:\n\n" % len(numeri_senza_prefisso))
            for item in numeri_senza_prefisso:
                f.write("%s -> %s\n" % (item,self.ripara_senza_prefisso(item)))
            f.write("\nI seguenti %d contenevano al loro interno un numero valido che ho estrapolato:\n\n" % len(numeri_contengono_altro))
            for item in numeri_contengono_altro:
                f.write("%s -> %s\n" % (item,self.ripara_contiene_altro(item)))
            f.write("\nI seguenti %d ho assunto avessero un prefisso sbagliato:\n\n" % len(numeri_prefisso_sbagliato))
            for item in numeri_prefisso_sbagliato:
                f.write("%s -> %s\n" % (item,self.ripara_prefisso_sbagliato(item)))

if __name__ == '__main__':
    helper = Helper('numeri_non_validi.txt')
    helper.dump_numeri_riparati()
    
