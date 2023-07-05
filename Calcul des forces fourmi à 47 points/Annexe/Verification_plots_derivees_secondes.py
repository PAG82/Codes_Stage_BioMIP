# -*- coding: utf-8 -*-
"""
Created on Fri May 26 15:16:54 2023

@author: pagro
"""
globals().clear()      # Supprime toutes les variables pour me permettre de relancer le code lorsque je veux faire de nouveaux essais

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tableau_Cg_segments = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/3_Positions_Cg_segments.xlsx', header = [0]) # Chemin d'accès au fichier .xlsx avec choix des lignes correspondant à nos headers

# On va créer les graphes révélant l'accélération des Cg des segments en fonction du temps

x = 2 
num_affichage =1

for x in range(2, tableau_Cg_segments.shape[1]):     # La boucle commence à partir de la 3ème colonne et va jusqu'à la dernière (sans passer par la colonne "Frame" et "Time" au début)
    try:
        temps = tableau_Cg_segments.iloc[:,1]     # Permet d'obtenir les valeurs de la colonne temps (où index = 1)
        position = tableau_Cg_segments.iloc[:,x]     # Permet d'obtenir les valeurs des positions mesurées colonne après colonne
         
        ### Calcul des des dérivées via la méthode des différences finies ###
        
        # Calcul de la première dérivée
        dx = np.diff(temps)
        dy = np.diff(position)
        first_derivative = dy / dx
        
        #print(first_derivative)
        #print(len(first_derivative))

        # Calcul de la seconde dérivée
        dx2 = np.diff(temps[1:])
        dy2 = np.diff(first_derivative)
        second_derivative = dy2 / dx2
        

        temps_for_plot = temps.drop(temps.index[[0,1]])   # On élimine les 2 premières lignes car on n'a pas de valeurs pour ces dernières à cause des 2 dérivées successives que l'ont fait
        
        
        plt.figure(figsize = (20, 14)) 
        plt.plot(temps_for_plot, second_derivative, label='accélération Cg')
        plt.title('accélération des Cg segmentaires en fonction du temps')   # titre
        plt.xlabel('Temps (s)')   # axe x
        plt.ylabel(f'Accélértion {tableau_Cg_segments.columns[x]} en mm/s^2')    #axe y
        plt.legend()   # légende
        filename = f"{num_affichage}"
        plt.savefig(f'C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/4_Graphiques/3_Graphiques_accelerations/{filename}.png') # sauvegarde du graphe
        plt.show()
        
        
        
        num_affichage += 1 
        x += 1     # Permet le passage de colonne en colonne pour les positions
    except IndexError:     # Empêche le blocage du programme lorsque x a une valeur supérieure au nombre de colonnes du tableau à la fin de la boucle
        print(f"Column index {x} is out of bounds.") 
        