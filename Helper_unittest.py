import unittest
from Helper import Helper

class TestCSVReader(unittest.TestCase):

    def setUp(self):
        self.helper = Helper('numeri_non_validi.txt')
        
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


if __name__ == '__main__':
    unittest.main()