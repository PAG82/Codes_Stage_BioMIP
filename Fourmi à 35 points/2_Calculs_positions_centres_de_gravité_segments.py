
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:17:16 2023

@author: pagro
"""

import pandas as pd

tableau_donnees_filtrees = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_35_points/3_Tableaux_excel/2_données_filtrées.xlsx', header = [0,1]) # Chemin d'accès au fichier .xlsx avec choix des lignes correspondant à nos headers
#print(list(tableau_donnees_filtrees.columns))     ## Utile pour analyse rapide


### On réarrange nos colonnes pour pouvoir faire nos calculs de position des centres de gravité des segments ###


new_column_order = [('Frame#', 'Unnamed: 0_level_1'), ('Time', 'Unnamed: 1_level_1'), ('head', 'X2'), ('head', 'Y2'), ('head', 'Z2'), ('neck', 'X3'), ('neck', 'Y3'), ('neck', 'Z3'), ('thpe', 'X34'), ('thpe', 'Y34'), ('thpe', 'Z34'), ('peta', 'X35'), ('peta', 'Y35'), ('peta', 'Z35'), ('abd', 'X36'), ('abd', 'Y36'), ('abd', 'Z36'), ('flth', 'X4'), ('flth', 'Y4'), ('flth', 'Z4'), ('flft', 'X6'), ('flft', 'Y6'), ('flft', 'Z6'), ('fltt', 'X8'), ('fltt', 'Y8'), ('fltt', 'Z8'), ('fltm', 'X10'), ('fltm', 'Y10'), ('fltm', 'Z10'), ('flmt', 'X12'), ('flmt', 'Y12'), ('flmt', 'Z12'), ('frth', 'X5'), ('frth', 'Y5'), ('frth', 'Z5'),  ('frft', 'X7'), ('frft', 'Y7'), ('frft', 'Z7'), ('frtt', 'X9'), ('frtt', 'Y9'), ('frtt', 'Z9'), ('frtm', 'X11'), ('frtm', 'Y11'), ('frtm', 'Z11'),('frmt', 'X13'), ('frmt', 'Y13'), ('frmt', 'Z13'), ('mlth', 'X14'), ('mlth', 'Y14'), ('mlth', 'Z14'), ('mlft', 'X16'), ('mlft', 'Y16'), ('mlft', 'Z16'), ('mltt', 'X18'), ('mltt', 'Y18'), ('mltt', 'Z18'), ('mltm', 'X20'), ('mltm', 'Y20'), ('mltm', 'Z20'), ('mlmt', 'X22'), ('mlmt', 'Y22'), ('mlmt', 'Z22'), ('mrth', 'X15'), ('mrth', 'Y15'), ('mrth', 'Z15'), ('mrft', 'X17'), ('mrft', 'Y17'), ('mrft', 'Z17'), ('mrtt', 'X19'), ('mrtt', 'Y19'), ('mrtt', 'Z19'), ('mrtm', 'X21'), ('mrtm', 'Y21'), ('mrtm', 'Z21'), ('mrmt', 'X23'), ('mrmt', 'Y23'), ('mrmt', 'Z23'), ('rlth', 'X24'), ('rlth', 'Y24'), ('rlth', 'Z24'), ('rlft', 'X26'), ('rlft', 'Y26'), ('rlft', 'Z26'), ('rltt', 'X28'), ('rltt', 'Y28'), ('rltt', 'Z28'), ('rltm', 'X30'), ('rltm', 'Y30'), ('rltm', 'Z30'), ('rlmt', 'X32'), ('rlmt', 'Y32'), ('rlmt', 'Z32'), ('rrth', 'X25'), ('rrth', 'Y25'), ('rrth', 'Z25'),  ('rrft', 'X27'), ('rrft', 'Y27'), ('rrft', 'Z27'), ('rrtt', 'X29'), ('rrtt', 'Y29'), ('rrtt', 'Z29'), ('rrtm', 'X31'), ('rrtm', 'Y31'), ('rrtm', 'Z31'), ('rrmt', 'X33'), ('rrmt', 'Y33'), ('rrmt', 'Z33') ] 
tableau_donnees_filtrees = tableau_donnees_filtrees.reindex(columns=new_column_order) # df.reindex permet de reformer notre tableau suivant l'organisation des titres des colonnes indiqués juste avant
#print(list(tableau_donnees_filtrees.columns))    ## Utile pour analyse rapide
tableau_donnees_filtrees.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_35_points/3_Tableaux_excel/3_données_filtrées_rangées_pour_calcul.xlsx')     # On enregistre le tableau avec les données filtrées rangées correctement pour permettre la boucle suivante (pas besoin de sauvegarder le doc en excel mais je préfère pour pouvoir regarder à l'intérieur du tableau)


### On crée notre tableau avec les positions des centres de gravités des segments au cours du temps ###

tableau_Cg_segments = tableau_donnees_filtrees.iloc[:, :2]     # Permet d'avoir les colonnes "Frame" et "Temps" dans un premier temps


#############################################

groupe_segment = 0     # Voir plus bas la description de cette variable
index = 2     # Va permettre d'insérer une par une les nouvelles colonnes calculées dans le tableau après la colonne "Frame" et "Temps"

xa = 2     # "a" va nous permettre d'incrémenter pour avoir accès aux colonnes que l'on souhaite avoir comme point proximal pour l'axe X. On commence avec 2 car c'est l'index de la colonne ('head','X2')
xb = 5     # "b" va nous permettre d'incrémenter pour avoir accès aux colonnes que l'on souhaite avoir comme point distal pour l'axe X. On commence axxvec 5 car c'est l'index de la colonne ('neck','X2')

ya, yb = 3, 6

za, zb = 4, 7

for columns in tableau_donnees_filtrees:     # Permet de lire tout le tableau
    if xa <= (len(tableau_donnees_filtrees.columns) - 2):     # Permet d'éviter l'erreur disant que xa et les autres valeurs permettant d'accéder aux colonnes aient des valeurs supérieurs aux nombres de colonnes de tableau_donnees_filtrees (Autrement dit, on irait chercher dans des colonnes vides à la fin de la boucle et ça empecherait d'automatiser le script)
        if groupe_segment < 4:     # Ce que j'appelle groupe_segment, ce sont les segments qui composent 1 patte ou le "corps" de la fourmi. Il y a 4 segments pour un groupe à chaque fois ici. Ca permet de ne pas associer des points qui ne devraient pas l'être (ex : "abd" et "flth")
        
            ### On va faire le calcul pour l'axe X ###
            new_column = tableau_donnees_filtrees.iloc[:,xa] + 0.5 *(tableau_donnees_filtrees.iloc[:,xb] - tableau_donnees_filtrees.iloc[:,xa])     # Calcul permettant d'obtenir la position du Cg d'un segment dans l'un des 3 axes de l'espace
            first_column_name = tableau_donnees_filtrees.columns[xa]     # Permet d'accéder au nom de la colonne pour le point proximal
            second_column_name = tableau_donnees_filtrees.columns[xb]     # Permet d'accéder au nom de la colonne pour le point distal
        
            name_new_column = pd.MultiIndex.from_tuples([(first_column_name, second_column_name)])    # Associe le titre des colonnes des 2 points utilisés pour la formation de la nouvelle colonne
            new_column_df = pd.DataFrame(new_column, columns=name_new_column)     # Création de la nouvelle colonne au format DataFrame avec comme nom "name_new_column"
            tableau_Cg_segments = pd.concat([tableau_Cg_segments, new_column_df], axis=1)     # Concaténation de la nouvelle colonne créée et "tableau_Cg_segments (je n'ai pas réussi à faire autrement)
        
        
            ### On fait la même chose pour Y ###
            new_column = tableau_donnees_filtrees.iloc[:,ya] + 0.5 *(tableau_donnees_filtrees.iloc[:,yb] - tableau_donnees_filtrees.iloc[:,ya])
            first_column_name = tableau_donnees_filtrees.columns[ya]
            second_column_name = tableau_donnees_filtrees.columns[yb]
        
            name_new_column = pd.MultiIndex.from_tuples([(first_column_name, second_column_name)])
            new_column_df = pd.DataFrame(new_column, columns=name_new_column)
            tableau_Cg_segments = pd.concat([tableau_Cg_segments, new_column_df], axis=1) 
        
        
            ### On fait la même chose pour Z ###
            new_column = tableau_donnees_filtrees.iloc[:,za] + 0.5 *(tableau_donnees_filtrees.iloc[:,zb] - tableau_donnees_filtrees.iloc[:,za])
            first_column_name = tableau_donnees_filtrees.columns[za]
            second_column_name = tableau_donnees_filtrees.columns[zb]
        
            name_new_column = pd.MultiIndex.from_tuples([(first_column_name, second_column_name)])
            new_column_df = pd.DataFrame(new_column, columns=name_new_column)
            tableau_Cg_segments = pd.concat([tableau_Cg_segments, new_column_df], axis=1) 
        
        
            index += 1
            xa, xb, ya, yb, za, zb = xa + 3, xb + 3, ya + 3, yb + 3, za + 3, zb + 3
            groupe_segment += 1
        
        
        else :
            groupe_segment = 0     # On remet à 0 pour le prochain "groupe de segments"   
            xa, xb, ya, yb, za, zb = xa + 3, xb + 3, ya + 3, yb + 3, za + 3, zb + 3     # Empêche les associations entre 2 points que l'on ne souhaite pas (ex: 'abd' et 'flth')
        
print(tableau_Cg_segments)     ## Utile pour analyse rapide
tableau_Cg_segments.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_35_points/3_Tableaux_excel/4_Positions_Cg_segments.xlsx') # Save the column to an Excel file
