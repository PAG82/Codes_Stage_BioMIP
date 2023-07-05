# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:24:47 2023

@author: pagro
"""
globals().clear()      # Supprime toutes les variables pour me permettre de relancer le code lorsque je veux faire de nouveaux essais

import pandas as pd
import numpy as np

tableau_Cg_segments = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/3_Positions_Cg_segments.xlsx', header = [0]) # Chemin d'accès au fichier .xlsx avec choix des lignes correspondant à nos headers

### On va créer un nouveau tableau contenant la colonne "Temps" et les accélérations ###

tableau_accelerations_Cg_segments = tableau_Cg_segments.iloc[:, 1]     # Permet d'avoir la colonne "Temps" dans un premier temps
tableau_accelerations_Cg_segments = tableau_accelerations_Cg_segments.drop(tableau_accelerations_Cg_segments.index[[0,1]])     # Permet d'enlever les 2 premières lignes car lors de l'estimation de la dérivée via les calculs différentiels, nous ne pouvons pas obtenir de valeurs pour les premières et dernières données. ( on ne se soucie pas des dernières données car np.diff ne fait pas ([x]i+1) - [x]i avec des valeurs extérieures au tableau)
tableau_accelerations_Cg_segments = pd.DataFrame(tableau_accelerations_Cg_segments)     # On convertit la série en DataFrame permettant les insertions de nouvelles colonnes plus loin

x = 2 

for x in range(2, tableau_Cg_segments.shape[1]):     # La boucle commence à partir de la 3ème colonne et va jusqu'à la dernière (sans passer par la colonne "Time" au début)
    try:
        temps = tableau_Cg_segments.iloc[:,1]     # Permet d'obtenir les valeurs de la colonne temps (où index = 1)
        position = tableau_Cg_segments.iloc[:,x]     # Permet d'obtenir les valeurs des positions mesurées colonne après colonne
         
        ### Calcul des des dérivées via la méthode des différences finies ###
        
        ## Calcul de la première dérivée ##
        dx = np.diff(temps)     # np.diff ne va pas faire de calcul pour la dernière valeur du tableau. Ce qui veut dire que pour une colonne de 128 valeurs initiales, nous aurons après exécution de cette ligne 127 valeurs.
        dy = np.diff(position)
        first_derivative = dy / dx
        
        #print(first_derivative)
        #print(len(first_derivative))
        
        ## Calcul de la seconde dérivée ##
        dx2 = np.diff(temps[1:])     # On prend à partir de la ligne 1 et pas 0 car nous n'avons plus de données pour la première ligne (car on a déjà fait des calculs de différences avant donc on se retrouve avec un élément en moins)
        dy2 = np.diff(first_derivative)
        second_derivative = dy2 / dx2
        
        #print(second_derivative)
        #print(len(second_derivative))
        
        
        tableau_accelerations_Cg_segments.insert(x-1, f'{tableau_Cg_segments.columns[x]}', second_derivative)
        
        x += 1     # Permet le passage de colonne en colonne pour les positions
    except IndexError:     # Empêche le blocage du programme lorsque x a une valeur supérieure au nombre de colonnes du tableau à la fin de la boucle
        print(f"Column index {x} is out of bounds.") 
        
        
tableau_accelerations_Cg_segments.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/4_Accélérations_Cg_segments.xlsx')       

print("Opération terminée")