from functii import *
import MecanismSelectie


def toate_literele_decriptate(individ: tuple) -> bool:
    return individ[1] is 26


def obtine_indivizi_sortati(indivizi: list, dictionar_codificat: dict,
                            dictionar_cuvinte: dict) -> list:
    scoruri_indivizi = evaluare_fitness_indivizi(indivizi,
                                                 dictionar_codificat,
                                                 dictionar_cuvinte)
    return sorteaza_indivizi(indivizi, scoruri_indivizi)


def decodifica(dictionar_codificat: dict, dictionar_cuvinte: dict):
    indivizi = genereaza_indivizi(100)
    indivizi_sortati = obtine_indivizi_sortati(indivizi, dictionar_codificat,
                                               dictionar_cuvinte)

    scor_maxim = indivizi_sortati[0][1]
    gena_valoroasa = indivizi_sortati[0][0]
    numar_blocaje = 0

    while not (
            toate_literele_decriptate(
                indivizi_sortati[0])) and numar_blocaje <= 100:
        print("Cel mai bun scor acum este:", indivizi_sortati[0])
        print("Numar blocaje curent: ", numar_blocaje)
        noua_gengeratie = list()
        elite = list()
        for i in range(3):
            individ = indivizi_sortati.pop(0)
            elite.append(individ)
            noua_gengeratie.append(individ[0])

        for i in range(20):
            castigator1_turnir = obtine_castigator_turnir(indivizi_sortati)
            castigator2_turnir = obtine_castigator_turnir(indivizi_sortati)
            incrucisare_indivizi(noua_gengeratie, castigator1_turnir[0],
                                 castigator2_turnir[0])

        # Incrucisez o elita cu un random

        for i in range(len(elite)):
            parinte1 = elite[i]
            parinte2 = random.choice(indivizi_sortati)
            copii = incrucisare_genetica(parinte1[0], parinte2[0])
            copil1 = (copii[0],
                      get_fitness_score(dictionar_codificat, dictionar_cuvinte,
                                        copii[0]))
            copil2 = (copii[1],
                      get_fitness_score(dictionar_codificat, dictionar_cuvinte,
                                        copii[1]))
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
    return gena_valoroasa


def incrucisare_indivizi(noua_generatie: list, individ1: str, individ2: str):
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
