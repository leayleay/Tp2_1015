# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.
import math
import random

def entiersrandom(): 
   listRandom = []
   for _ in range(5):
    valeur = math.floor(20*random.random() + 1)
    listRandom.append(valeur)

   return listRandom 
    

def matcherVars(symboles, listRandom):
   listMatch = []
   for i in range(5):
    var = []
    var += (symboles[i], listRandom[i])
    listMatch.append(var)

   return listMatch
    

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
      <div id="jeu">
      <table>\n
      """
   

   for i in range(5):
    sousliste = grille[i]
    html += """<tr>\n"""
    for item in sousliste:
        html += """<td id="case""" + str(caseNbre) + """">""" + """<img src="symboles/""" + str(item) + """.svg"></td>\n"""
        caseNbre += 1
    html += """<td>""" + str(listeSommesRangee[i]) + """</td>\n"""
    html += """</tr>\n"""  

    html += """<tr>\n"""  
   for sommeCol in listeSommesCols:
      html += """<td>""" + str(sommeCol) + """</td>\n"""
   html += """<td></td>\n</tr>\n""" 
   html += """</table></div>"""  

   return html

def init():
    symboles = ["penta", "pyramide", "cube", "star","circle"]
    listEntiers = entiersrandom()
    grille = creerGrille(symboles)
    listeSommesRangee, listeSommesCols = afficherSommes(listEntiers, grille, symboles) 

    main = document.querySelector("#main")
    main.innerHTML = changerHTML(grille, listeSommesCols, listeSommesRangee)