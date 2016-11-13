import re
import random


def citeste_fisier(path: str) -> str:
    """
        Functie ce citeste textul din fisierul dat ca parametru
    :param path: Path-ul catre text
    :return:
    """
    file_object = open(path, mode="rt")
    file_content = file_object.read()
    return file_content


def get_cuvinte_unice(text: str) -> set:
    return set(re.findall("[a-z]+", text))


def get_dictionar_cuvinte(continut_fisier: str) -> dict:
    """
        Functie ce construieste dictionarul de cuvinte.
        Dictionarul de cuvinte este multimea tuturor cuvintelor ce se gaseste in text
    :param continut_fisier: Continutul fisierului pe baza caruia construiesc dictionarul de cuvinte
    :return:
    """
    cuvinte = list(get_cuvinte_unice(continut_fisier))
    dictionar = {i: cuvinte[i] for i in range(len(cuvinte))}
    return dictionar


def get_subdictionar(dictionar: dict, text_de_extras: str) -> dict:
    """
        Se extrage din dictionar acei itemi care au ca valoare un cuvant din textul de extras
    :param dictionar
    :param text_de_extras
    :return:
    """
    cuvinte = get_cuvinte_unice(text_de_extras)
    return {item[0]: item[1] for item in dictionar.items() if
            item[1] in cuvinte}


def codifica_dictionar(dictionar_cuvinte: dict, codificare: str) -> dict:
    dictionar_cuvinte_criptate = {item[0]: codifica_fraza(item[1], codificare)
                                  for item in dictionar_cuvinte.items()}
    return dictionar_cuvinte_criptate


def get_litere_alfabet():
    """
        Functie ce imi returneaza literele alfabetului
        Aceasta va fi folosita in generarea de indivizi , etc.
        Folosita pentru a sti ce valori pot avea
    :return:
    """
    litere_alfabet = list()
    prima_litera_alfabet = 97
    ultima_litera_alfabet = 97 + 26
    for litera in range(prima_litera_alfabet, ultima_litera_alfabet):
        litere_alfabet.append(chr(litera))
    return litere_alfabet


def genereaza_codificare():
    """
        Functie ce imi genereaza o codificare
        La fiecare pas scot din lista de litere dispobilite litera pe care
         tocmai al ales-o
    :return:
    """
    codificare = ""
    litere_alfabet = get_litere_alfabet()
    while len(codificare) < 26:
        litera_aleasa = random.choice(litere_alfabet)
        litere_alfabet.remove(litera_aleasa)
        codificare += litera_aleasa
    return codificare


def codifica_fraza(fraza: str, codificare: str) -> str:
    """
        Functie ce codifica o fraza pe baza codificarii primite ca parametru
    :param fraza: Fraza pe care vreau sa o codific
    :param codificare: Codificarea utlizata
    :return:  Fraza codificata
    """
    fraza_codificata = ""
    for litera in fraza:
        fraza_codificata += codificare[ord(litera) - 97]
    return fraza_codificata


def decodifica_fraza(fraza_codificata: str, codificare: str) -> str:
    """
        Functie ce decodifica fraza pe baza presupuse codificari primite ca si parametru
    :param fraza_codificata: Fraza pe care vreau sa o decodific
    :param codificare: Presupusa codificare
    :return: Textul decodificat utilizand codificarea primita ca parametru
    """
    fraza_decodificata = ""
    for litera in fraza_codificata:
        fraza_decodificata += chr(codificare.find(litera) + 97)
    return fraza_decodificata


def genereaza_indivizi(numar_indivizi: int):
    """
        Functie de imi geneaza un numar de indivizi
    :param numar_indivizi: Numarul de indivizi pe care vreau sa ii generez
    :return:
    """
    indivizi = list()
    for i in range(0, numar_indivizi):
        indivizi.append(genereaza_codificare())
    return indivizi


def evaluare_fitness_indivizi(indivizi: list, dictionar_codificat: dict,
                              dictionar: dict):
    """
        Functie ce imi evaluaza fiecare individ pe baza functiei de fitness
        Functie de fitness:Numarul de cuvinte din dictionar care apare in fraza decodificata de fiecare individ
    :param indivizi:
    :param dictionar_codificat:
    :param dictionar:
    :return:
    """

    scor_indivizi = list()
    for individ in indivizi:
        contor = get_fitness_score(dictionar_codificat, dictionar, individ)
        scor_indivizi.append(contor)
    return scor_indivizi


