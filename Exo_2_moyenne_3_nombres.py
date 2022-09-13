#Calculer la moyenne de 3 nombres donnés

somme = 0
compteur = 0
while compteur < 3:
    nombre = float(input())
    somme += nombre
    compteur += 1
moyenne = somme / 3
print(moyenne)