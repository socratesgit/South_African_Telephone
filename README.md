# South African Mobile Numbers

Questo progetto Python (3.X) ha come obiettivo quello di estrarre da un file formato CSV numeri di telefono sudafricani e renderli accessibili per qualsiasi applicativo che voglia operare delle analisi.
Il codice è suddiviso nei seguenti moduli:

1. ### CSVReader
    si occupa di produrre, dato in input un file __'data.csv'__, due file: __'numeri_validi.txt'__, il quale contiene i numeri validi e __'numeri_non_validi.txt'__, il quale contiene i numeri non validi

2. ### Helper
    si occupa di produrre un file __'numeri_riparati.txt'__ dove cerca di estrapolare
    dati i numeri presenti nel file __'numeri_non_validi.txt'__ attraverso varie euristiche dei numeri validi.
    Inoltre, se viene lanciato da linea di comando (**python Helper.py**), attraverso un menu da linea comando permette all'utente di inserire numeri di telefono da verificare e, nel caso non siano validi, propone alcune alternative.