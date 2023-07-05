# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:24:47 2023

@author: pagro
"""


from IPython.display import display 
import pandas as pd
import numpy as np

tableau_Cg_segments = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_35_points/3_Tableaux_excel/4_Positions_Cg_segments.xlsx', header = [0,1]) # Chemin d'accès au fichier .xlsx avec choix des lignes correspondant à nos headers
tableau_Cg_segments = tableau_Cg_segments.drop(tableau_Cg_segments.index[[0,1]]) # Enlève les 2 premières lignes qui ne servent à rien (je ne sais pas pourquoi elles sont là)
tableau_Cg_segments = tableau_Cg_segments.drop(tableau_Cg_segments.columns[[0]], axis = 1) # Enlève la première colonne qui ne sert à rien (je ne sais pas pourquoi elle est là)

# On va créer un nouveau tableau

tableau_accelerations_Cg_segments = tableau_Cg_segments.iloc[:, :2]     # Permet d'avoir les colonnes "Frame" et "Temps" dans un premier temps
tableau_accelerations_Cg_segments = tableau_accelerations_Cg_segments.drop(tableau_accelerations_Cg_segments.index[[0,1]])     # Permet d'enlever les 2 premières lignes car lors de l'estimation de la dérivée via les calculs différentiels, nous ne pouvons pas obtenir de valeurs pour les premières et dernières données. ( on ne se soucie pas des dernières données car np.diff ne fait pas ([x]i+1) - [x]i avec des valeurs extérieures au tableau)

x = 2 

for x in range(2, tableau_Cg_segments.shape[1]):     # La boucle commence à partir de la 3ème colonne et va jusqu'à la dernière (sans passer par la colonne "Frame" et "Time" au début)
    try:
        temps = tableau_Cg_segments.iloc[:,1]     # Permet d'obtenir les valeurs de la colonne temps (où index = 1)
        position = tableau_Cg_segments.iloc[:,x]     # Permet d'obtenir les valeurs des positions mesurées colonne après colonne
         
        ### Calcul des des dérivées via la méthode des différences finies ###
        
        # Calcul de la première dérivée ##
        dx = np.diff(temps)     # np.diff ne va pas faire de calcul pour la dernière valeur du tableau. Ce qui veut dire que pour une colonne de 128 valeurs initiales, nous aurons après exécution de cette ligne 127 valeurs.
        dy = np.diff(position)
        first_derivative = dy / dx
        
        #print(first_derivative)
        #print(len(first_derivative))
        
        ## Calcul de la seconde dérivée ##
        dx2 = np.diff(temps[1:])
        dy2 = np.diff(first_derivative)
        second_derivative = dy2 / dx2
        
        #print(second_derivative)
        #print(len(second_derivative))
        
        tableau_accelerations_Cg_segments.insert(x, f'{tableau_Cg_segments.columns[x]}', second_derivative)
        
        x += 1     # Permet le passage de colonne en colonne pour les positions
    except IndexError:     # Empêche le blocage du programme lorsque x a une valeur supérieure au nombre de colonnes du tableau à la fin de la boucle
        print(f"Column index {x} is out of bounds.") 
        
        
tableau_accelerations_Cg_segments.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_35_points/3_Tableaux_excel/5_Accélérations_Cg_segments.xlsx')       
