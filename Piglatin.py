def convertir_a_pig_latin(palabra):
    palabra = palabra.lower()  # Convertimos todo a minúsculas
    vocales = "aeiou"

    if palabra[0] in vocales:
        return palabra + "way"
    else:
        i = 0
        while i < len(palabra) and palabra[i] not in vocales:
            i += 1
        return palabra[i:] + palabra[:i] + "ay"

# Pedir al usuario una palabra
palabra = input("Ingresa una palabra: ")
pig_latin = convertir_a_pig_latin(palabra)

print("En Pig Latin:", pig_latin)
