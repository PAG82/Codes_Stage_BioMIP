# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 07:46:56 2023

@author: pagro
"""

globals().clear()      # Supprime toutes les variables pour me permettre de relancer le code lorsque je veux faire de nouveaux essais

import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

tableau_donnees_filtrees = pd.read_excel("C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/2_données_filtrées.xlsx", header=[0])

#############################################

groupe_segment = 0
num_affichage =1     # Permet de sauvegarder les graphes

xa = 2     # "a" va nous permettre d'incrémenter pour avoir accès aux colonnes que l'on souhaite avoir comme point proximal pour l'axe X. On commence avec 2 car c'est l'index de la colonne ('head','X2')
xb = 5     # "b" va nous permettre d'incrémenter pour avoir accès aux colonnes que l'on souhaite avoir comme point distal pour l'axe X. On commence axxvec 5 car c'est l'index de la colonne ('neck','X2')

ya, yb = 3, 6

za, zb = 4, 7

for columns in tableau_donnees_filtrees:     # Permet de lire tout le tableau
    try:    # Permet d'éviter l'erreur disant que xa et les autres valeurs permettant d'accéder aux colonnes aient des valeurs supérieurs aux nombres de colonnes de tableau_donnees_filtrees (Autrement dit, on irait chercher dans des colonnes vides à la fin de la boucle et ça empecherait d'automatiser le script)
   
    ### On va d'abord s'occuper des segments composants le "tronc" ###
       
        while groupe_segment < 4:     # Ce que j'appelle groupe_segment, ce sont les segments qui composent 1 patte ou le "corps" de la fourmi. Il y a 4 segments pour le "tronc" et 6 pour les pattes. Ca permet de ne pas associer des points qui ne devraient pas l'être (ex : "abd" et "flth")
 
    ### On va établir les différentes valeurs qu'on va utiliser ###
    
            xa_value, ya_value, za_value = tableau_donnees_filtrees.iloc[:,xa], tableau_donnees_filtrees.iloc[:,ya], tableau_donnees_filtrees.iloc[:,za] # Donne les coordonnées du point proximal
            xb_value, yb_value, zb_value = tableau_donnees_filtrees.iloc[:,xb], tableau_donnees_filtrees.iloc[:,yb], tableau_donnees_filtrees.iloc[:,zb] # Donne les coordonnées du point distal
        
            Cg_x_position, Cg_y_position, Cg_z_position = tableau_donnees_filtrees.iloc[:,xa] + 0.5 *(tableau_donnees_filtrees.iloc[:,xb] - tableau_donnees_filtrees.iloc[:,xa]), tableau_donnees_filtrees.iloc[:,ya] + 0.5 *(tableau_donnees_filtrees.iloc[:,yb] - tableau_donnees_filtrees.iloc[:,ya]), tableau_donnees_filtrees.iloc[:,za] + 0.5 *(tableau_donnees_filtrees.iloc[:,zb] - tableau_donnees_filtrees.iloc[:,za])
        
        
            nom_point_proximal, nom_point_distal = tableau_donnees_filtrees.columns[xa], tableau_donnees_filtrees.columns[xb]
        
    ### On forme le graphe en 3D des positions des différents points du segment et on les sauvegarde ###
    
            fig = plt.figure(figsize = (20, 14)) 
            ax = fig.add_subplot(111, projection='3d')
            
            ax.plot(xa_value, ya_value, za_value, marker='o', markersize=6, markerfacecolor='blue', label = f"Point proximal, {nom_point_proximal}")
            ax.plot(xb_value, yb_value, zb_value, marker='o', markersize=6, markerfacecolor='orange', label = f"Point distal, {nom_point_distal}")
            ax.plot(Cg_x_position, Cg_y_position, Cg_z_position, marker='o', markersize=6, markerfacecolor='red', label = 'Centre de gravité segmentaire')
       

            ax.set_title('Vérification position du Cg segmentaire')
            ax.set_xlabel('position en X')
            ax.set_ylabel('position en Y')
            ax.set_zlabel('position en Z')
            ax.legend()
            
        
            filename = f"({num_affichage}). 3D, {tableau_donnees_filtrees.columns[xa]}, {tableau_donnees_filtrees.columns[xb]}"
            plt.savefig(f'C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/4_Graphiques/2bis_Verification_3D_position_Cg_segmentaire/{filename}.png') # sauvegarde du graphe
            plt.show()
        
            xa, xb, ya, yb, za, zb = xa + 3, xb + 3, ya + 3, yb + 3, za + 3, zb + 3
            num_affichage += 1 
            groupe_segment += 1
        
        groupe_segment = 0     # On remet à 0 pour le prochain "groupe de segments"   
        xa, xb, ya, yb, za, zb = xa + 3, xb + 3, ya + 3, yb + 3, za + 3, zb + 3     # Empêche les associations entre 2 points que l'on ne souhaite pas (ex: 'abd' et 'flth')
    
    
    ### On va ensuite s'occuper des segments composants les différentes pattes ###
    
        while groupe_segment < 6:     # Ce que j'appelle groupe_segment, ce sont les segments qui composent 1 patte ou le "corps" de la fourmi. Il y a 4 segments pour le "tronc" et 6 pour les pattes. Ca permet de ne pas associer des points qui ne devraient pas l'être (ex : "abd" et "flth")
   
    ### On va établir les différentes valeurs qu'on va utiliser ###
    
            xa_value, ya_value, za_value = tableau_donnees_filtrees.iloc[:,xa], tableau_donnees_filtrees.iloc[:,ya], tableau_donnees_filtrees.iloc[:,za] # Donne les coordonnées du point proximal
            xb_value, yb_value, zb_value = tableau_donnees_filtrees.iloc[:,xb], tableau_donnees_filtrees.iloc[:,yb], tableau_donnees_filtrees.iloc[:,zb] # Donne les coordonnées du point distal
        
            Cg_x_position, Cg_y_position, Cg_z_position = tableau_donnees_filtrees.iloc[:,xa] + 0.5 *(tableau_donnees_filtrees.iloc[:,xb] - tableau_donnees_filtrees.iloc[:,xa]), tableau_donnees_filtrees.iloc[:,ya] + 0.5 *(tableau_donnees_filtrees.iloc[:,yb] - tableau_donnees_filtrees.iloc[:,ya]), tableau_donnees_filtrees.iloc[:,za] + 0.5 *(tableau_donnees_filtrees.iloc[:,zb] - tableau_donnees_filtrees.iloc[:,za])
        
        
            nom_point_proximal, nom_point_distal = tableau_donnees_filtrees.columns[xa], tableau_donnees_filtrees.columns[xb]
        
    ### On forme le graphe en 3D des positions des différents points du segment et on les sauvegarde ###
    
            fig = plt.figure(figsize = (20, 14)) 
            ax = fig.add_subplot(111, projection='3d')
            
            ax.plot(xa_value, ya_value, za_value, marker='o', markersize=6, markerfacecolor='blue', label = f"Point proximal, {nom_point_proximal}")
            ax.plot(xb_value, yb_value, zb_value, marker='o', markersize=6, markerfacecolor='orange', label = f"Point distal, {nom_point_distal}")
            ax.plot(Cg_x_position, Cg_y_position, Cg_z_position, marker='o', markersize=6, markerfacecolor='red', label = 'Centre de gravité segmentaire')
       

            ax.set_title('Vérification position du Cg segmentaire')
            ax.set_xlabel('position en X')
            ax.set_ylabel('position en Y')
            ax.set_zlabel('position en Z')
            ax.legend()
            
        
            filename = f"({num_affichage}). 3D, {tableau_donnees_filtrees.columns[xa]}, {tableau_donnees_filtrees.columns[xb]}"
            plt.savefig(f'C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/4_Graphiques/2bis_Verification_3D_position_Cg_segmentaire/{filename}.png') # sauvegarde du graphe
            plt.show()
        
            xa, xb, ya, yb, za, zb = xa + 3, xb + 3, ya + 3, yb + 3, za + 3, zb + 3
            num_affichage += 1 
            groupe_segment += 1
              
    except IndexError:     # Empêche le blocage du programme lorsque x a une valeur supérieure au nombre de colonnes du tableau à la fin de la boucle
       print(f"Column index {xa} is out of bounds.")     
       break