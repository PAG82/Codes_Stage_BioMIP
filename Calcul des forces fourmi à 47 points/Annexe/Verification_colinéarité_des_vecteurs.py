# -*- coding: utf-8 -*-
"""
Created on Sat Jun  3 12:39:22 2023

@author: pagro
"""

##################################################################################################
# 2 vecteurs sont colinéaires si il existe un réel k tel que u = kv où u et v sont nos 2 vecteurs#
##################################################################################################

globals().clear()      # Supprime toutes les variables pour me permettre de relancer le code lorsque je veux faire de nouveaux essais

import pandas as pd
import sys

tableau_donnees_filtrees = pd.read_excel("C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/2_données_filtrées.xlsx", header=[0])

matrice = []

# Chaque colonne va devenir une liste dans notre matrice
for index, column in enumerate(tableau_donnees_filtrees.columns):    # Les 2 premières colonnes vont formées 2 listes dans la matrice mais vu qu'après on prend xa = 2 comme point de départ, ça n'a pas d'importance
        valeurs_colonnes = tableau_donnees_filtrees[column].tolist()
        matrice.append(valeurs_colonnes)

#############################################

groupe_segment = 0
num_affichage =1     # Permet de sauvegarder les graphes

xa = 2     # "a" va nous permettre d'incrémenter pour avoir accès aux colonnes que l'on souhaite avoir comme point proximal pour l'axe X. On commence avec 2 car c'est l'index de la colonne ('head','X2')
xb = 5     # "b" va nous permettre d'incrémenter pour avoir accès aux colonnes que l'on souhaite avoir comme point distal pour l'axe X. On commence axxvec 5 car c'est l'index de la colonne ('neck','X2')
ya, yb = 3, 6
za, zb = 4, 7

x_vecteur, y_vecteur, z_vecteur = 0,1,2    # Il est nécessaire de créer ces nouvelles variables pour accéder au bonnes colonnes pour les coordonnées des vecteurs. On ne peut pas prendre les variables du dessus car il y a aura un problème d'indice lorsque l'on passera au groupement suivant (on aura xa += 3, etc pour sauter une "association" non voulue mais ça impacterait également la prise de valeurs dans les matrices des coordonnées des vecteurs. On serait alors "out of bounds") 


matrice_Cg, coordonnees_vecteur_segment, coordonnees_vecteur_Cg = [], [], []      # On prépare les matrices que l'on va utiliser après 


