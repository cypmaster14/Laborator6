import random

min_fitness = 0
max_fitness = 0


def competitie(individ1: tuple, individ2: tuple) -> tuple:
    return individ1 if individ1[1] > individ2[1] else individ2


def fitness_turnir(individ: tuple) -> float:
    pondere = 0.65
    nr_random = random.uniform(min_fitness, max_fitness)
    return individ[1] * pondere + nr_random * (1 - pondere)


def compara_indivizi_turnir(individ1: tuple, individ2: tuple) -> tuple:
    return individ1 if fitness_turnir(individ1) > fitness_turnir(
        individ2) else individ2


def turnir(indivizi: list) -> tuple:
    if len(indivizi) is 1:
        return indivizi[0]
    runda_urmatoare = list()
    for i in range(0, len(indivizi), 2):
        runda_urmatoare.append(
            compara_indivizi_turnir(indivizi[i], indivizi[i + 1]))
    return turnir(runda_urmatoare)
