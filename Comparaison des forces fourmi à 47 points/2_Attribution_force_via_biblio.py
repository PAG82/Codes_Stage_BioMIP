# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 20:40:01 2023

@author: pagro
"""

globals().clear()

import pandas as pd
from scipy import signal
import numpy as np
from itertools import chain
import matplotlib.pyplot as plt

#tableau_biblio = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/1_Data_Bibliographie/Data_Reinhardt&Blickhan-JExpBiol-2014b/optimisation_tableau_Reinhardt_2014b.xlsx')     # Données non filtrées me permettant de rapidement comparer


tableau_biblio = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/3_Comparaison_forces_de_réaction_47_points/3_Tableaux_excel/1_Données_filtrées.xlsx')
tableau_biblio = tableau_biblio.iloc[:, 1:]

data_tdc = [   # "tdc" signifie "temps de contact"
    ('Patte antérieure gauche', [0, 0.43, 1.4, 2.6, 3.65], [0.17, 1.06, 2.19, 3.29, 3.69]),     # On a ici dans l'ordre : le nom, les temps pour lesquelles la fourmi pose sa patte sur le sol et les temps pour lesquelles la fourmi lève sa patte du sol
    ('Patte antérieure droite', [0, 0.87, 2.01, 3.09], [0.53, 1.71, 2.8, 3.69]),
    ('Patte médiane gauche', [0, 0.89, 2, 3.05], [0.66, 1.65, 2.75, 3.69]),
    ('Patte médiane droite', [0, 0.37, 1.28, 2.5, 3.54], [0.15, 1.06, 2.3, 3.3, 3.69]),
    ('Patte postérieure gauche', [0, 0.51, 1.49, 2.66], [0.34, 1.26, 2.46, 3.59]),
    ('Patte postérieure droite', [0, 0.93, 2.17, 3.16], [0.78, 1.87, 2.96, 3.69]),         
]

#########################################

### On va créer le tableau "tab_diff_temps" qui contiendra tous les temps de contact de la patte au sol ###

tab_diff_temps = pd.DataFrame()

for row in data_tdc:      ## Va analyser les tuples une par une du tableau "data_tdc"
    nom = row[0]
    start_times = row[1]     # Va prendre la première liste dans le tuple choisi pour les temps de début de contact au sol
    end_times = row[2]     # Va prendre la seconde liste dans le tuple choisi pour les temps de fin de contact au sol
    
    temps_tdc = [end - start for start, end in zip(start_times, end_times)]     # "zip()" permet la soustraction entre 2 listes
    
    # Vu qu'on a pas le même nombre de phase de temps de contact entre les pattes, on est obligé de rajouter des cellules sans valeurs pour pouvoir regrouper toutes les valeurs dans un même tableau
    if len(temps_tdc) < len(tab_diff_temps):
        temps_tdc.extend([float('nan')] * (len(tab_diff_temps) - len(temps_tdc)))
    
    tab_diff_temps[nom] = temps_tdc

########################################

### On va mainteant obtenir le temps pour le signal qu'on va "resampler" par la suite. On aura une valeur de temps toutes les 0.01 sec entre "start_time" et "end_time" dans une matrice ###

temps_resampled_list = []
row = ()     # Permet de nettoyer le tuple déjà utilisé plus haut
for row in data_tdc:      # Va analyser les tuples une par une du tableau "data_pas"
    nom = row[0]
    start_times = row[1] 
    end_times = row[2]
    
    for i in range(len(start_times)):     ## Va associer les valeurs une par une dans nos listes (on aura alors le début de contact et la fin de contact de la patte au sol pour chaque phase de tdc)
        start_time = start_times[i]
        end_time = end_times[i]
        interval = 0.01

        temps_resampled = []
        current_time = start_time
        
        while current_time <= end_time - interval/2:    # Hyper important de rajouter "- interval/2" car sinon on va avoir des problèmes de calcul et d'arrondi de l'ordi et avoir trop de valeurs de temps pour nos futurs points.
            temps_resampled.append(round(current_time, 2))     # Nécessaire de mettre "round" car l'ordi fait des arrondis qu'on ne veut pas même si on met bien comme intervalle "0.01". Si on ne fait pas ça, on se retrouve avec des valeurs comme 3.469999999999...
            current_time += interval
        
        temps_resampled_list.append(temps_resampled)
        print(temps_resampled)
                

####################################

### On va mainteant obtenir les valeurs après resample. On va ensuite les associer respectivement aux valeurs de temps "resamplées" obtenues précédemment ###

signal_resampled_list = []   # Liste qui va contenir les listes de valeurs de forces resamplées
tab_final = pd.DataFrame()


def signal_resampled(index_col_tdt, index_col_biblio):     # On resample le signal ("tdt" signifie "tab_diff_temps")
    for column in tab_diff_temps.columns[index_col_tdt: index_col_tdt + 2]:     # Permet d'accéder aux colonnes des tdc des pattes dans "tab_diff temps". On fait "+2" et pas "+1" car on veut prendre 2 colonnes. Si on fait "+1", seul "index_col_tdc" sera pris en compte
        column_length = len(tab_diff_temps[column].dropna())     # On se débarasse de "Nan" pour le calcul de la longueur de note colonne
    
        try:        # "try/except" empêche d'avoir un message d'erreur d'"out of bounds" et de continuer la lecture du code
                index_row = 0      # Indice pour les lignes de "tab_diff_temps"
            
                for i in range(column_length):     # Permet d'accéder aux lignes de "tab_diff temps"
                    donnees_signal = tableau_biblio.iloc[:, index_col_biblio]     # Permet d'accéder aux données de la biblio des différentes forces pour les différentes pattes
                    fs_new = 100     # Fréquence d'acquisition de nos données
                    fs_orig = 51 / tab_diff_temps.iloc[index_row, index_col_tdt]       # Fréquence d'origine que j'ai utilisé pour obtenir 51 points dans la bibliographie. Va changer entre les différents pas car elle dépend de leur durée
                    
                    if np.isnan(fs_orig):  # Vérifie si fs_orig est un NaN dû à l'absence potentielle de valeur dans le tableau "tab_diff_temps". On va alors passer cette valeur et continuer le code si c'est le cas
                        print("Invalid value. Skipping resampling for this iteration.")
                        continue
                    
                    signal_resampled = signal.resample(donnees_signal, round(len(donnees_signal) * (fs_new / fs_orig)))      # On resample le signal
                    signal_resampled_list.append(signal_resampled)     # On ajoute le nouveau signal dans la liste "signal_resampled_list
                    
                    index_row += 1
                index_col_tdt += 1
                
        except IndexError:
            print("Index out of bounds. Skipping resampling for this iteration.")

def signal_resampled_minus(index_col_tdt, index_col_biblio):     # Cette fonction est similaire à celle juste au-dessus mais je vais pouvoir changer le signe pour les forces d'une des 2 pattes. Je l'ai exlusivement fait pour les forces latérales des pattes médianes
        column_length = len(tab_diff_temps.iloc[:,index_col_tdt].dropna())     # On se débarasse de "Nan" pour le calcul de la longueur de note colonne
    
        try:        # "try/except" empêche d'avoir un message d'erreur d'"out of bounds" et de continuer la lecture du code
                index_row = 0      # Indice pour les lignes de "tab_diff_temps"
            
                for i in range(column_length):     # Permet d'accéder aux lignes de "tab_diff temps"
                    donnees_signal = tableau_biblio.iloc[:, index_col_biblio]      
                    fs_new = 100     # Fréquence d'acquisition de nos données
                    fs_orig = 51 / tab_diff_temps.iloc[index_row, index_col_tdt]       # Fréquence d'origine que j'ai utilisé pour obtenir 51 points dans la bibliographie. Va changer entre les différents pas car elle dépend de leur durée
                    
                    if np.isnan(fs_orig):  # Vérifie si fs_orig est un NaN dû à l'absence potentielle de valeur dans le tableau "tab_diff_temps". On va alors passer cette valeur et continuer le code si c'est le cas
                        print("Invalid value. Skipping resampling for this iteration.")
                        continue
                    
                    signal_resampled = signal.resample(donnees_signal, round(len(donnees_signal) * (fs_new / fs_orig)))      # On resample le signal
                    signal_resampled_list.append(signal_resampled)     # On ajoute le nouveau signal dans la liste "signal_resampled_list
                    
                    index_row += 1
                
        except IndexError:
            print("Index out of bounds. Skipping resampling for this iteration.")

        
        column_length = len(tab_diff_temps.iloc[:,index_col_tdt+1].dropna())   
        try:   
                index_row = 0
            
                for i in range(column_length):
                    donnees_signal = - tableau_biblio.iloc[:, index_col_biblio]    # On va inverser de signe les forces latérales pour les pattes du côté droit
                    fs_new = 100
                    fs_orig = 51 / tab_diff_temps.iloc[index_row, index_col_tdt + 1]
                    
                    if np.isnan(fs_orig):
                        print("Invalid value. Skipping resampling for this iteration.")
                        continue
                    
                    signal_resampled = signal.resample(donnees_signal, round(len(donnees_signal) * (fs_new / fs_orig)))
                    signal_resampled_list.append(signal_resampled)     
                    
                    index_row += 1
                
        except IndexError:
            print("Index out of bounds. Skipping resampling for this iteration.")


def create_tab_final(nom_col_force):     # Permet de créer un tableau contenant uniquement 2 colonnes : le temps "resamplé" et le signal "resamplé"
    global tab_final
    tab_final = pd.DataFrame({'Temps (s)': temps_resampled_list, nom_col_force: signal_resampled_list})     # Crée le tableau final à 2 colonnes avec le temps et les forces

    tab_final = tab_final.sort_values(by = 'Temps (s)', ascending=True)     # Trie les données en fonctions du temps
    tab_final = tab_final.groupby('Temps (s)')[nom_col_force].sum().reset_index()     # Regroupe les valeurs de temps qui sont en doubles et fait la somme des forces qui correspondent 

    ### On doit enlever les données inf à 0.5 sec et sup à 3.2 sec ###
    #On doit faire ça car comme on le voit dans le graphe du "stepping pattern" tracé avec le code pour Messor Barbarus on ne peut pas dire que les temps de contact du début et de la fin du temps d'acquisition vont de 0 à 100%

    tab_final = tab_final[(tab_final['Temps (s)'] >= 0.5) & (tab_final['Temps (s)'] <= 3.2)] # On fait un booléen pour ne garder les valeurs entre 0.5 et 3.2 pour le temps avec leur valeur de force respective
    
    return tab_final     # Nécessaire de retourner la variable "tab_final" car sinon c'est une variable locale qu'on ne pourra pas utiliser pour la fonction "create_graph"

def create_graph(tab_final, nom_force):     # Création des graphes
    temps = tab_final['Temps (s)']
    force = tab_final[f'Force {nom_force}']

    plt.figure(figsize = (20, 14)) 
    plt.plot(temps,force, label = f"Force dans l'axe {nom_force}")

    plt.title("Force de réaction du sol dans la littérature scientifique")     # titre
    plt.xlabel('Temps (s)')     # axe x
    plt.ylabel("Force de réaction du sol (normalisée au poids du corps)")    # axe y
    plt.legend()     # légende
    plt.savefig(f'C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/3_Comparaison_forces_de_réaction_47_points/4_Graphiques/1_Graphes_biblio/Force {nom_force}.png')
    plt.show()  


#### Forces latérales ###   # Je fais le resample des forces dans cette ordre là pour facilement les comparer aux forces de notre fourmi Barbarus dans le script suivant

signal_resampled(0,2)     # Va prendre les tdc des pas des pattes antérieures (index 0 et 1) et leurs attribuer les valeurs des forces latérales pour les pattes antérieures trouvées dans la bibliographie (index 2)
signal_resampled_minus(2,5)     # J'utilise cette fonction plutôt que l'autre ici car les forces latérales des pattes médianes s'opposent entre elles (sinon la fourmi tournerai d'un côté et n'avancerai pas droit). C'est le but de la fonction "signal_resampled_minus". Contrairement à "signal_resampled_minus", la fonction va rajouter un signe "-" aux valeurs de la patte médiane droite (et pas à la patte gauche pour que cela corresponde à notre système où l'axe X se dirige vers le côté droit de la fourmi). 
signal_resampled_minus(4,8)     # Va prendre les tdc des pas des pattes postérieures (index 4 et 5) et leurs attribuer les valeurs des forces latérales pour les pattes postérieures trouvées dans la bibliographie (index 8)

# On va transformer nos 2 listes de listes en 2 listes de valeurs qui vont être associées par la suite. Les valeurs de temps avec les valeurs de forces correspondantes.
temps_resampled_list = list(chain(*temps_resampled_list))
signal_resampled_list = list(chain(*signal_resampled_list))


create_graph(create_tab_final('Force latérale'), 'latérale')

# On va former un tableau excel avec le temps et toutes les forces pour pouvoir comparer avec nos données dans un autre script
tab_excel = pd.DataFrame({'Temps (s)': tab_final.iloc[:,0]})
tab_excel['Forces latérales'] = tab_final.iloc[:,1]



### Forces ant-post ###
signal_resampled_list = []    # On remet à 0 la liste qui va contenir les signaux resamplés (pour éviter de garder les forces utilisées juste avant)


signal_resampled(0,1)
signal_resampled(2,4)
signal_resampled(4,7)

signal_resampled_list = list(chain(*signal_resampled_list))     # Pas besoin de faire la même action avec le temps car on l'a déjà fait plus haut et c'est valable pour toutes les valeurs de forces

create_graph(create_tab_final('Force ant-post'), 'ant-post')

tab_excel['Forces ant-post'] = tab_final.iloc[:,1]





#### Forces verticales ###
signal_resampled_list = []    # On remet à 0 la liste qui va contenir les signaux resamplés (pour éviter de garder les forces utilisées juste avant)

signal_resampled(0,3)
signal_resampled(2,6)
signal_resampled(4,9)

signal_resampled_list = list(chain(*signal_resampled_list))     # Pas besoin de faire la même action avec le temps car on l'a déjà fait plus haut et c'est valable pour toutes les valeurs de forces

create_graph(create_tab_final('Force verticale'), 'verticale')

tab_excel['Forces verticales'] = tab_final.iloc[:,1]

tab_excel.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/3_Comparaison_forces_de_réaction_47_points/3_Tableaux_excel/2_Tableau_forces_comparaison_biblio.xlsx')