for columns in tableau_donnees_filtrees:     # Permet de lire tout le tableau
    try:    # Permet d'éviter l'erreur disant que xa et les autres valeurs permettant d'accéder aux colonnes aient des valeurs supérieurs aux nombres de colonnes de tableau_donnees_filtrees (Autrement dit, on irait chercher dans des colonnes vides à la fin de la boucle et ça empecherait d'automatiser le script)
   
    ### On va d'abord s'occuper des segments composants le "tronc" ###
       
        while groupe_segment < 4:     # Ce que j'appelle groupe_segment, ce sont les segments qui composent 1 patte ou le "corps" de la fourmi. Il y a 4 segments pour le "tronc" et 6 pour les pattes. Ca permet de ne pas associer des points qui ne devraient pas l'être (ex : "abd" et "flth")
 
    ### On établit la position du centre de gravité ###
    
            Cg_x_position, Cg_y_position, Cg_z_position = tableau_donnees_filtrees.iloc[:,xa] + 0.5 *(tableau_donnees_filtrees.iloc[:,xb] - tableau_donnees_filtrees.iloc[:,xa]), tableau_donnees_filtrees.iloc[:,ya] + 0.5 *(tableau_donnees_filtrees.iloc[:,yb] - tableau_donnees_filtrees.iloc[:,ya]), tableau_donnees_filtrees.iloc[:,za] + 0.5 *(tableau_donnees_filtrees.iloc[:,zb] - tableau_donnees_filtrees.iloc[:,za])            
            matrice_Cg.extend([Cg_x_position, Cg_y_position, Cg_z_position])     # Permet d'intégrer les nouvelles valeurs calculées dans une nouvelle matrice
            
    ### On calcule les coordonnées de nos 2 vecteurs ###  ex calcul coordonnées vecteur: AB = (xB-xA, yB-yA, zB-zA) ###

       # 1. On calcule les coordonnées du vecteur passant par le point proximal et distal
            vecteur_segment_x = [b - a for a, b in zip(matrice[xa], matrice[xb])]     # Soustrait les valeurs de la colonne ayant pour indice "xb" par les ayant pour indices "xa . La fonction zip() est nécessaire car on veut soustraire ici des des valeurs entre 2 listes
            vecteur_segment_y = [b - a for a, b in zip(matrice[ya], matrice[yb])]
            vecteur_segment_z = [b - a for a, b in zip(matrice[za], matrice[zb])]
            
       # 2. On calcule les coordonnées du vecteur passant par le point proximal et le centre de gravité du segment        
            vecteur_Cg_x = [b - a for a, b in zip(matrice[xa], matrice_Cg[x_vecteur])]     
            vecteur_Cg_y = [b - a for a, b in zip(matrice[ya], matrice_Cg[y_vecteur])]
            vecteur_Cg_z = [b - a for a, b in zip(matrice[za], matrice_Cg[z_vecteur])]
            
            
       # 3. On rentre les coordonnées de nos vecteurs dans 2 matrices distinctes pour les prochains calculs
            coordonnees_vecteur_segment.extend([vecteur_segment_x, vecteur_segment_y, vecteur_segment_z])
            coordonnees_vecteur_Cg.extend([vecteur_Cg_x, vecteur_Cg_y, vecteur_Cg_z])

    ### On regarde si les 2 vecteurs sont colinéaires ###
            
            rapport_x = [b / a for a, b in zip(coordonnees_vecteur_segment[x_vecteur], coordonnees_vecteur_Cg[x_vecteur])]     # Même raisonnement que plus haut pour le -2
            rapport_y = [b / a for a, b in zip(coordonnees_vecteur_segment[y_vecteur], coordonnees_vecteur_Cg[y_vecteur])]
            rapport_z = [b / a for a, b in zip(coordonnees_vecteur_segment[z_vecteur], coordonnees_vecteur_Cg[z_vecteur])]

            rapport_x = [round(ratio, 10) for ratio in rapport_x]     # On arrondit les ratios parce que sinon il y aura des micros différences liées à l'arrondissement automatique de certaines valeurs aux mauvais endroits
            rapport_y = [round(ratio, 10) for ratio in rapport_y]     # On arrondit (pour toutes les valeurs) à 10 chiffres après la virgule
            rapport_z = [round(ratio, 10) for ratio in rapport_z]

            for row in range(len(rapport_x)):
                if rapport_x[row] == rapport_y[row] == rapport_z[row]:
                    print("True")
                else:
                    print("Les vecteurs ne sont pas colinéaires")
                    sys.exit()     # Le script s'arrêtera dès qu'il y a 2 vecteurs non colinéaires pour ce groupe de segments

            xa, xb, ya, yb, za, zb = xa + 3, xb + 3, ya + 3, yb + 3, za + 3, zb + 3
            x_vecteur, y_vecteur, z_vecteur = x_vecteur + 3, y_vecteur + 3, z_vecteur + 3
            num_affichage += 1 
            groupe_segment += 1
        
            
        groupe_segment = 0     # On remet à 0 pour le prochain "groupe de segments"   
        xa, xb, ya, yb, za, zb = xa + 3, xb + 3, ya + 3, yb + 3, za + 3, zb + 3     # Empêche les associations entre 2 points que l'on ne souhaite pas (ex: 'abd' et 'flth')
        # Pas besoin de modifier "vecteur_x", "vecteur_y" et "vecteur_z" car les matrices des vecteurs sont créées au fur et à mesure (contrairement à la matrice initiale qui va faire des "associations" non voulues (comme exliqué à la ligne du dessus))
    
    ### On va ensuite s'occuper des segments composants les différentes pattes ###
    
        while groupe_segment < 6:
            
            Cg_x_position, Cg_y_position, Cg_z_position = tableau_donnees_filtrees.iloc[:,xa] + 0.5 *(tableau_donnees_filtrees.iloc[:,xb] - tableau_donnees_filtrees.iloc[:,xa]), tableau_donnees_filtrees.iloc[:,ya] + 0.5 *(tableau_donnees_filtrees.iloc[:,yb] - tableau_donnees_filtrees.iloc[:,ya]), tableau_donnees_filtrees.iloc[:,za] + 0.5 *(tableau_donnees_filtrees.iloc[:,zb] - tableau_donnees_filtrees.iloc[:,za])            
            matrice_Cg.extend([Cg_x_position, Cg_y_position, Cg_z_position])  
            
    ### On calcule les coordonnées de nos 2 vecteurs ###  ex calcul coordonnées vecteur: AB = (xB-xA, yB-yA, zB-zA) ###
    
       # 1. On calcule les coordonnées du vecteur passant par le point proximal et distal
            vecteur_segment_x = [b - a for a, b in zip(matrice[xa], matrice[xb])]  
            vecteur_segment_y = [b - a for a, b in zip(matrice[ya], matrice[yb])]
            vecteur_segment_z = [b - a for a, b in zip(matrice[za], matrice[zb])]
            
       # 2. On calcule les coordonnées du vecteur passant par le point proximal et le centre de gravité du segment        
            vecteur_Cg_x = [b - a for a, b in zip(matrice[xa], matrice_Cg[x_vecteur])] 
            vecteur_Cg_y = [b - a for a, b in zip(matrice[ya], matrice_Cg[y_vecteur])]
            vecteur_Cg_z = [b - a for a, b in zip(matrice[za], matrice_Cg[z_vecteur])]
            
            
       # 3. On rentre les coordonnées de nos vecteurs dans 2 matrices distinctes pour les prochains calculs
            coordonnees_vecteur_segment.extend([vecteur_segment_x, vecteur_segment_y, vecteur_segment_z])
            coordonnees_vecteur_Cg.extend([vecteur_Cg_x, vecteur_Cg_y, vecteur_Cg_z])
    
    ### On regarde si les 2 vecteurs sont colinéaires ###
            
            rapport_x = [b / a for a, b in zip(coordonnees_vecteur_segment[x_vecteur], coordonnees_vecteur_Cg[x_vecteur])] 
            rapport_y = [b / a for a, b in zip(coordonnees_vecteur_segment[y_vecteur], coordonnees_vecteur_Cg[y_vecteur])]
            rapport_z = [b / a for a, b in zip(coordonnees_vecteur_segment[z_vecteur], coordonnees_vecteur_Cg[z_vecteur])]
    
            rapport_x = [round(ratio, 10) for ratio in rapport_x]   
            rapport_y = [round(ratio, 10) for ratio in rapport_y]
            rapport_z = [round(ratio, 10) for ratio in rapport_z]
    
            for row in range(len(rapport_x)):
                if rapport_x[row] == rapport_y[row] == rapport_z[row]:
                    print("True")
                else:
                    print("Les vecteurs ne sont pas colinéaires")
                    sys.exit()     
                
            xa, xb, ya, yb, za, zb = xa + 3, xb + 3, ya + 3, yb + 3, za + 3, zb + 3
            x_vecteur, y_vecteur, z_vecteur = x_vecteur + 3, y_vecteur + 3, z_vecteur + 3
            num_affichage += 1 
            groupe_segment += 1
                  
    except IndexError:     # Empêche le blocage du programme lorsque x a une valeur supérieure au nombre de colonnes du tableau à la fin de la boucle
       print(f"Column index {xa} is out of bounds.")     
       break