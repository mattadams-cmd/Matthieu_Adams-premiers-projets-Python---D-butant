import random
joueur_1 = 50
ennemi = 50
potions = 3
saisie = ""
passer_tour = False

print("***Combat JDR***")
while joueur_1 > 0 and ennemi > 0:
    if passer_tour: 
        print("Vous passez votre tour...")
        passer_tour = False

        attaque_ennemi = random.randint(5, 15)
        joueur_1 = joueur_1 - attaque_ennemi

        if joueur_1 <= 0:
            print(f"L'ennemi vous a infligé {attaque_ennemi} point de dégats ⚔️")
            print("Vous avez perdu !")
            print("Fin du jeu.")
            break

        print(f"L'ennemi vous a infligé {attaque_ennemi} point de dégats ⚔️")
        print(f"Il vous reste {joueur_1} points de vie")
        print(f"Il reste {ennemi} points de vie à l'ennemi")
        continue

    saisie = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?")  
    if not saisie.isdigit() or int(saisie) not in (1, 2) :
        print("Veuillez saisir une action valide")
        continue

    saisie_action = int(saisie)

    if saisie_action == 1:
        attaque_joueur_1 = random.randint(5, 10)
        attaque_ennemi = random.randint(5, 15)

        ennemi = ennemi - attaque_joueur_1

        if ennemi <= 0: 
            print(f"Vous avez infligé {attaque_joueur_1} point de dégats à l'ennemi ⚔️")
            print("Tu as gagné !")
            print("Fin du jeu.")
            break

        joueur_1 = joueur_1 - attaque_ennemi

        if joueur_1 <= 0:
            print(f"L'ennemi vous a infligé {attaque_ennemi} point de dégats ⚔️")
            print("Vous avez perdu !")
            print("Fin du jeu.")
            break

        print(f"Vous avez infligé {attaque_joueur_1} point de dégats à l'ennemi ⚔️")
        print(f"L'ennemi vous a infligé {attaque_ennemi} point de dégats ⚔️")
        print(f"Il vous reste {joueur_1} points de vie")
        print(f"Il reste {ennemi} points de vie à l'ennemi")
        continue

    if saisie_action == 2: 
        if potions <= 0:   
            print("Vous n'avez plus de potions")
            continue

        potions -=1
        soin_potion = random.randint(15, 50)
        joueur_1 = joueur_1 + soin_potion
        joueur_1 = min(joueur_1, 50)

        attaque_ennemi = random.randint(5, 15)
        joueur_1 = joueur_1 - attaque_ennemi

        if joueur_1 <= 0:
            print(f"L'ennemi vous a infligé {attaque_ennemi} point de dégats ⚔️")
            print("Vous avez perdu !")
            print("Fin du jeu.")
            break

        print(f"Vous récupérez {soin_potion} point de vie ❤️ ({potions} 🧪 restantes )")
        print(f"L'ennemi vous a infligé {attaque_ennemi} point de dégats ⚔️")
        print(f"Il vous reste {joueur_1} points de vie")
        print(f"Il reste {ennemi} points de vie à l'ennemi")
        passer_tour = True
        continue           



