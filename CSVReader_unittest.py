import unittest
import CSVReader as csv
import re

class TestCSVReader(unittest.TestCase):

    def setUp(self):
        self.reader = csv.CSVReader('data.csv')
        self.perfect_match = re.compile('27[0-9]{9}')

    def test_lista_numeri(self):
        primi_cinque_numeri = ['6478342944','84528784843','263716791426','27736529279','27718159078']
        self.assertListEqual(self.reader.lista_numeri()[0:5],primi_cinque_numeri)
    
    def test_lista_numeri_validi(self):
        for item in self.reader.lista_numeri_validi():
            self.assertTrue(self.perfect_match.match(item))
    
    def test_lista_numeri_non_validi(self):
        for item in self.reader.lista_numeri_non_validi():
            self.assertFalse(self.perfect_match.match(item))



if __name__ == '__main__':
    unittest.main()