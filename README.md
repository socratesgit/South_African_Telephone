# South African Mobile Numbers

Questo progetto Python (3.X) ha come obiettivo quello di estrarre da un file formato CSV numeri di telefono sudafricani e renderli accessibili per qualsiasi applicativo che voglia operare delle analisi.
Il codice è suddiviso nei seguenti moduli:

1. ### CSVReader
    si occupa di produrre, dato in input un file 'data.csv', due file:
        - 'numeri_validi.txt', il quale contiene i numeri validi
        - 'numeri_non_validi.txt', il quale contiene i numeri non validi

2. ### Helper
    si occupa di produrre un file 'numeri_riparati.txt' dove cerca di estrapolare
    dati i numeri presenti nel file 'numeri_non_validi.txt' attraverso varie euristiche
    dei numeri validi.