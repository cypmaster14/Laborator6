from algoritm import *

continut_fisier = ""
try:
    continut_fisier = citeste_fisier("data.txt").lower()
except Exception as e:
    print(e)
    print("Nu s-a putut citi textul din fisier")
    exit()

dictionar_cuvinte = get_dictionar_cuvinte(continut_fisier)
codificare = genereaza_codificare()
fraza = "But the story was drawn irresistibly towards the older world, and became an account, as it were, of its end and passing away before its beginning and middle had been told."
subdictionar_cuvinte = get_subdictionar(dictionar_cuvinte, continut_fisier)
dictionar_cuvinte_criptate = codifica_dictionar(subdictionar_cuvinte,
                                                codificare)
cheie_descriptare = decodifica(dictionar_cuvinte_criptate, dictionar_cuvinte)
print("Cheie de criptare:  ", codificare)
print("Cheie de decriptare:", cheie_descriptare)
litere_gasite = 0
for i in range(len(codificare)):
    if codificare[i] == cheie_descriptare[i]:
        litere_gasite += 1
print("Litere corect decriptate:", litere_gasite)
