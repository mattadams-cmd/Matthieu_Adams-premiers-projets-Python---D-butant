import random
nombre_mystere = random.randint(0, 100)
tentatives = 5
saisie = ""

print("*** Le jeu du nombre mystère***")
while tentatives > 0 :
    saisie = input("Devine le nombre : ")
    if not saisie.isdigit():
        print("Veuillez entrer un nombre valide.")  
        continue

    nombre = int(saisie)
    tentatives -= 1

    if nombre == nombre_mystere:
        print(f"Bravo ! Le nombre mystère était bien {nombre_mystere} !")
        print(f"Tu as trouvé le nombre en {5 - tentatives} tentatives.")
        print("Fin du jeu")
        break

    elif nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
        print(f" Il te reste {tentatives} essais ")

    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
        print(f" Il te reste {tentatives} essais ")
else:
    print(f"Dommage ! Le nombre mystère était {nombre_mystere}")