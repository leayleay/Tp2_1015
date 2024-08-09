# Fichier: TP2.py
# Auteurs: Léa H. et Grace T.
# Date: 2024-08-08

# Ce programme imite le comportement du jeu "La somme des symboles". Le but du joueur est de rechercher les nombres 
# associés à cinq symboles dans une grille 5 x 5. À la fin de chaque rangée et de chaque colonne se trouvent les sommes
# des cinq chiffres au total.  

import math
import random

# Fonction qui conçoit au hasard cinq entiers entre 1 et 20 
def entiersrandom(): 
   listRandom = []
   for _ in range(5):
    valeur = math.floor(20*random.random() + 1)
    listRandom.append(valeur)

   return listRandom 
    

# Fonction qui crée une liste contenant cinq sous-listes de symboles 
# qui sert de base pour la grille 
def creerGrille(symboles):
    grille = []
    for _ in range(5):
        rangee = []
        for _ in range(5):
            index = math.floor(4*random.random() + 1)
            symbole = symboles[index]
            rangee.append(symbole)
        grille.append(rangee)
    
    return grille


# Fonction
def afficherSommes(listEntiers, grille, symboles):
    listeSommesRangee = []
    for rangee in grille:
        somme = 0
        for symbole in rangee:
            somme += retournerValeur(listEntiers, symboles, symbole)
        listeSommesRangee.append(somme)

    listeSommesCols = []
    for j in range(5): 
        somme = 0
        for i in range(5):
          somme += retournerValeur(listEntiers, symboles, grille[i][j])
        listeSommesCols.append(somme)      

    return listeSommesRangee, listeSommesCols  

def retournerValeur(listMatch, symboles, symbole):
   for i in range(5):
      if symboles[i] == symbole :
         return listMatch[i]

def changerHTML(grille, listeSommesCols, listeSommesRangee): 
   caseNbre = 0
   html = """
      <style>
        #jeu table { float: none; }
        #jeu table td {
            border: 1px solid black; 
            padding: 1px 2px;
            width: 80px;
            height: 80px;
            font-family: Helvetica; 
            font-size: 20px; 
            text-align: center;
        }
        #jeu table td img {
            display: block;
            margin-left: auto;
            margin-right: auto;
            object-fit: contain;
            width: 80%;
            height: 80%;
        }
      </style>
      <button onclick="init()">Nouvelle partie</button>
      <div id="jeu">
      <table>\n
      """
   

   for i in range(5):
    sousliste = grille[i]
    html += """<tr>\n"""
    for item in sousliste:
        html += """<td id="case""" + str(caseNbre) + """" onclick="clic()"><img src="symboles/""" + str(item) + """.svg"></td>\n"""
        caseNbre += 1
    html += """<td>""" + str(listeSommesRangee[i]) + """</td>\n"""
    html += """</tr>\n"""  

    html += """<tr>\n"""  
   for sommeCol in listeSommesCols:
      html += """<td>""" + str(sommeCol) + """</td>\n"""
   html += """<td></td>\n</tr>\n""" 
   html += """</table></div>"""  

   return html

def clic():
    valeur = input("Entrez un nombre entre 1 et 20:")
    
   
   

def init():
    symboles = ["penta", "pyramide", "cube", "star","circle"]
    listEntiers = entiersrandom()
    grille = creerGrille(symboles)
    listeSommesRangee, listeSommesCols = afficherSommes(listEntiers, grille, symboles) 

    main = document.querySelector("#main")
    main.innerHTML = changerHTML(grille, listeSommesCols, listeSommesRangee)