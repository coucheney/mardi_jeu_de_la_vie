####################################################
# Auteurs: 
# Pierre Coucheney
# Toto
# Groupe:
# BI 5
# https://github.com/coucheney/mardi_jeu_de_la_vie
###################################################

#####################
# import des modules

import tkinter as tk
import copy


#####################
# constantes

HAUTEUR = 400
LARGEUR = 600
COTE = 20
NB_COL = LARGEUR // COTE
NB_LIG = HAUTEUR // COTE

COULEUR_QUADR = "grey20"
COULEUR_FOND = "grey60"
COULEUR_CARRE = "yellow"



######################
# variables globales

# liste à deux dimensions telle que tableau[i][j] vaut 0 si la case (i, j) est morte
# et vaut l'identifiant du carré dessiné à la case (i, j) sinon
tableau = []



###################
# fonctions

def quadrillage():
    """Dessine un quadrillage dans le canevas avec des carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    i = 0
    while i * COTE <= LARGEUR:
        x = i * COTE
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        i += 1


def xy_to_ij(x, y):
    """Retourne la colonne et la ligne correspondant au point du canevas de coordonnées (x,y)"""
    return x // COTE, y // COTE


def change_carre(event):
    """Change la couleur du carre à la position (event.x, event.y)"""
    i, j = xy_to_ij(event.x, event.y)
    if tableau[i][j] == 0:
        x = i * COTE
        y = j * COTE
        carre = canvas.create_rectangle((x, y), (x + COTE, y + COTE), fill=COULEUR_CARRE, outline=COULEUR_QUADR)
        tableau[i][j] = carre
    else:
        canvas.delete(tableau[i][j])
        tableau[i][j] = 0


def nb_vivant(i, j):
    """Retourner le nombre de cases voisines vivantes de la case de coordonnées (i, j)"""
    return 0


def etape_ij():
    """Fait une étape du jeu de la vie pour la case de coordonnées (i, j):
    retourne la nouvelle valeur à mettre dans le tableau
    """
    return 0


def etape():
    """Fait une étape du jeu de la vie"""
    global tableau
    # copie du tableau
    tableau_res = copy.deepcopy(tableau)
    # traiter toutes les cases du tableau
    for i in range(NB_LIG):
        for j in range(NB_COL):
            tableau_res[i][j] = etape_ij()
    # on modifie le tableau global
    tableau = tableau_res




#####################
# programme principal

for i in range(NB_LIG):
    tableau.append([0] * NB_COL)

racine = tk.Tk()
racine.title("Jeu de la vie")

# création des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND)

# placement des widgets
canvas.grid(row=0)

# liaison des événements
canvas.bind("<Button-1>", change_carre)


quadrillage()



racine.mainloop()


