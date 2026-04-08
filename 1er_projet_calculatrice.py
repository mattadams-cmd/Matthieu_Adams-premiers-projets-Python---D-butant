#mon code :
calculatrice1 = input("Saissisez le premier nombre afin de réaliser une addition")
premier_nombre = int(calculatrice1)
calculatrice2 = input("Saissisez le deuxième nombre afin de réaliser une addition")
deuxieme_nombre = int(calculatrice2)
somme = (premier_nombre) + (deuxieme_nombre)
calcul_final = f"Le résultat de l'addition du nombre {premier_nombre} avec le nombre {deuxieme_nombre} est égal à {somme}"
print(calcul_final)

#code correction :
a = input("Entrez un premier nombre : ")
b = input("Entrez un deuxième nombre : ")
print(f"Le résultat de l'addition de {a} avec {b} est égal à {int(a) + int(b)}")