def get_fitness_score(dictionar_codificat: dict, dictionar: dict,
                      posibila_decodificare: str) -> int:
    litere_decriptate = [0] * 26
    for item in dictionar_codificat.items():
        cuvant_codificat = item[1]
        cuvant_decodificat = decodifica_fraza(cuvant_codificat,
                                              posibila_decodificare)
        cuvant = dictionar.get(item[0])
        for j in range(len(cuvant_decodificat)):
            if cuvant[j] == cuvant_decodificat[j]:
                litere_decriptate[ord(cuvant_decodificat[j]) - 97] = 1
    return sum(litere_decriptate)


def sorteaza_indivizi(indivizi: list,
                      scoruri_indivizi: list) -> list:
    """
        Functie ce realizeaza indivizi sortati dupa functia de fitness
    :param indivizi:
    :param scoruri_indivizi:
    :return: O lista de tuple in care cheia=>individul; valoarea=>numarul de cuvinte gasite de respectivul individ
    """
    dictionar_indivizi = [(indivizi[i], scoruri_indivizi[i]) for i in
                          range(0, len(indivizi))]
    indivizi_sortati = [individ for individ in
                        sorted(dictionar_indivizi,
                               key=lambda individ: individ[1], reverse=True)]
    return indivizi_sortati


def determina_duplicate_copil(copil: str, index_ruptura):
    """
        Functie ce determina daca in urma incrusisarii apar duplicate
    :param copil: Unul dintre cei doi copii rezultati in urma incrusicarii
    :param index_ruptura: Indexul la care s-a produs ruptura
    :return: Lista cu indicii duplicatelor
    """
    pozitii_duplicate = list()
    for i in range(0, index_ruptura):
        if copil[index_ruptura:].find(copil[i]) != -1:
            pozitii_duplicate.append(i)
    return pozitii_duplicate


def incrucisare_genetica(parinte1: str, parinte2: str):
    """
        Functie ce returneaza cei doi copii rezultati in urma incrucisarii a doi indivizi
    :param parinte1:
    :param parinte2:
    :return: Un tuplu cu cei di copii rezultati in urma incrucisarii
    """
    index_ruptura = random.randint(2, 26)
    copil1 = parinte1[0:index_ruptura] + parinte2[index_ruptura:]
    copil2 = parinte2[0:index_ruptura] + parinte1[index_ruptura:]
    pozitii_duplicate_copil1 = determina_duplicate_copil(copil1, index_ruptura)
    pozitii_duplicate_copil2 = determina_duplicate_copil(copil2, index_ruptura)
    if len(pozitii_duplicate_copil1) > 0:
        lista_copil1 = [litera for litera in copil1]
        lista_copil2 = [litera for litera in copil2]
        for i in range(0, len(pozitii_duplicate_copil1)):
            lista_copil1[pozitii_duplicate_copil1[i]], lista_copil2[
                pozitii_duplicate_copil2[i]] = lista_copil2[
                                                   pozitii_duplicate_copil2[
                                                       i]], \
                                               lista_copil1[
                                                   pozitii_duplicate_copil1[
                                                       i]]

        copil1 = ""
        copil2 = ""
        for i in range(0, len(lista_copil1)):
            copil1 += lista_copil1[i]
            copil2 += lista_copil2[i]
    return copil1, copil2


def mutatie_genetica(individ: str):
    """
        Functie ce returneaza individul rezultat in urma unei mutatii genetice
    :param individ: Individul ce urmeaza sa fie supus unei mutatii genetice
    :return:
    """
    lungime_individ = len(individ)
    gena_x = random.randint(0, lungime_individ - 1)
    gena_y = random.randint(0, lungime_individ - 1)
    while gena_x == gena_y:
        gena_y = random.randint(0, lungime_individ - 1)
    mutatie_individ = ""
    for i in range(0, lungime_individ):
        if i == gena_x:
            mutatie_individ += individ[gena_y]
        elif i == gena_y:
            mutatie_individ += individ[gena_x]
        else:
            mutatie_individ += individ[i]
    return mutatie_individ
