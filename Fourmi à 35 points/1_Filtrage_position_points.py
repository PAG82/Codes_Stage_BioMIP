# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:54:35 2023

@author: pagro
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

# Chemin d'accès au fichier .xlsx avec choix des lignes correspondant à nos headers
tableau = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_35_points/1_Données_intiales_à_traiter/trc file to xlsx.xlsx', header = [3,4]) 


### On va ranger notre tableau pour pouvoir l'utiliser correctement ###

new_tableau = tableau.drop(tableau.index[[0]]) # On supprime la ligne qui ne contient aucune valeur dans le tableur
new_tableau = new_tableau.drop(('load'), axis=1, level =0) # On supprime également les colonnes "load" car nous n'avons aucune donnée 

# On supprime les colonnes Z36.1, Z36.2 Z36.3 qui n'ont pas de données (ça doit être malheureusement un reste des colonnes X37, Y37, Z37 que j'ai supprimé du tableur car il n'y avait pas de valeurs) 
new_tableau = new_tableau.drop(new_tableau.columns[len(new_tableau.columns)-3:], axis=1) 

# Crée un nouveau tableur avec les données qui nous intéresse (utile pour une meilleure visualisation dans excel)
new_tableau.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_35_points/3_Tableaux_excel/1_données_rangées.xlsx') 


### On va filtrer nos données, créer nos graphes et les sauvegarder ###

x = 1 
num_affichage = 1
i = 0
for x in range(1, new_tableau.shape[1]):
    try:
    #if (i < 3):    ## Utile pour analyse rapide
        temps = new_tableau.iloc[:,1]   # Permet d'obtenir les valeurs de la colonne temps (où index = 1)
        x += 1   # Permet le passage de colonne en colonne pour les positions
        position = new_tableau.iloc[:,x]   # Permet d'obtenir les valeurs des positions mesurées colonne après colonne
        plt.figure(figsize = (20, 14))   # Va permettre d'afficher plusieurs courbes sur une même figure
        
        
        # Filtre Butterworth
        fc = 4      # Permet de définir la fréquence de coupure
        nyquist_frequency = 0.5 * 1 / (temps[2] - temps[1])  # Permet le calcul de la fréquence de Nyquist
        normalized_cutoff = fc / nyquist_frequency # Nécessaire car le second argument de signal.butter (Wn) doit être entre 0 et 1 (on ne peut pas donc directement mettre fc (= 4 Hz))
        b, a = signal.butter(4, normalized_cutoff, btype='low', analog=False)
        position_filtree = signal.filtfilt(b, a, position)


        plt.plot(temps,position, label = 'données brutes')
        plt.plot(temps, position_filtree, c = 'red', label='Filtre Butterworth')

        
        plt.title('Low pass filtering impact on data')   # titre
        plt.xlabel('Temps (Hz)')   # axe x
        plt.ylabel(f'Position {new_tableau.columns[x]}')    #axe y
        plt.legend()   #légende
        filename = f"{num_affichage} ,{new_tableau.columns[x]}"
        num_affichage += 1 
        plt.savefig(f'C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_35_points/4_Graphiques/1_Graphiques_mesures_en_fonction du temps/{filename}.png') # sauvegarde du graphe
        plt.show()
        new_tableau.iloc[:, x] = position_filtree    # Permet de remplacer la colonne de données avec les nouvelles données filtrées pour pouvoir enregistrer le tableur par la suite
        #i += 1     ## Utile pour analyse rapide
    except IndexError:
        print(f"Column index {x} is out of bounds.")   
### On va créer un tableau excel avec les nouvelles données filtrées pour pouvoir les utiliser pour nos calculs des positions des centres de gravités segmentaires ###


new_tableau.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_35_points/3_Tableaux_excel/2_données_filtrées.xlsx') # Crée un nouveau tableur avec les données filtrées
