# -*- coding: utf-8 -*-
"""
Created on Thu May 18 23:54:35 2023

@author: pagro
"""
globals().clear()      # Supprime toutes les variables pour me permettre de relancer le code lorsque je veux faire de nouveaux essais

import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

tableau = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/1_Données_intiales_à_traiter/jordan_data.xlsx', header = None ) # Chemin d'accès au fichier .xlsx contenant les data

### On a besoin d'éliminer les colonnes R (qui ne nous intéresse pas) et de garder les colonnes X, Y et Z ###

columns_to_delete = tableau.columns[3::4]     # On sélectionne les colonnes tous les 4 pas en commençant par 3 car la première colonne a pour index 0
tableau = tableau.drop(columns=columns_to_delete)     # On élimine ces colonnes


### On va créer un nouveau tableau rangé correctement avec le temps et les données mesurées pour pouvoir les exploiter après ###

freq_acquisition = float(input("Indiquez la fréquence d'aquisition (en Hz): "))     # Demande à l'utilisateur 

temps = [round(x * (1 / freq_acquisition), 3) for x in range(0, 370)]      # Va créer les valeurs allant de 0 à 3,69 Hz avec un pas dépendant de la fréquence d'acquisition
new_tableau = pd.DataFrame({'Temps (s)': temps})     # Crée un tableau avec une seule colonne appelée "Temps"

# On crée les headers pour les colonnes des données obtenues après mesures
tableau.columns = ['1-head X' , '1-head Y', '1-head Z', '2-neck X', '2-neck Y', '2-neck Z', '3-fl_th_cox X', '3-fl_th_cox Y', '3-fl_th_cox Z', '4-fr_th_cox X', '4-fr_th_cox Y', '4-fr_th_cox Z', '5-fl_cox_tro X', '5-fl_cox_tro Y', '5-fl_cox_tro Z', '6-fr_cox_tro X', '6-fr_cox_tro Y', '6-fr_cox_tro Z', '7-fl_tro_fe X', '7-fl_tro_fe Y', '7-fl_tro_fe Z',  '8-fr_tro_fe X', '8-fr_tro_fe Y', '8-fr_tro_fe Z', '9-fl_fe_ti X', '9-fl_fe_ti Y', '9-fl_fe_ti Z', '10-fr_fe_ti X', '10-fr_fe_ti Y', '10-fr_fe_ti Z', '11-fl_ti_ta X', '11-fl_ti_ta Y', '11-fl_ti_ta Z', '12-fr_ti_ta X', '12-fr_ti_ta Y', '12-fr_ti_ta Z', '13-fl_ta_mt X', '13-fl_ta_mt Y', '13-fl_ta_mt Z', '14-fr_ta_mt X', '14-fr_ta_mt Y', '14-fr_ta_mt Z', '15-fl_mt X', '15-fl_mt Y', '15-fl_mt Z', '16-fr_mt X', '16-fr_mt Y', '16-fr_mt Z', '17-ml_th_cox X', '17-ml_th_cox Y', '17-ml_th_cox Z', '18-mr_th_cox X', '18-mr_th_cox Y', '18-mr_th_cox Z', '19-ml_cox_tro X', '19-ml_cox_tro Y', '19-ml_cox_tro Z', '20-mr_cox_tro X', '20-mr_cox_tro Y', '20-mr_cox_tro Z', '21-ml_tro_fe X', '21-ml_tro_fe Y','21-ml_tro_fe Z', '22-mr_tro_fe X', '22-mr_tro_fe Y','22-mr_tro_fe Z', '23-ml_fe_ti X', '23-ml_fe_ti Y', '23-ml_fe_ti Z', '24-mr_fe_ti X', '24-mr_fe_ti Y', '24-mr_fe_ti Z', '25-ml_ti_ta X', '25-ml_ti_ta Y', '25-ml_ti_ta Z', '26-mr_ti_ta X', '26-mr_ti_ta Y', '26-mr_ti_ta Z', '27-ml_ta_mt X', '27-ml_ta_mt Y', '27-ml_ta_mt Z', '28-mr_ta_mt X', '28-mr_ta_mt Y', '28-mr_ta_mt Z', '29-ml_mt X', '29-ml_mt Y', '29-ml_mt Z', '30-mr_mt X', '30-mr_mt Y', '30-mr_mt Z', '31-rl_th_cox X', '31-rl_th_cox Y', '31-rl_th_cox Z', '32-rr_th_cox X', '32-rr_th_cox Y', '32-rr_th_cox Z', '33-rl_cox_tro X','33-rl_cox_tro Y', '33-rl_cox_tro Z', '34-rr_cox_tro X', '34-rr_cox_tro Y', '34-rr_cox_tro Z', '35-rl_tro_fe X', '35-rl_tro_fe Y', '35-rl_tro_fe Z', '36-rr_tro_fe X', '36-rr_tro_fe Y', '36-rr_tro_fe Z', '37-rl_fe_ti X', '37-rl_fe_ti Y', '37-rl_fe_ti Z', '38-rr_fe_ti X', '38-rr_fe_ti Y', '38-rr_fe_ti Z', '39-rl_ti_ta X', '39-rl_ti_ta Y', '39-rl_ti_ta Z', '40-rr_ti_ta X', '40-rr_ti_ta Y', '40-rr_ti_ta Z', '41-rl_ta_mt X', '41-rl_ta_mt Y', '41-rl_ta_mt Z', '42-rr_ta_mt X', '42-rr_ta_mt Y', '42-rr_ta_mt Z', '43-rl_mt X', '43-rl_mt Y', '43-rl_mt Z', '44-rr_mt X', '44-rr_mt Y', '44-rr_mt Z', '45-th_pet X', '45-th_pet Y', '45-th_pet Z', '46-pet_abd X', '46-pet_abd Y', '46-pet_abd Z', '47-abd X', '47-abd Y', '47-abd Z' ]

