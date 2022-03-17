import pandas as pd
import os
import re

'''
Questo modulo legge da un CSV contenente coppie (id,numero) e restituisce 
attraverso i suoi metodi viste sui dati.
'''
class CSVReader:

    __perfect_match = re.compile('^27[0-9]{9}$')

    def __init__(self,file):
        if not os.path.isfile(file):
            raise FileNotFoundError('il file non esiste!')
        self.df=pd.read_csv(file)
        self.__numeri_validi = None
        self.__numeri_non_validi = None
    
    '''
    Resituisce la lista dei numeri presenti nel file.
    '''
    def lista_numeri(self):
        return [item[1] for item in self.df.values]
    
    '''
    Restituisce la lista dei numeri validi presenti nel file.
    '''
    def lista_numeri_validi(self):
        if self.__numeri_validi is None:
            self.__numeri_validi = [numero for numero in self.lista_numeri() if self.__perfect_match.match(numero)]
        return self.__numeri_validi
    
    '''
    Restituisce la lista dei numeri non validi presenti nel file.
    '''
    def lista_numeri_non_validi(self):
        if self.__numeri_non_validi is None:
            self.__numeri_non_validi = [numero for numero in self.lista_numeri() if numero not in self.lista_numeri_validi()]
        return self.__numeri_non_validi     
    
    '''
    Salva in un file chiamato "numeri_validi.txt" i numeri validi presenti nel file.
    '''
    def dump_lista_numeri_validi(self):
        if os.path.isfile('numeri_validi.txt'):
            os.remove('numeri_validi.txt')
        with open('numeri_validi.txt', 'w') as f:
            for item in self.lista_numeri_validi():
                f.write("%s\n" % item)
    '''
    Salva in un file chiamato "numeri_non_validi.txt" i numeri non validi presenti nel file.
    '''
    def dump_lista_numeri_non_validi(self):
        if os.path.isfile('numeri_non_validi.txt'):
            os.remove('numeri_non_validi.txt')
        with open('numeri_non_validi.txt','w') as f:
            for item in self.lista_numeri_non_validi():
                f.write("%s\n" % item)

if __name__ == '__main__':
    try:
        reader = CSVReader('data.csv')
    except:
        print("Nella cartella non e' presente un file di nome 'data.csv'")
        os._exit()
    reader.dump_lista_numeri_validi()
    reader.dump_lista_numeri_non_validi()
    


