sommaire = ["Ajouter un élément à la liste",
            "Retirer un élément de la liste",
            "Afficher les éléments de la liste",
            "Vider la liste",
            "Quitter"]

courses = []
choix = ""

while choix != "5":

    print("\n" + "-" * 40)
    
    for numero, phrase in enumerate(sommaire, start=1):
        print(numero, ":", phrase)

    choix = input("👉 Votre choix : ")

    if not choix.isdigit():
        print("Choix invalide")
        continue

    choix_int = int(choix)

    if choix_int < 1 or choix_int > 5:
        print("Choix invalide")
        continue

    if choix_int == 1:
        element = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        courses.append(element)
        print(f"L'élément {element} a bien été ajouté à la liste")

    if choix_int == 2:
        element = input("Entrez le nom d'un élément à retirer à la liste de courses : ")

        if element in courses:
            courses.remove(element)
            print(f"L'élément {element} a bien été retiré de la liste")
        else:
            print("Cet élément n'est pas dans la liste")
            continue

    if choix_int == 3:
        if not courses:
            print("Votre liste ne contient aucun élément. Faites un nouveau choix.")
            continue

        print("Voici le contenu de votre liste :")
        for numero, element in enumerate(courses, start=1):
            print(numero, ".", element)

        print("-" * 40)

    if choix_int == 4:
        if not courses:
            print("Votre liste est déjà vide. Faites un nouveau choix.")
            continue

        courses.clear()
        print("Votre liste a été vidée. Elle ne contient plus aucun élément.")
        continue

print("Fin du programme")