# On trie les colonnes pour pouvoirs les utiliser correctement plus tard
new_column_order = ['1-head X' , '1-head Y', '1-head Z', '2-neck X', '2-neck Y', '2-neck Z' , '45-th_pet X', '45-th_pet Y', '45-th_pet Z', '46-pet_abd X', '46-pet_abd Y', '46-pet_abd Z', '47-abd X', '47-abd Y', '47-abd Z', '3-fl_th_cox X', '3-fl_th_cox Y', '3-fl_th_cox Z', '5-fl_cox_tro X', '5-fl_cox_tro Y', '5-fl_cox_tro Z', '7-fl_tro_fe X', '7-fl_tro_fe Y', '7-fl_tro_fe Z', '9-fl_fe_ti X', '9-fl_fe_ti Y', '9-fl_fe_ti Z', '11-fl_ti_ta X', '11-fl_ti_ta Y', '11-fl_ti_ta Z', '13-fl_ta_mt X', '13-fl_ta_mt Y', '13-fl_ta_mt Z', '15-fl_mt X', '15-fl_mt Y', '15-fl_mt Z', '4-fr_th_cox X', '4-fr_th_cox Y', '4-fr_th_cox Z',  '6-fr_cox_tro X', '6-fr_cox_tro Y', '6-fr_cox_tro Z',  '8-fr_tro_fe X', '8-fr_tro_fe Y', '8-fr_tro_fe Z', '10-fr_fe_ti X', '10-fr_fe_ti Y', '10-fr_fe_ti Z', '12-fr_ti_ta X', '12-fr_ti_ta Y', '12-fr_ti_ta Z', '14-fr_ta_mt X', '14-fr_ta_mt Y', '14-fr_ta_mt Z',  '16-fr_mt X', '16-fr_mt Y', '16-fr_mt Z', '17-ml_th_cox X', '17-ml_th_cox Y', '17-ml_th_cox Z', '19-ml_cox_tro X', '19-ml_cox_tro Y', '19-ml_cox_tro Z', '21-ml_tro_fe X', '21-ml_tro_fe Y','21-ml_tro_fe Z', '23-ml_fe_ti X', '23-ml_fe_ti Y', '23-ml_fe_ti Z', '25-ml_ti_ta X', '25-ml_ti_ta Y', '25-ml_ti_ta Z', '27-ml_ta_mt X', '27-ml_ta_mt Y', '27-ml_ta_mt Z', '29-ml_mt X', '29-ml_mt Y', '29-ml_mt Z', '18-mr_th_cox X', '18-mr_th_cox Y', '18-mr_th_cox Z', '20-mr_cox_tro X', '20-mr_cox_tro Y', '20-mr_cox_tro Z', '22-mr_tro_fe X', '22-mr_tro_fe Y','22-mr_tro_fe Z', '24-mr_fe_ti X', '24-mr_fe_ti Y', '24-mr_fe_ti Z', '26-mr_ti_ta X', '26-mr_ti_ta Y', '26-mr_ti_ta Z', '28-mr_ta_mt X', '28-mr_ta_mt Y', '28-mr_ta_mt Z',  '30-mr_mt X', '30-mr_mt Y', '30-mr_mt Z', '31-rl_th_cox X', '31-rl_th_cox Y', '31-rl_th_cox Z', '33-rl_cox_tro X','33-rl_cox_tro Y', '33-rl_cox_tro Z', '35-rl_tro_fe X', '35-rl_tro_fe Y', '35-rl_tro_fe Z', '37-rl_fe_ti X', '37-rl_fe_ti Y', '37-rl_fe_ti Z', '39-rl_ti_ta X', '39-rl_ti_ta Y', '39-rl_ti_ta Z', '41-rl_ta_mt X', '41-rl_ta_mt Y', '41-rl_ta_mt Z', '43-rl_mt X', '43-rl_mt Y', '43-rl_mt Z', '32-rr_th_cox X', '32-rr_th_cox Y', '32-rr_th_cox Z',  '34-rr_cox_tro X', '34-rr_cox_tro Y', '34-rr_cox_tro Z',  '36-rr_tro_fe X', '36-rr_tro_fe Y', '36-rr_tro_fe Z', '38-rr_fe_ti X', '38-rr_fe_ti Y', '38-rr_fe_ti Z', '40-rr_ti_ta X', '40-rr_ti_ta Y', '40-rr_ti_ta Z', '42-rr_ta_mt X', '42-rr_ta_mt Y', '42-rr_ta_mt Z',  '44-rr_mt X', '44-rr_mt Y', '44-rr_mt Z' ] 
tableau_donnees_rangees = tableau.reindex(columns=new_column_order)

