# declaramos la frase a trabajar
frase = "good game"
# declaramos variable quitandole "de" y separando las palabras a frase
phrase = (frase.replace('de', '')).split()
# declaramos variable de texto
acronimo = ""
# hacemos un ciclo for en donde cortamos la primera letra y agregamos en acronimo
for word in phrase:
    acronimo = acronimo + word[0].upper()
print(acronimo)
