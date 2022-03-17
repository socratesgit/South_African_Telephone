# South African Mobile Numbers

Questo progetto Python (3.X) ha come obiettivo quello di estrarre da un file formato CSV numeri di telefono sudafricani (es.: 27897465321) e renderli accessibili per qualsiasi applicativo che voglia operare delle analisi.
Il codice è suddiviso nei seguenti moduli:

1. ### CSVReader
    si occupa di produrre, dato in input un file _'data.csv'_, due file: _'numeri\_validi.txt'_, il quale contiene i numeri validi e _'numeri\_non\_validi.txt'_, il quale contiene i numeri non validi

2. ### Helper
    si occupa di produrre un file  _'numeri\_riparati.txt'_  dove cerca di estrapolare
    dati i numeri presenti nel file _'numeri\_non\_validi.txt'_ attraverso varie euristiche dei numeri validi.
    Inoltre, se viene lanciato da linea di comando (_'python Helper.py'_), attraverso un menu da linea comando permette all'utente di inserire numeri di telefono da verificare e, nel caso non siano validi, propone alcune alternative.

## WORKFLOW

1. Clona la repo in locale
2. Crea un ambiente virtuale con _python -m venv [nome ambiente virtuale]_
3. Installa le dipendenze con _pip install -r requirements.txt_
4. Lancia il comando _python run.py_

A questo punto, se non fossero stati già presenti, dovrebbero essere stati generati i file _'numeri\_validi.txt'_, _'numeri\_non\_validi_ e _'numeri\_riparati.txt'_. Inoltre, nella cartella _img_ troverete alcuni grafici prodotti dal programma _run.py_ che danno alcune informazioni rispetto ai risultati delle computazioni dei moduli.