# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 15:42:26 2023

@author: pagro
"""

globals().clear()

import pandas as pd
import matplotlib.pyplot as plt


### On crée une fonction qui va nous permettre de facilement accéder à la matrice des masses ###
def acces_matrice_masse(colonne_masse, ligne_masse): 

# 1. On crée d'abord le nom des colonnes et des lignes
    nom_colonnes_masse = ['Front', 'Middle', 'Hind']
    nom_lignes_masse = ['Head', 'Thorax', 'Petiole + Abdomen', 'Coxa', 'Trochanter', 'Femur', 'Tibia', 'Tarsus']

    matrice_masse = {}     # Permet de créer un dictionnaire qui va être utilisé pour stocker les différentes valeurs

    for i in nom_colonnes_masse:
        matrice_masse[i] = []     # Chaque nom de lignes va correspondre à une clé du dictionnaire

# 2. On rentre les différentes valeurs
    matrice_masse['Front'] = [0.0026, 0.001, 0.0037, 0.001, 5.3E-6, 6.75E-5, 3.98E-6, 1.89E-5]
    matrice_masse['Middle'] = [0, 0, 0, 4.29E-5, 2.70E-6, 5.51E-5, 3.83E-5, 2.77E-5]
    matrice_masse['Hind'] = [0, 0, 0, 5.63E-5, 3.87E-6, 9.11E-5, 4.2E-5, 1.96E-5]

# 3. On récupère la masse qui nous intéresse
    valeur_masse = matrice_masse[colonne_masse][nom_lignes_masse.index(ligne_masse)]     # On va chercher la masse du segment qui nous intéresse 
    return valeur_masse

### On crée une fonction qui va nous permettre de facilement accéder à la matrice des accélérations ###
def acces_matrice_acceleration(colonne_acceleration):
   
    valeur_acceleration = tableau_acceleration[colonne_acceleration].values
    return valeur_acceleration

tableau_acceleration =  pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/4_Accélérations_Cg_segments.xlsx')


colonne_temps = tableau_acceleration.iloc[:, 1]     # Permet de récupérer la colonne "Temps"

### On calcule la force ###

force_x = acces_matrice_masse('Front', 'Head') * acces_matrice_acceleration('head_x') + acces_matrice_masse('Front', 'Thorax') * acces_matrice_acceleration('thorax_x') + acces_matrice_masse('Front', 'Petiole + Abdomen') * acces_matrice_acceleration('petiole_abdomen_x')
+  acces_matrice_masse('Front', 'Coxa') * acces_matrice_acceleration('fl_coxa_x') + acces_matrice_masse('Front', 'Trochanter') * acces_matrice_acceleration('fl_trochanter_x') + acces_matrice_masse('Front', 'Femur') * acces_matrice_acceleration('fl_femur_x') + acces_matrice_masse('Front', 'Tibia') * acces_matrice_acceleration('fl_tibia_x') + acces_matrice_masse('Front', 'Tarsus') * acces_matrice_acceleration('fl_tarse_metatarse_x') + acces_matrice_masse('Front', 'Coxa') * acces_matrice_acceleration('fr_coxa_x') + acces_matrice_masse('Front', 'Trochanter') * acces_matrice_acceleration('fr_trochanter_x') + acces_matrice_masse('Front', 'Femur') * acces_matrice_acceleration('fr_femur_x') + acces_matrice_masse('Front', 'Tibia') * acces_matrice_acceleration('fr_tibia_x') + acces_matrice_masse('Front', 'Tarsus') * acces_matrice_acceleration('fr_tarse_metatarse_x')
+ acces_matrice_masse('Middle', 'Coxa') * acces_matrice_acceleration('ml_coxa_x') + acces_matrice_masse('Middle', 'Trochanter') * acces_matrice_acceleration('ml_trochanter_x') + acces_matrice_masse('Middle', 'Femur') * acces_matrice_acceleration('ml_femur_x') + acces_matrice_masse('Middle', 'Tibia') * acces_matrice_acceleration('ml_tibia_x') + acces_matrice_masse('Middle', 'Tarsus') * acces_matrice_acceleration('ml_tarse_metatarse_x') +  acces_matrice_masse('Middle', 'Coxa') * acces_matrice_acceleration('mr_coxa_x') + acces_matrice_masse('Middle', 'Trochanter') * acces_matrice_acceleration('mr_trochanter_x') + acces_matrice_masse('Middle', 'Femur') * acces_matrice_acceleration('mr_femur_x') + acces_matrice_masse('Middle', 'Tibia') * acces_matrice_acceleration('mr_tibia_x') + acces_matrice_masse('Middle', 'Tarsus') * acces_matrice_acceleration('mr_tarse_metatarse_x')
+ acces_matrice_masse('Hind', 'Coxa') * acces_matrice_acceleration('rl_coxa_x') + acces_matrice_masse('Hind', 'Trochanter') * acces_matrice_acceleration('rl_trochanter_x') + acces_matrice_masse('Hind', 'Femur') * acces_matrice_acceleration('rl_femur_x') + acces_matrice_masse('Hind', 'Tibia') * acces_matrice_acceleration('rl_tibia_x') + acces_matrice_masse('Hind', 'Tarsus') * acces_matrice_acceleration('rl_tarse_metatarse_x') +  acces_matrice_masse('Hind', 'Coxa') * acces_matrice_acceleration('rr_coxa_x') + acces_matrice_masse('Hind', 'Trochanter') * acces_matrice_acceleration('rr_trochanter_x') + acces_matrice_masse('Hind', 'Femur') * acces_matrice_acceleration('rr_femur_x') + acces_matrice_masse('Hind', 'Tibia') * acces_matrice_acceleration('rr_tibia_x') + acces_matrice_masse('Hind', 'Tarsus') * acces_matrice_acceleration('rr_tarse_metatarse_x')

force_x = force_x *1E-3 * 1E6     
# "1E-3" c'est pour bien avoir des Newton à partir des valeurs de "force_x". Car "force_x" sont des valeurs en mg.mm.s^-2 donc 10^-3 N.
# "1E6" c'est pour obtenir au final des µN. J'aurais pû écrire "1E3" directement mais je trouve ça mieux pour comprendre le raisonnement.

force_y = acces_matrice_masse('Front', 'Head') * acces_matrice_acceleration('head_y') + acces_matrice_masse('Front', 'Thorax') * acces_matrice_acceleration('thorax_y') + acces_matrice_masse('Front', 'Petiole + Abdomen') * acces_matrice_acceleration('petiole_abdomen_y') 
+  acces_matrice_masse('Front', 'Coxa') * acces_matrice_acceleration('fl_coxa_y') + acces_matrice_masse('Front', 'Trochanter') * acces_matrice_acceleration('fl_trochanter_y') + acces_matrice_masse('Front', 'Femur') * acces_matrice_acceleration('fl_femur_y') + acces_matrice_masse('Front', 'Tibia') * acces_matrice_acceleration('fl_tibia_y') + acces_matrice_masse('Front', 'Tarsus') * acces_matrice_acceleration('fl_tarse_metatarse_y') + acces_matrice_masse('Front', 'Coxa') * acces_matrice_acceleration('fr_coxa_y') + acces_matrice_masse('Front', 'Trochanter') * acces_matrice_acceleration('fr_trochanter_y') + acces_matrice_masse('Front', 'Femur') * acces_matrice_acceleration('fr_femur_y') + acces_matrice_masse('Front', 'Tibia') * acces_matrice_acceleration('fr_tibia_y') + acces_matrice_masse('Front', 'Tarsus') * acces_matrice_acceleration('fr_tarse_metatarse_y')
+ acces_matrice_masse('Middle', 'Coxa') * acces_matrice_acceleration('ml_coxa_y') + acces_matrice_masse('Middle', 'Trochanter') * acces_matrice_acceleration('ml_trochanter_y') + acces_matrice_masse('Middle', 'Femur') * acces_matrice_acceleration('ml_femur_y') + acces_matrice_masse('Middle', 'Tibia') * acces_matrice_acceleration('ml_tibia_y') + acces_matrice_masse('Middle', 'Tarsus') * acces_matrice_acceleration('ml_tarse_metatarse_y') + acces_matrice_masse('Middle', 'Coxa') * acces_matrice_acceleration('mr_coxa_y') + acces_matrice_masse('Middle', 'Trochanter') * acces_matrice_acceleration('mr_trochanter_y') + acces_matrice_masse('Middle', 'Femur') * acces_matrice_acceleration('mr_femur_y') + acces_matrice_masse('Middle', 'Tibia') * acces_matrice_acceleration('mr_tibia_y') + acces_matrice_masse('Middle', 'Tarsus') * acces_matrice_acceleration('mr_tarse_metatarse_y')
+ acces_matrice_masse('Hind', 'Coxa') * acces_matrice_acceleration('rl_coxa_y') + acces_matrice_masse('Hind', 'Trochanter') * acces_matrice_acceleration('rl_trochanter_y') + acces_matrice_masse('Hind', 'Femur') * acces_matrice_acceleration('rl_femur_y') + acces_matrice_masse('Hind', 'Tibia') * acces_matrice_acceleration('rl_tibia_y') + acces_matrice_masse('Hind', 'Tarsus') * acces_matrice_acceleration('rl_tarse_metatarse_y') + acces_matrice_masse('Hind', 'Coxa') * acces_matrice_acceleration('rr_coxa_y') + acces_matrice_masse('Hind', 'Trochanter') * acces_matrice_acceleration('rr_trochanter_y') + acces_matrice_masse('Hind', 'Femur') * acces_matrice_acceleration('rr_femur_y') + acces_matrice_masse('Hind', 'Tibia') * acces_matrice_acceleration('rr_tibia_y') + acces_matrice_masse('Hind', 'Tarsus') * acces_matrice_acceleration('rr_tarse_metatarse_y')

force_y = force_y * 1E-3 * 1E6

force_z = acces_matrice_masse('Front', 'Head') * acces_matrice_acceleration('head_z') + acces_matrice_masse('Front', 'Thorax') * acces_matrice_acceleration('thorax_z') + acces_matrice_masse('Front', 'Petiole + Abdomen') * acces_matrice_acceleration('petiole_abdomen_z')
+  acces_matrice_masse('Front', 'Coxa') * acces_matrice_acceleration('fl_coxa_z') + acces_matrice_masse('Front', 'Trochanter') * acces_matrice_acceleration('fl_trochanter_z') + acces_matrice_masse('Front', 'Femur') * acces_matrice_acceleration('fl_femur_z') + acces_matrice_masse('Front', 'Tibia') * acces_matrice_acceleration('fl_tibia_z') + acces_matrice_masse('Front', 'Tarsus') * acces_matrice_acceleration('fl_tarse_metatarse_z') + acces_matrice_masse('Front', 'Coxa') * acces_matrice_acceleration('fr_coxa_z') + acces_matrice_masse('Front', 'Trochanter') * acces_matrice_acceleration('fr_trochanter_z') + acces_matrice_masse('Front', 'Femur') * acces_matrice_acceleration('fr_femur_z') + acces_matrice_masse('Front', 'Tibia') * acces_matrice_acceleration('fr_tibia_z') + acces_matrice_masse('Front', 'Tarsus') * acces_matrice_acceleration('fr_tarse_metatarse_z') 
+ acces_matrice_masse('Middle', 'Coxa') * acces_matrice_acceleration('ml_coxa_z') + acces_matrice_masse('Middle', 'Trochanter') * acces_matrice_acceleration('ml_trochanter_z') + acces_matrice_masse('Middle', 'Femur') * acces_matrice_acceleration('ml_femur_z') + acces_matrice_masse('Middle', 'Tibia') * acces_matrice_acceleration('ml_tibia_z') + acces_matrice_masse('Middle', 'Tarsus') * acces_matrice_acceleration('ml_tarse_metatarse_z') + acces_matrice_masse('Middle', 'Coxa') * acces_matrice_acceleration('mr_coxa_z') + acces_matrice_masse('Middle', 'Trochanter') * acces_matrice_acceleration('mr_trochanter_z') + acces_matrice_masse('Middle', 'Femur') * acces_matrice_acceleration('mr_femur_z') + acces_matrice_masse('Middle', 'Tibia') * acces_matrice_acceleration('mr_tibia_z') + acces_matrice_masse('Middle', 'Tarsus') * acces_matrice_acceleration('mr_tarse_metatarse_z')
+ acces_matrice_masse('Hind', 'Coxa') * acces_matrice_acceleration('rl_coxa_z') + acces_matrice_masse('Hind', 'Trochanter') * acces_matrice_acceleration('rl_trochanter_z') + acces_matrice_masse('Hind', 'Femur') * acces_matrice_acceleration('rl_femur_z') + acces_matrice_masse('Hind', 'Tibia') * acces_matrice_acceleration('rl_tibia_z') + acces_matrice_masse('Hind', 'Tarsus') * acces_matrice_acceleration('rl_tarse_metatarse_z') + acces_matrice_masse('Hind', 'Coxa') * acces_matrice_acceleration('rr_coxa_z') + acces_matrice_masse('Hind', 'Trochanter') * acces_matrice_acceleration('rr_trochanter_z') + acces_matrice_masse('Hind', 'Femur') * acces_matrice_acceleration('rr_femur_z') + acces_matrice_masse('Hind', 'Tibia') * acces_matrice_acceleration('rr_tibia_z') + acces_matrice_masse('Hind', 'Tarsus') * acces_matrice_acceleration('rr_tarse_metatarse_z')

force_z = force_z * 1E-3 - (9 * 1E-6 * (-9.81))      # On soustrait le poids à la force verticale P = m * g
force_z = force_z * 1E6

### On crée le tableau des forces ###

tableau_forces = {            # Création d'un dictionnaire avec les colonnes qui nous intéresse
    'Time': colonne_temps,
    'Force_X': force_x,
    'Force_Y': force_y,
    'Force_Z': force_z
}

tableau_forces = pd.DataFrame(tableau_forces)     # Permet de passer de dictionnaire à Dataframe

tableau_forces.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/5_Forces_de_reaction (µN).xlsx') # On sauvegarde les nouvelles données dans un tableur       

### On crée les graphiques ###

plt.figure(figsize = (20, 14)) 
plt.plot(colonne_temps,force_x, label = "Force dans l'axe X")
plt.plot(colonne_temps,force_y, label = "Force dans l'axe Y")
plt.plot(colonne_temps,force_z, label = "Force dans l'axe Z")

plt.title("Force de réaction du sol chez Messor Barbarus dans l'espace et en fonction du temps")   # titre
plt.xlabel('Temps (s)')   # axe x
plt.ylabel("Force (µN)")    # axe y
plt.legend()     # légende
plt.savefig('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/4_Graphiques/4_Graphiques_forces_de_réaction/Force de réaction du sol en fonction du temps.png') # sauvegarde du graphe
plt.show() 

print("Opération terminée")


### On va normaliser les valeurs de forces par rapport au poids ###

for column_index in range(1, 4): 
    column = tableau_forces.iloc[:, column_index]
    force_norm = column * 1E-6 / (9 * 1E-6 * (9.81))
    tableau_forces.iloc[:, column_index] = force_norm

tableau_forces.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/5_Forces_de_reaction_normalisées.xlsx') # On sauvegarde les forces normalisées dans un tableur       
