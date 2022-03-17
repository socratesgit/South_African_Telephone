from CSVReader import CSVReader
from Helper import Helper
import matplotlib.pyplot as plt
import os

reader = CSVReader('data.csv')
reader.dump_lista_numeri_validi()
reader.dump_lista_numeri_non_validi()

helper = Helper()
helper.dump_numeri_riparati()


legenda = ['# validi', '# non validi']
validi_vs_non_validi = [len(reader.lista_numeri_validi()),len(reader.lista_numeri_non_validi())]

fig1 = plt.figure(figsize = (10, 5))

plt.bar(legenda, validi_vs_non_validi, color ='maroon',
        width = 0.4)

if os.path.isfile('img/validi_vs_non_validi.png'):
    os.remove('img/validi_vs_non_validi.png')

plt.savefig('img/validi_vs_non_validi.png')
plt.close()

legenda2 = ['# non validi', '# senza prefisso', '# prefisso sbagliato', '# che ne contenevano uno valido']
valori = [len(reader.lista_numeri_non_validi()),len(helper.lista_numeri_senza_prefisso()),
            len(helper.lista_numeri_prefisso_sbagliato()),len(helper.lista_numeri_contengono_altro())]

fig2 = plt.figure(figsize = (10, 5))

plt.bar(legenda2, valori, color ='maroon',
        width = 0.4)

if os.path.isfile('img/riparati.png'):
    os.remove('img/.riparati.png')

plt.savefig('img/riparati.png')
plt.close()