# On combine les 2 tableaux
new_tableau = pd.concat([new_tableau, tableau_donnees_rangees], axis=1)

new_tableau.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/1_données_rangées.xlsx') # Crée un nouveau tableur avec les données qui nous intéresse (utile pour une meilleure visualisation dans excel)


### On va filtrer nos données, créer nos graphes et les sauvegarder ###

x = 0
num_affichage = 1
i = 0
for x in range(0, new_tableau.shape[1]):    # Toutes les colonnes vont être traitées sauf la première
    try:
        #if (i < 3):    ## Utile pour analyse rapide
            temps = new_tableau.iloc[:,0]   # Permet d'obtenir les valeurs de la colonne temps
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
            plt.xlabel('Temps (s)')   # axe x
            plt.ylabel(f'Position {new_tableau.columns[x]} en mm')    # axe y
            plt.legend()     # légende
            filename = f"{num_affichage} ,{new_tableau.columns[x]}"      # J'incrémente le numéro d'affichage pour pouvoir avoir les graphes dans l'ordre de création dans mon document
            num_affichage += 1 
            plt.savefig(f'C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/4_Graphiques/1_Graphiques_mesures_en_fonction du temps/{filename}.png') # sauvegarde du graphe
            plt.show()
            new_tableau.iloc[:, x] = position_filtree    # Permet de remplacer la colonne de données avec les nouvelles données filtrées pour pouvoir enregistrer le tableur par la suite
            #i += 1     ## Utile pour analyse rapide
    except IndexError:
        print(f"Column index {x} is out of bounds.")   
        
        
### On va créer un tableau excel avec les nouvelles données filtrées pour pouvoir les utiliser pour nos calculs des positions des centres de gravités segmentaires ###
new_tableau.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/2_données_filtrées.xlsx') # Crée un nouveau tableur avec les données filtrées

print("Opération terminée")