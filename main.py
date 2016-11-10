from functii import *
import re

try:
    continut_fisier = citeste_fisier("data.txt").lower()
except Exception as e:
    print(e)
    print("Nu s-a putut citi textul din fisier")
    exit()

dictionar_cuvinte = get_dictionar_cuvinte(continut_fisier)
# print(len(dictionar_cuvinte))
codificare = genereaza_codificare()
fraza = "But the story was drawn irresistibly towards the older world, and became an account, as it were, of its end and passing away before its beginning and middle had been told."
fraza_procesata = re.sub("[^a-z]", "", fraza.lower())
print("Fraza initiala    ", fraza_procesata)
fraza_codificata = codifica_fraza(fraza_procesata, codificare)
indivizi = genereaza_indivizi(100)
evaluare_indivizi = evaluare_fitness_indivizi(indivizi, fraza_codificata, dictionar_cuvinte)
indivizi_sortati = sorteaza_indivizi(indivizi, evaluare_indivizi)
print(indivizi_sortati)
print("acbwziuhyftspdvlgmxknrjeqo")
print(mutatie_genetica("acbwziuhyftspdvlgmxknrjeqo"))
