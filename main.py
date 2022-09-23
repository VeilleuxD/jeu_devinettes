"""
nom: David A. Veilleux
Groupe: 405
Description: Un petit jeu ou le joueur doit deviner le nombre choisi aléatoirement entre 1 et 100.

"""

import random


jouer = True


while jouer:
    borne_min = 0
    borne_max = 100

    number = random.randint(borne_min, borne_max)
    nbr_essai = 0

# plus tard je donnera la possibilité de choisir les bornes
    print("J'ai choisi un nombre entre " + str(borne_min) + " et " + str(borne_max) + ". À vous de le trouver!")

# Merci Cabana
    while (answer := int(input("\nInsérez votre réponse ici! \n-->"))) != number:

        if answer < number:
            print("La réponse est plus grande")

        elif answer > number:
            print("la réponse est plus petite!")

        nbr_essai = nbr_essai + 1

    print("Voilà la bonne réponse! C'était bien " + str(number) + "!")
    print("Vous avez réussi en " + str(nbr_essai) + " essai(s)!")
    leave = input("\n\nVoulez-vous jouer encore? y/n\n-->")
    if leave == "y":
        jouer = True
    else:
        print("Merci d'avoir joué!\n:)")

        jouer = False
