# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 17:14:56 2023

@author: pagro
"""

globals().clear()  

import matplotlib.pyplot as plt
import pandas as pd

### Je rentre les temps que j'ai relevés sur les vidéos (je les ai multipliés par 3 entre temps car les vidéos "brutes" ont été prises à 300 Hz mais le traitement a été ensuite fait à 100 Hz)

data = [
    ('Patte postérieure droite', [0, 0.93, 2.17, 3.16], [0.78, 1.87, 2.96, 3.69]),    # On a ici dans l'ordre : le nom, les temps pour lesquelles la fourmi pose sa patte sur le sol et les temps pour lesquelles la fourmi lève sa patte du sol 
    ('Patte médiane droite', [0, 0.37, 1.28, 2.5, 3.54], [0.15, 1.06, 2.3, 3.3, 3.69]),
    ('Patte antérieure droite', [0, 0.87, 2.01, 3.09], [0.53, 1.71, 2.8, 3.69]),
    ('Patte postérieure gauche', [0, 0.51, 1.49, 2.66], [0.34, 1.26, 2.46, 3.59]),
    ('Patte médiane gauche', [0, 0.89, 2, 3.05], [0.66, 1.65, 2.75, 3.69]),
    ('Patte antérieure gauche', [0, 0.430, 1.4, 2.6, 3.65], [0.17, 1.06, 2.19, 3.29, 3.69])     
]

noms = [item[0] for item in data]      # Permet de prendre tous les noms des pattes dans les tuples faits auparavant 

tableau_force = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/5_Forces_de_reaction_normalisées.xlsx')      # On récupère les données de force pour notre fourmi 
tableau_force = tableau_force[(tableau_force['Time'] >= 0.5) & (tableau_force['Time'] <= 3.2)] # On fait un booléen pour ne garder les valeurs entre 0.5 et 3.2 pour le temps avec leur valeur de force respective car on ne veut pas le début et la fin de l'acquisition

tableau_biblio = pd.read_excel('C:/Users\pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/3_Comparaison_forces_de_réaction_47_points/3_Tableaux_excel/2_Tableau_forces_comparaison_biblio.xlsx')

colonne_temps = tableau_force.iloc[:, 1]     # On récupère la colonne "Temps" 
index = 2
i = 2

### Création de nos 2 graphiques ###
for column_name in tableau_force.columns[index:]:
    fig, (ax1, ax2) = plt.subplots(2,1, figsize = (15,12))     
    
    ### D'abbord on crée le stride pattern ###
    
    for item in data:     # Permet de prendre une par une les listes qui nous intéresse dans chaque tuples 
        pose = item[1]
        leve = item[2]
        for p, l in zip(pose, leve):
            ax1.hlines(noms.index(item[0]), p, l)     # Permet de tracer chaque lignes horizontales
    
    ax1.margins(0.05)     # Permet une meilleure présentation
    ax1.set(yticks=range(len(noms)), yticklabels=noms, xlabel='Temps (s)')     #     Permet de modifier les axes
    ax1.title.set_text('Stepping pattern')
    ax1.grid(axis='x')
    
    ### Puis on crée les graphiques de nos forces et celles de la biblio en fonction du temps ###

    colonne_force = tableau_force[column_name]  # On extrait les données de la colonne en fonction du nom pour notre fourmi
    colonne_biblio = tableau_biblio.iloc[:,i]     # On extrait les données de la colonne en fonction du nom pour la fourmi de la biblio
    ax2.plot(colonne_temps, colonne_force, label = 'Données pour Messor Barbarus')
    ax2.plot(colonne_temps, colonne_biblio, label ='Données tirées de la littérature')
    
    ax2.set_title("Comparaison des forces de réactions du sol entre Messor Barbarus et les données de la bibliographie dans l'espace et en fonction du temps")
    ax2.set_xlabel('Temps (s)')
    force_nom = f"{tableau_force.columns[index]}"
    ax2.set_ylabel(f"{force_nom} (normalisée au poids du corps)")
    plt.legend()
    plt.savefig(f'C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/3_Comparaison_forces_de_réaction_47_points/4_Graphiques/2_Graphes_comparaison/Graphiques {force_nom}.png')
    
    index += 1
    i += 1
    
    plt.show()