from functii import *


def bucla(text: str, dictionar_cuvinte: str, fraza: str):
    codificare = genereaza_codificare()
    fraza_procesata = re.sub("[^a-z]", "", fraza.lower())
    print("Fraza initiala    ", fraza_procesata)
    fraza_codificata = codifica_fraza(fraza_procesata, codificare)
    print("Fraza codificata", fraza_codificata)
    indivizi = genereaza_indivizi(100)

    while True:
        evaluare_indivizi = evaluare_fitness_indivizi(indivizi, fraza_codificata, dictionar_cuvinte)
        indivizi_sortati = sorteaza_indivizi(indivizi, evaluare_indivizi)
        print(indivizi_sortati)

