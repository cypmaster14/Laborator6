from algoritm import *

continut_fisier = ""
try:
    continut_fisier = citeste_fisier("data.txt").lower()
except Exception as e:
    print(e)
    print("Nu s-a putut citi textul din fisier")
    exit()

dictionar_cuvinte = get_dictionar_cuvinte(continut_fisier)
print("Numar de cuvinte in dicionar:", len(dictionar_cuvinte))
codificare = genereaza_codificare()
text_clar = re.sub("[^a-z]", "", continut_fisier)
text_codificat = codifica_text(text_clar, codificare)
cheie_descriptare = decodifica(text_codificat, dictionar_cuvinte)
print("Cheie de criptare:  ", codificare)
print("Cheie de decriptare:", cheie_descriptare)
litere_gasite = 0
for i in range(len(codificare)):
    if codificare[i] == cheie_descriptare[i]:
        litere_gasite += 1
print("Litere corect decriptate:", litere_gasite)
