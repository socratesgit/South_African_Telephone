from CSVReader import CSVReader
import os
import re

class Helper:

    perfect_match = re.compile('^27[0-9]{9}$')
    manca_prefisso = re.compile('^[0-9]{9}$')
    prefisso_sbagliato = re.compile('^[0-9]{11}$')
    contiene_altro = re.compile('27[0-9]{9}')


    def __init__(self,file):
        if not os.path.isfile(file):
            CSVReader('data.csv').dump_lista_numeri_non_validi()
        with open(file,'r') as f:
            self.__lista = f.read().splitlines()
    
    def lista_numeri_senza_prefisso(self):
        return [item for item in self.__lista if self.manca_prefisso.match(item)]
    
    def lista_numeri_contengono_altro(self):
        return [item for item in self.__lista if self.contiene_altro.match(item)]

    def lista_numeri_prefisso_sbagliato(self):
        return [item for item in self.__lista if self.prefisso_sbagliato.match(item)]
    
    def ripara_senza_prefisso(numero_senza_prefisso):
        return "27"+numero_senza_prefisso;
    
    def ripara_contiene_altro(numero_contiene_altro):
        return re.search(Helper.contiene_altro,numero_contiene_altro).group()
    
    def ripara_prefisso_sbagliato(numero_prefisso_sbagliato):
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
    print("Ciao! Sono il modulo Helper.\nTi aiutero' a capire se il numero che introduci e' un numero sudafricano valido.")
    print("Qualora il numero che hai introdotto non risulterà essere valido ti fornirò delle alternative che lo siano!")
    while True:
        query = input("Che numero vuoi cercare oggi?\n(Se vuoi uscire dal programma clicca INVIO)\n")
        if(not query):
            break
        if Helper.perfect_match.match(query):
            print("Il numero che hai cercato e' valido!\n")
            continue
        if Helper.manca_prefisso.match(query):
            print("Il numero che hai cercato non e' valido perchè sembra mancargli il prefisso.\n")
            print("Prova con: %s\n" % Helper.ripara_senza_prefisso(query))
            continue
        if Helper.prefisso_sbagliato.match(query):
            print("Il numero che hai cercato non e' valido. Forse hai sbagliato il prefisso!.\n")
            print("Prova con: %s\n" % Helper.ripara_prefisso_sbagliato(query))
            continue
        if Helper.contiene_altro.match(query):
            print("Il numero che hai cercato non e' valido, ma contiene al suo interno un numero valido!")
            print("Prova con: %s\n" % Helper.ripara_contiene_altro(query))
            continue
        
        
    
