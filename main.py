import random

def pa_pi_ci():
    choix_joueur = input("veuillez entrer un choix (papier, pierre, ciseaux) : ")
    choix_possible = ["papier","pierre","ciseaux"]
    choix_robot = random.choice(choix_possible)

    if choix_joueur == choix_robot :
        print("Egalité")
    elif (choix_joueur == "papier" and choix_robot == "pierre") or \
        (choix_joueur == "pierre" and choix_robot == "ciseaux") or (choix_joueur == "ciseaux" and choix_robot == "papier"):
        print("vous avez gagner")
    else:
        print("l'ordinateur à gagné")

pa_pi_ci()