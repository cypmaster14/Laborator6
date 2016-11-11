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
    gena_valoroasa = indivizi_sortati[0][0]
    numar_blocaje = 0

    while not (
            dictionar_corect_decriptat(dictionar_cuvinte, indivizi_sortati[0])) and numar_blocaje <= 100:
        print("Cel mai bun scor acum este:", indivizi_sortati[0], numar_blocaje)
        noua_gengeratie = list()
        print(indivizi_sortati)
        elite = list()
        for i in range(3):
            individ = indivizi_sortati.pop(0)
            elite.append(individ)
            noua_gengeratie.append(individ[0])

        for i in range(20):
            castigator1_turnir = obtine_castigator_turnir(indivizi_sortati)
            castigator2_turnir = obtine_castigator_turnir(indivizi_sortati)
            incrucisate_indivizi(noua_gengeratie, castigator1_turnir[0], castigator2_turnir[0])

        # Incrucisez o elita cu un random

        for i in range(len(elite)):
            parinte1 = elite[i]
            parinte2 = random.choice(indivizi_sortati)
            copii = incrucisare_genetica(parinte1[0], parinte2[0])
            copil1 = (copii[0], get_fitness_score(dictionar_cuvinte, dictionar_codificat, copii[0]))
            copil2 = (copii[1], get_fitness_score(dictionar_cuvinte, dictionar_codificat, copii[1]))
            invingator_competitie = MecanismSelectie.competitie(copil1, copil2)
            noua_gengeratie.append(invingator_competitie[0])
            indivizi_sortati.remove(parinte2)

        for individ in indivizi_sortati:
            mutant = mutatie_genetica(individ[0])
            noua_gengeratie.append(mutant)

        indivizi_sortati = obtine_indivizi_sortati(noua_gengeratie,
                                                   dictionar_codificat,
                                                   dictionar_cuvinte)
        if indivizi_sortati[0][1] <= scor_maxim:
            numar_blocaje += 1
        else:
            numar_blocaje = 0
            scor_maxim = indivizi_sortati[0][1]
            gena_valoroasa = indivizi_sortati[0][0]

    print("Gena valoroasa:", gena_valoroasa)
    print("Numar blocaje:", numar_blocaje)
    print("Cheie de decriptare:", gena_valoroasa)
    return gena_valoroasa


def incrucisate_indivizi(noua_generatie: list, individ1: str, individ2: str):
    copil1, copil2 = incrucisare_genetica(individ1, individ2)
    noua_generatie.append(copil1)
    noua_generatie.append(copil2)


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
