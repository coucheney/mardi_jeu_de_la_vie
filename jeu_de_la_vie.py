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


#####################
# constantes

HAUTEUR = 400
LARGEUR = 600
COULEUR_FOND = "grey60"
COTE = 10
COULEUR_QUADR = "grey20"


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


def xy_to_cl(x, y):
    """Retourne la colonne et la ligne correspondant au point du canevas de coordonnées (x,y)"""
    pass


def change_carre(event):
    """Change la couleur du carre à la position (event.x, event.y)"""
    pass



#####################
# programme principal

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


