import unittest
import re
from Helper import Helper

class TestCSVReader(unittest.TestCase):

    def setUp(self):
        self.helper = Helper('numeri_non_validi.txt')
        self.perfect_match = re.compile('^27[0-9]{9}$')
        
    def test_lista_numeri_senza_prefisso(self):
        lista_test = ['824784612','621433086','770598777']
        lista_numeri_senza_prefisso = self.helper.lista_numeri_senza_prefisso()
        for item in lista_test:
            self.assertTrue(item in lista_numeri_senza_prefisso)

    def test_numeri_contengono_altro(self):
        lista_test = ['27735405794_DELETED_1488987214','27836826107_DELETED_1488997292','27735405794_DELETED_1488987552']
        lista_numeri_contengono_altro = self.helper.lista_numeri_contengono_altro()
        for item in lista_test:
            self.assertTrue(item in lista_numeri_contengono_altro)

    def test_numeri_prefisso_sbagliato(self):
        lista_test = ['81875586919','96894783831','26876272427']
        lista_numeri_prefisso_sbagliato = self.helper.lista_numeri_prefisso_sbagliato()
        for item in lista_test:
            self.assertTrue(item in lista_numeri_prefisso_sbagliato)
    
    def test_ripara_senza_prefisso(self):
        lista_test = self.helper.lista_numeri_senza_prefisso()
        lista_corretta = list()
        for item in lista_test:
            lista_corretta.append(self.helper.ripara_senza_prefisso(item))
        for item in lista_corretta:
            self.assertTrue(self.perfect_match.match(item))

    def test_ripara_contiene_altro(self):
        lista_test = self.helper.lista_numeri_contengono_altro()
        lista_corretta = list()
        for item in lista_test:
            lista_corretta.append(self.helper.ripara_contiene_altro(item))
        for item in lista_corretta:
            self.assertTrue(self.perfect_match.match(item))

    def test_ripara_prefisso_sbagliato(self):
        lista_test = self.helper.lista_numeri_prefisso_sbagliato()
        lista_corretta = list()
        for item in lista_test:
            lista_corretta.append(self.helper.ripara_prefisso_sbagliato(item))
        for item in lista_corretta:
            self.assertTrue(self.perfect_match.match(item))
  

if __name__ == '__main__':
    unittest.main()