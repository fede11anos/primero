import random
for i in range(5):
    meme_dict = {
        "XD": "es un emoticono que se usa para expresar risas o carcajadas.",
        "NTP": "Significa no te procupes.",
        "LORE":  "es el conjunto de historias, datos, personajes, etc."
    }
    
    p = input("¿Que palabra quieres saber?:")
    if p in meme_dict:
        print (p, meme_dict[p])
    else:
        print("La palabra no esta en el diccionario")
        A = input("¿quieres agregar la palabra al diccionario?(s/n)")
        if A == s:
            Sg = input("cual es la definicion de lo que quieres agregar?")
            meme_dict.append{p: Sg) 
