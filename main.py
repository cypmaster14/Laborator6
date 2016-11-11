from algoritm import *
import re

continut_fisier = ""
try:
    continut_fisier = citeste_fisier("data.txt").lower()
except Exception as e:
    print(e)
    print("Nu s-a putut citi textul din fisier")
    exit()

dictionar_cuvinte = get_dictionar_cuvinte(continut_fisier)
# print(len(dictionar_cuvinte))
codificare = genereaza_codificare()
print("Cheie de criptare:", codificare)
fraza = "But the story was drawn irresistibly towards the older world, and became an account, as it were, of its end and passing away before its beginning and middle had been told."
dictionar_cuvinte_criptate = codifica_dictionar(dictionar_cuvinte, codificare)
bucla(dictionar_cuvinte_criptate, dictionar_cuvinte, fraza)
