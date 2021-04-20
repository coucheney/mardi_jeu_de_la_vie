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

# liste à deux dimensions telle que tableau[i][j] vaut 0
# si la case (i, j) est morte
# et vaut l'identifiant du carré dessiné à la case (i, j) sinon
tableau = []
val = 0
delai = 100


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
    """Retourne la colonne et la ligne correspondant au
       point du canevas de coordonnées (x,y)"""
    return x // COTE, y // COTE


def change_carre(event):
    """Change la couleur du carre à la position (event.x, event.y)"""
    i, j = xy_to_ij(event.x, event.y)
    if tableau[i][j] == 0:
        x = i * COTE
        y = j * COTE
        carre = canvas.create_rectangle((x, y),
                                        (x + COTE, y + COTE),
                                        fill=COULEUR_CARRE,
                                        outline=COULEUR_QUADR
                                        )
        tableau[i][j] = carre
    else:
        canvas.delete(tableau[i][j])
        tableau[i][j] = 0


def nb_vivant(i, j):
    """Retourner le nombre de cases voisines vivantes
       de la case de coordonnées (i, j)"""
    cpt = 0
    for k in range(max(0, i-1), min(NB_COL, i+2)):
        for el in range(max(0, j-1), min(NB_LIG, j+2)):
            if tableau[k][el] != 0 and [k, el] != [i, j]:
                cpt += 1
    return cpt


def etape_ij(i, j):
    """Fait une étape du jeu de la vie pour la case de coordonnées (i, j):
    retourne la nouvelle valeur à mettre dans le tableau
    """
    n = nb_vivant(i, j)
    if tableau[i][j] == 0:
        # si la case est morte
        if n == 3:
            x = i * COTE
            y = j * COTE
            return canvas.create_rectangle((x, y),
                                           (x + COTE, y + COTE),
                                           fill=COULEUR_CARRE,
                                           outline=COULEUR_QUADR
                                           )
        else:
            return 0
    else:
        # si la case est vivante
        if n == 3 or n == 2:
            return tableau[i][j]
        else:
            canvas.delete(tableau[i][j])
            return 0


def etape():
    """Fait une étape du jeu de la vie"""
    global tableau
    # copie du tableau
    tableau_res = copy.deepcopy(tableau)
    # traiter toutes les cases du tableau
    for i in range(NB_COL):
        for j in range(NB_LIG):
            tableau_res[i][j] = etape_ij(i, j)
    # on modifie le tableau global
    tableau = tableau_res


def etape_n(event):
    """Appelle la fonction étape sans l'argument event"""
    etape()


def charger():
    """charger la grille depuis le fichier sauvegarde.txt"""
    global tableau
    fic = open("sauvegarde.txt", "r")
    canvas.delete("all")
    quadrillage()
    j = 0
    for ligne in fic:
        i = 0
        val = ligne.split()
        for e in val:
            if e == "0":
                tableau[i][j] = 0
            else:
                x = i * COTE
                y = j * COTE
                carre = canvas.create_rectangle((x, y),
                                                (x + COTE, y + COTE),
                                                fill=COULEUR_CARRE,
                                                outline=COULEUR_QUADR
                                                )
                tableau[i][j] = carre
            i += 1
        j += 1
    fic.close()


def sauvegarder():
    """sauvegarder la grille vers le fichier sauvegarde.txt"""
    fic = open("sauvegarde.txt", "w")
    for j in range(NB_LIG):
        for i in range(NB_COL):
            if tableau[i][j] == 0:
                fic.write("0 ")
            else:
                fic.write("1 ")
        fic.write("\n")
    fic.close()


def start():
    """Démarre l'animation du jeu de la vie"""
    global id_after
    etape()
    id_after = racine.after(delai, start)


def start_stop():
    """Démarre ou arrête l'automate en changeant
       le nom du bouton correspondant"""
    global val
    if val == 0:
        bout_animation.config(text="arrêter")
        start()
    else:
        bout_animation.config(text="démarrer")
        racine.after_cancel(id_after)
    val = 1 - val


def augmente_delai(event):
    """augmente le delai entre 2 étapes de l'automate"""
    global delai
    if delai < 1000:
        delai += 10
        lbl_delai.config(text="Delai entre 2 étapes: " + str(delai) + "ms")


def diminue_delai(event):
    """diminue le delai entre 2 étapes de l'automate"""
    global delai
    if delai > 10:
        delai -= 10
        lbl_delai.config(text="Delai entre 2 étapes: " + str(delai) + "ms")


#####################
# programme principal

for i in range(NB_COL):
    tableau.append([0] * NB_LIG)

racine = tk.Tk()
racine.title("Jeu de la vie")

# création des widgets
canvas = tk.Canvas(racine, width=LARGEUR, height=HAUTEUR, bg=COULEUR_FOND)
lbl_delai = tk.Label(racine, text="Delai entre 2 étapes: " + str(delai) + "ms")
bout_charger = tk.Button(racine, text="charger", command=charger)
bout_sauv = tk.Button(racine, text="sauvegarder", command=sauvegarder)
bout_animation = tk.Button(racine, text="démarrer", command=start_stop)

# liaison des événements
canvas.bind("<Button-1>", change_carre)
racine.bind("n", etape_n)
racine.bind("p", augmente_delai)
racine.bind("m", diminue_delai)

# placement des widgets
canvas.grid(row=0, rowspan=3)
bout_charger.grid(row=0, column=1)
bout_sauv.grid(row=1, column=1)
bout_animation.grid(column=1, row=2)
lbl_delai.grid(row=3, column=0)

# programme principal
quadrillage()
racine.mainloop()
