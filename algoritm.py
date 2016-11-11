from functii import *
import MecanismSelectie


def dictionar_corect_decriptat(dictionar: list, individ: tuple) -> bool:
    return len(dictionar) == individ[1]


def obtine_indivizi_sortati(indivizi: list, dictionar_codificat: list,
                            dictionar_cuvinte: list) -> list:
    evaluare_indivizi = evaluare_fitness_indivizi(indivizi,
                                                  dictionar_codificat,
                                                  dictionar_cuvinte)
    return sorteaza_indivizi(indivizi, evaluare_indivizi)


def bucla(dictionar_codificat: list, dictionar_cuvinte: list, fraza: str):
    codificare = genereaza_codificare()
    fraza_procesata = re.sub("[^a-z]", "", fraza.lower())
    print("Fraza initiala  ", fraza_procesata)
    fraza_codificata = codifica_fraza(fraza_procesata, codificare)
    print("Fraza codificata", fraza_codificata)
    indivizi = genereaza_indivizi(100)
    indivizi_sortati = obtine_indivizi_sortati(indivizi, dictionar_codificat,
                                               dictionar_cuvinte)

    scor_maxim = indivizi_sortati[0][1]
    numar_blocaje = 0

    while not (
            dictionar_corect_decriptat(dictionar_cuvinte, indivizi_sortati[0])) \
            and numar_blocaje < 100:
        print("Cel mai bun scor acum este:", indivizi_sortati[0])
        noua_gengeratie = list()
        for i in range(3):
            noua_gengeratie.append(indivizi_sortati[i][0])
            del indivizi_sortati[i]
        for i in range(35):
            castigator1_turnir = obtine_castigator_turnir(indivizi_sortati)
            castigator2_turnir = obtine_castigator_turnir(indivizi_sortati)
            copii = incrucisare_genetica(castigator1_turnir[0],
                                         castigator2_turnir[0])
            noua_gengeratie.append(copii[0])
            noua_gengeratie.append(copii[1])
        for individ in indivizi_sortati:
            mutant = mutatie_genetica(individ[0])
            noua_gengeratie.append(mutant)
        indivizi_sortati = obtine_indivizi_sortati(noua_gengeratie,
                                                   dictionar_codificat,
                                                   dictionar_cuvinte)
        if indivizi_sortati[0][1] == scor_maxim:
            numar_blocaje += 1
        else:
            numar_blocaje = 0
    print("Cheie de decriptare:", indivizi_sortati[0][0])
    print("Numar blocaje:", numar_blocaje)


def obtine_castigator_turnir(indivizi_sortati: list) -> tuple:
    copie_lista = list(indivizi_sortati)
    participanti_turnir = list()
    for j in range(8):
        participant_selectat = random.choice(copie_lista)
        participanti_turnir.append(participant_selectat)
        copie_lista.remove(participant_selectat)
    castigator_turnir = MecanismSelectie.turnir(participanti_turnir)
    indivizi_sortati.remove(castigator_turnir)
    return castigator_turnir
