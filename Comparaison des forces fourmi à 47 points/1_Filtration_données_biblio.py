# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:57:59 2023

@author: pagro
"""

globals().clear()

import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt

tableau_biblio = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/1_Data_Bibliographie/Data_Reinhardt&Blickhan-JExpBiol-2014b/optimisation_tableau_Reinhardt_2014b.xlsx')

temps = tableau_biblio.iloc[:,0] * 0.01
x = 0
num_affichage = 1

for col in range(1, tableau_biblio.shape[1]):     # Toutes les colonnes vont être traitées sauf la première
    position = tableau_biblio.iloc[:,col]   # Permet d'obtenir les valeurs des positions mesurées colonne après colonne
    x += 1   # Permet le passage de colonne en colonne pour les positions
    position = tableau_biblio.iloc[:,x]   # Permet d'obtenir les valeurs des positions mesurées colonne après colonne
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
    plt.xlabel('Temps (s)')   # axe x
    plt.ylabel(f'Force {tableau_biblio.columns[x]} (normalisée au poids du corps)')    # axe y
    plt.legend()     # légende
    filename = f"{num_affichage}. {tableau_biblio.columns[x]}"      # J'incrémente le numéro d'affichage pour pouvoir avoir les graphes dans l'ordre de création dans mon document
    num_affichage += 1 
    plt.savefig(f'C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/3_Comparaison_forces_de_réaction_47_points/4_Graphiques/3_Graphes_données_filtrées/{filename}.png') # sauvegarde du graphe
    plt.show()
    tableau_biblio.iloc[:, col] = position_filtree    # Permet de remplacer la colonne de données avec les nouvelles données filtrées pour pouvoir enregistrer le tableur par la suite
     #i += 1     ## Utile pour analyse rapide
     
#### On doit modifier le tableau pour que le système utilisé dans la biblio soit le même que celui de notre fourmi ###
# Le sens des axes de X et Y sont inversés (voir article "Reinhardt&Blickhan-JExpBiol-2014b") donc on va modifier le signe pour les forces latérales et ant-post

tableau_biblio.iloc[:, 1], tableau_biblio.iloc[:, 4], tableau_biblio.iloc[:, 7]  = - tableau_biblio.iloc[:, 1], -tableau_biblio.iloc[:, 4], - tableau_biblio.iloc[:, 7]     # je modifie ici le signe des forces ant-post
tableau_biblio.iloc[:, 2], tableau_biblio.iloc[:, 5], tableau_biblio.iloc[:, 8]  = - tableau_biblio.iloc[:, 2], -tableau_biblio.iloc[:, 5], - tableau_biblio.iloc[:, 8]     # je modifie ici le signe des forces latérales

tableau_biblio.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/3_Comparaison_forces_de_réaction_47_points/3_Tableaux_excel/1_Données_filtrées.xlsx')