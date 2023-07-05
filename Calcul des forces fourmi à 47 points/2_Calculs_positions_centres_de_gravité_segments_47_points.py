# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:29:23 2023

@author: pagro
"""

globals().clear()    # Supprime toutes les variables pour me permettre de relancer le code lorsque je veux faire de nouveaux essais

import pandas as pd

tableau_donnees_filtrees = pd.read_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/2_données_filtrées.xlsx', header=[0])

tableau_Cg_segments = tableau_donnees_filtrees.iloc[:, 1]     # Permet d'avoir la colonne "Temps" dans un premier temps

def coef(colonne_coef):     # Matrice qui va permettre d'accéder aux coefs
    matrice_coef = {
        'head': 0.5,
        'thorax': 0.5,
        'petiole': 0.5,
        'abdomen': 0.5,
        'coxa': 0.5,
        'trochanter': 0.5,
        'femur': 0.5,
        'tibia': 0.5,
        'tarse': 0.5,
        'metatarse': 0.5
    }
    coef = matrice_coef[colonne_coef]
    return coef

def pos(colonne_position):     # Matrice qui va permettre d'accéder aux positions des points
    position = tableau_donnees_filtrees[colonne_position].values
    return position

head_x = pos('1-head X') + coef('head') * (pos('2-neck X') - pos('1-head X'))
head_y = pos('1-head Y') + coef('head') * (pos('2-neck Y') - pos('1-head Y'))
head_z = pos('1-head Z') + coef('head') * (pos('2-neck Z') - pos('1-head Z'))
thorax_x = pos('2-neck X') + coef('thorax') * (pos('45-th_pet X') - pos('2-neck X'))
thorax_y = pos('2-neck Y') + coef('thorax') * (pos('45-th_pet Y') - pos('2-neck Y'))
thorax_z = pos('2-neck Z') + coef('thorax') * (pos('45-th_pet Z') - pos('2-neck Z'))
petiole_abdomen_x = pos('45-th_pet X') + coef('abdomen') * (pos('47-abd X') - pos('45-th_pet X'))      # Ici on calcule la position du centre de gravité du pétiole et abdomen réunis car dans l'article de Jordan, la masse est mesurée pour les 2 ensembles
petiole_abdomen_y = pos('45-th_pet Y') + coef('abdomen') * (pos('47-abd Y') - pos('45-th_pet Y'))      # Pour le coef, on aurait pu mettre 'petiole' aussi puis que les 2 sont égales à 0,5 ici
petiole_abdomen_z = pos('45-th_pet Z') + coef('abdomen') * (pos('47-abd Z') - pos('45-th_pet Z'))

fl_coxa_x = pos('3-fl_th_cox X') + coef('coxa') * (pos('5-fl_cox_tro X') - pos('3-fl_th_cox X'))
fl_coxa_y = pos('3-fl_th_cox Y') + coef('coxa') * (pos('5-fl_cox_tro Y') - pos('3-fl_th_cox Y'))
fl_coxa_z = pos('3-fl_th_cox Z') + coef('coxa') * (pos('5-fl_cox_tro Z') - pos('3-fl_th_cox Z'))
fl_trochanter_x = pos('5-fl_cox_tro X') + coef('trochanter') * (pos('7-fl_tro_fe X') - pos('5-fl_cox_tro X'))
fl_trochanter_y = pos('5-fl_cox_tro Y') + coef('trochanter') * (pos('7-fl_tro_fe Y') - pos('5-fl_cox_tro Y'))
fl_trochanter_z = pos('5-fl_cox_tro Z') + coef('trochanter') * (pos('7-fl_tro_fe Z') - pos('5-fl_cox_tro Z'))
fl_femur_x = pos('7-fl_tro_fe X') + coef('femur') * (pos('9-fl_fe_ti X') - pos('7-fl_tro_fe X'))
fl_femur_y = pos('7-fl_tro_fe Y') + coef('femur') * (pos('9-fl_fe_ti Y') - pos('7-fl_tro_fe Y'))
fl_femur_z = pos('7-fl_tro_fe Z') + coef('femur') * (pos('9-fl_fe_ti Z') - pos('7-fl_tro_fe Z'))
fl_tibia_x = pos('9-fl_fe_ti X') + coef('tibia') * (pos('11-fl_ti_ta X') - pos('9-fl_fe_ti X'))
fl_tibia_y = pos('9-fl_fe_ti Y') + coef('tibia') * (pos('11-fl_ti_ta Y') - pos('9-fl_fe_ti Y'))
fl_tibia_z = pos('9-fl_fe_ti Z') + coef('tibia') * (pos('11-fl_ti_ta Z') - pos('9-fl_fe_ti Z'))
fl_tarse_metatarse_x = pos('11-fl_ti_ta X') + coef('tarse') * (pos('15-fl_mt X') - pos('11-fl_ti_ta X'))     # Même raisonnement que plus haut avec le pétiole et l'abdomen mais cette fois-ci pour le tarse et métatarse
fl_tarse_metatarse_y = pos('11-fl_ti_ta Y') + coef('tarse') * (pos('15-fl_mt Y') - pos('11-fl_ti_ta Y'))
fl_tarse_metatarse_z = pos('11-fl_ti_ta Z') + coef('tarse') * (pos('15-fl_mt Z') - pos('11-fl_ti_ta Z'))

fr_coxa_x = pos('4-fr_th_cox X') + coef('coxa') * (pos('6-fr_cox_tro X') - pos('4-fr_th_cox X'))
fr_coxa_y = pos('4-fr_th_cox Y') + coef('coxa') * (pos('6-fr_cox_tro Y') - pos('4-fr_th_cox Y'))
fr_coxa_z = pos('4-fr_th_cox Z') + coef('coxa') * (pos('6-fr_cox_tro Z') - pos('4-fr_th_cox Z'))
fr_trochanter_x = pos('6-fr_cox_tro X') + coef('trochanter') * (pos('8-fr_tro_fe X') - pos('6-fr_cox_tro X'))
fr_trochanter_y = pos('6-fr_cox_tro Y') + coef('trochanter') * (pos('8-fr_tro_fe Y') - pos('6-fr_cox_tro Y'))
fr_trochanter_z = pos('6-fr_cox_tro Z') + coef('trochanter') * (pos('8-fr_tro_fe Z') - pos('6-fr_cox_tro Z'))
fr_femur_x = pos('8-fr_tro_fe X') + coef('femur') * (pos('10-fr_fe_ti X') - pos('8-fr_tro_fe X'))
fr_femur_y = pos('8-fr_tro_fe Y') + coef('femur') * (pos('10-fr_fe_ti Y') - pos('8-fr_tro_fe Y'))
fr_femur_z = pos('8-fr_tro_fe Z') + coef('femur') * (pos('10-fr_fe_ti Z') - pos('8-fr_tro_fe Z'))
fr_tibia_x = pos('10-fr_fe_ti X') + coef('tibia') * (pos('12-fr_ti_ta X') - pos('10-fr_fe_ti X'))
fr_tibia_y = pos('10-fr_fe_ti Y') + coef('tibia') * (pos('12-fr_ti_ta Y') - pos('10-fr_fe_ti Y'))
fr_tibia_z = pos('10-fr_fe_ti Z') + coef('tibia') * (pos('12-fr_ti_ta Z') - pos('10-fr_fe_ti Z'))
fr_tarse_metatarse_x = pos('12-fr_ti_ta X') + coef('tarse') * (pos('16-fr_mt X') - pos('12-fr_ti_ta X')) 
fr_tarse_metatarse_y = pos('12-fr_ti_ta Y') + coef('tarse') * (pos('16-fr_mt Y') - pos('12-fr_ti_ta Y'))
fr_tarse_metatarse_z = pos('12-fr_ti_ta Z') + coef('tarse') * (pos('16-fr_mt Z') - pos('12-fr_ti_ta Z'))

ml_coxa_x = pos('17-ml_th_cox X') + coef('coxa') * (pos('19-ml_cox_tro X') - pos('17-ml_th_cox X'))
ml_coxa_y = pos('17-ml_th_cox Y') + coef('coxa') * (pos('19-ml_cox_tro Y') - pos('17-ml_th_cox Y'))
ml_coxa_z = pos('17-ml_th_cox Z') + coef('coxa') * (pos('19-ml_cox_tro Z') - pos('17-ml_th_cox Z'))
ml_trochanter_x = pos('19-ml_cox_tro X') + coef('trochanter') * (pos('21-ml_tro_fe X') - pos('19-ml_cox_tro X'))
ml_trochanter_y = pos('19-ml_cox_tro Y') + coef('trochanter') * (pos('21-ml_tro_fe Y') - pos('19-ml_cox_tro Y'))
ml_trochanter_z = pos('19-ml_cox_tro Z') + coef('trochanter') * (pos('21-ml_tro_fe Z') - pos('19-ml_cox_tro Z'))
ml_femur_x = pos('21-ml_tro_fe X') + coef('femur') * (pos('23-ml_fe_ti X') - pos('21-ml_tro_fe X'))
ml_femur_y = pos('21-ml_tro_fe Y') + coef('femur') * (pos('23-ml_fe_ti Y') - pos('21-ml_tro_fe Y'))
ml_femur_z = pos('21-ml_tro_fe Z') + coef('femur') * (pos('23-ml_fe_ti Z') - pos('21-ml_tro_fe Z'))
ml_tibia_x = pos('23-ml_fe_ti X') + coef('tibia') * (pos('25-ml_ti_ta X') - pos('23-ml_fe_ti X'))
ml_tibia_y = pos('23-ml_fe_ti Y') + coef('tibia') * (pos('25-ml_ti_ta Y') - pos('23-ml_fe_ti Y'))
ml_tibia_z = pos('23-ml_fe_ti Z') + coef('tibia') * (pos('25-ml_ti_ta Z') - pos('23-ml_fe_ti Z'))
ml_tarse_metatarse_x = pos('25-ml_ti_ta X') + coef('tarse') * (pos('29-ml_mt X') - pos('25-ml_ti_ta X')) 
ml_tarse_metatarse_y = pos('25-ml_ti_ta Y') + coef('tarse') * (pos('29-ml_mt Y') - pos('25-ml_ti_ta Y'))
ml_tarse_metatarse_z = pos('25-ml_ti_ta Z') + coef('tarse') * (pos('29-ml_mt Z') - pos('25-ml_ti_ta Z'))

mr_coxa_x = pos('18-mr_th_cox X') + coef('coxa') * (pos('20-mr_cox_tro X') - pos('18-mr_th_cox X'))
mr_coxa_y = pos('18-mr_th_cox Y') + coef('coxa') * (pos('20-mr_cox_tro Y') - pos('18-mr_th_cox Y'))
mr_coxa_z = pos('18-mr_th_cox Z') + coef('coxa') * (pos('20-mr_cox_tro Z') - pos('18-mr_th_cox Z'))
mr_trochanter_x = pos('20-mr_cox_tro X') + coef('trochanter') * (pos('22-mr_tro_fe X') - pos('20-mr_cox_tro X'))
mr_trochanter_y = pos('20-mr_cox_tro Y') + coef('trochanter') * (pos('22-mr_tro_fe Y') - pos('20-mr_cox_tro Y'))
mr_trochanter_z = pos('20-mr_cox_tro Z') + coef('trochanter') * (pos('22-mr_tro_fe Z') - pos('20-mr_cox_tro Z'))
mr_femur_x = pos('22-mr_tro_fe X') + coef('femur') * (pos('24-mr_fe_ti X') - pos('22-mr_tro_fe X'))
mr_femur_y = pos('22-mr_tro_fe Y') + coef('femur') * (pos('24-mr_fe_ti Y') - pos('22-mr_tro_fe Y'))
mr_femur_z = pos('22-mr_tro_fe Z') + coef('femur') * (pos('24-mr_fe_ti Z') - pos('22-mr_tro_fe Z'))
mr_tibia_x = pos('24-mr_fe_ti X') + coef('tibia') * (pos('26-mr_ti_ta X') - pos('24-mr_fe_ti X'))
mr_tibia_y = pos('24-mr_fe_ti Y') + coef('tibia') * (pos('26-mr_ti_ta Y') - pos('24-mr_fe_ti Y'))
mr_tibia_z = pos('24-mr_fe_ti Z') + coef('tibia') * (pos('26-mr_ti_ta Z') - pos('24-mr_fe_ti Z'))
mr_tarse_metatarse_x = pos('26-mr_ti_ta X') + coef('tarse') * (pos('30-mr_mt X') - pos('26-mr_ti_ta X')) 
mr_tarse_metatarse_y = pos('26-mr_ti_ta Y') + coef('tarse') * (pos('30-mr_mt Y') - pos('26-mr_ti_ta Y'))
mr_tarse_metatarse_z = pos('26-mr_ti_ta Z') + coef('tarse') * (pos('30-mr_mt Z') - pos('26-mr_ti_ta Z'))

rl_coxa_x = pos('31-rl_th_cox X') + coef('coxa') * (pos('33-rl_cox_tro X') - pos('31-rl_th_cox X'))
rl_coxa_y = pos('31-rl_th_cox Y') + coef('coxa') * (pos('33-rl_cox_tro Y') - pos('31-rl_th_cox Y'))
rl_coxa_z = pos('31-rl_th_cox Z') + coef('coxa') * (pos('33-rl_cox_tro Z') - pos('31-rl_th_cox Z'))
rl_trochanter_x = pos('33-rl_cox_tro X') + coef('trochanter') * (pos('35-rl_tro_fe X') - pos('33-rl_cox_tro X'))
rl_trochanter_y = pos('33-rl_cox_tro Y') + coef('trochanter') * (pos('35-rl_tro_fe Y') - pos('33-rl_cox_tro Y'))
rl_trochanter_z = pos('33-rl_cox_tro Z') + coef('trochanter') * (pos('35-rl_tro_fe Z') - pos('33-rl_cox_tro Z'))
rl_femur_x = pos('35-rl_tro_fe X') + coef('femur') * (pos('37-rl_fe_ti X') - pos('35-rl_tro_fe X'))
rl_femur_y = pos('35-rl_tro_fe Y') + coef('femur') * (pos('37-rl_fe_ti Y') - pos('35-rl_tro_fe Y'))
rl_femur_z = pos('35-rl_tro_fe Z') + coef('femur') * (pos('37-rl_fe_ti Z') - pos('35-rl_tro_fe Z'))
rl_tibia_x = pos('37-rl_fe_ti X') + coef('tibia') * (pos('39-rl_ti_ta X') - pos('37-rl_fe_ti X'))
rl_tibia_y = pos('37-rl_fe_ti Y') + coef('tibia') * (pos('39-rl_ti_ta Y') - pos('37-rl_fe_ti Y'))
rl_tibia_z = pos('37-rl_fe_ti Z') + coef('tibia') * (pos('39-rl_ti_ta Z') - pos('37-rl_fe_ti Z'))
rl_tarse_metatarse_x = pos('39-rl_ti_ta X') + coef('tarse') * (pos('43-rl_mt X') - pos('39-rl_ti_ta X')) 
rl_tarse_metatarse_y = pos('39-rl_ti_ta Y') + coef('tarse') * (pos('43-rl_mt Y') - pos('39-rl_ti_ta Y'))
rl_tarse_metatarse_z = pos('39-rl_ti_ta Z') + coef('tarse') * (pos('43-rl_mt Z') - pos('39-rl_ti_ta Z'))

rr_coxa_x = pos('32-rr_th_cox X') + coef('coxa') * (pos('34-rr_cox_tro X') - pos('32-rr_th_cox X'))
rr_coxa_y = pos('32-rr_th_cox Y') + coef('coxa') * (pos('34-rr_cox_tro Y') - pos('32-rr_th_cox Y'))
rr_coxa_z = pos('32-rr_th_cox Z') + coef('coxa') * (pos('34-rr_cox_tro Z') - pos('32-rr_th_cox Z'))
rr_trochanter_x = pos('34-rr_cox_tro X') + coef('trochanter') * (pos('36-rr_tro_fe X') - pos('34-rr_cox_tro X'))
rr_trochanter_y = pos('34-rr_cox_tro Y') + coef('trochanter') * (pos('36-rr_tro_fe Y') - pos('34-rr_cox_tro Y'))
rr_trochanter_z = pos('34-rr_cox_tro Z') + coef('trochanter') * (pos('36-rr_tro_fe Z') - pos('34-rr_cox_tro Z'))
rr_femur_x = pos('36-rr_tro_fe X') + coef('femur') * (pos('38-rr_fe_ti X') - pos('36-rr_tro_fe X'))
rr_femur_y = pos('36-rr_tro_fe Y') + coef('femur') * (pos('38-rr_fe_ti Y') - pos('36-rr_tro_fe Y'))
rr_femur_z = pos('36-rr_tro_fe Z') + coef('femur') * (pos('38-rr_fe_ti Z') - pos('36-rr_tro_fe Z'))
rr_tibia_x = pos('38-rr_fe_ti X') + coef('tibia') * (pos('40-rr_ti_ta X') - pos('38-rr_fe_ti X'))
rr_tibia_y = pos('38-rr_fe_ti Y') + coef('tibia') * (pos('40-rr_ti_ta Y') - pos('38-rr_fe_ti Y'))
rr_tibia_z = pos('38-rr_fe_ti Z') + coef('tibia') * (pos('40-rr_ti_ta Z') - pos('38-rr_fe_ti Z'))
rr_tarse_metatarse_x = pos('40-rr_ti_ta X') + coef('tarse') * (pos('44-rr_mt X') - pos('40-rr_ti_ta X')) 
rr_tarse_metatarse_y = pos('40-rr_ti_ta Y') + coef('tarse') * (pos('44-rr_mt Y') - pos('40-rr_ti_ta Y'))
rr_tarse_metatarse_z = pos('40-rr_ti_ta Z') + coef('tarse') * (pos('44-rr_mt Z') - pos('40-rr_ti_ta Z'))



new_columns = pd.DataFrame({      # Création des nouvelles colonnes au format DataFrame
    'head_x': head_x,
    'head_y': head_y,
    'head_z': head_z,
    'thorax_x': thorax_x,
    'thorax_y': thorax_y,
    'thorax_z': thorax_z,
    'petiole_abdomen_x': petiole_abdomen_x,
    'petiole_abdomen_y': petiole_abdomen_y,
    'petiole_abdomen_z': petiole_abdomen_z,
    'fl_coxa_x': fl_coxa_x,
    'fl_coxa_y': fl_coxa_y,
    'fl_coxa_z': fl_coxa_z,
    'fl_trochanter_x': fl_trochanter_x,
    'fl_trochanter_y': fl_trochanter_y,
    'fl_trochanter_z': fl_trochanter_z,
    'fl_femur_x': fl_femur_x,
    'fl_femur_y': fl_femur_y,
    'fl_femur_z': fl_femur_z,
    'fl_tibia_x': fl_tibia_x,
    'fl_tibia_y': fl_tibia_y,
    'fl_tibia_z': fl_tibia_z,
    'fl_tarse_metatarse_x': fl_tarse_metatarse_x,
    'fl_tarse_metatarse_y': fl_tarse_metatarse_y,
    'fl_tarse_metatarse_z': fl_tarse_metatarse_z,
    'fr_coxa_x': fr_coxa_x,
    'fr_coxa_y': fr_coxa_y,
    'fr_coxa_z': fr_coxa_z,
    'fr_trochanter_x': fr_trochanter_x,
    'fr_trochanter_y': fr_trochanter_y,
    'fr_trochanter_z': fr_trochanter_z,
    'fr_femur_x': fr_femur_x,
    'fr_femur_y': fr_femur_y,
    'fr_femur_z': fr_femur_z,
    'fr_tibia_x': fr_tibia_x,
    'fr_tibia_y': fr_tibia_y,
    'fr_tibia_z': fr_tibia_z,
    'fr_tarse_metatarse_x': fr_tarse_metatarse_x,
    'fr_tarse_metatarse_y': fr_tarse_metatarse_y,
    'fr_tarse_metatarse_z': fr_tarse_metatarse_z,
    'ml_coxa_x': ml_coxa_x,
    'ml_coxa_y': ml_coxa_y,
    'ml_coxa_z': ml_coxa_z,
    'ml_trochanter_x': ml_trochanter_x,
    'ml_trochanter_y': ml_trochanter_y,
    'ml_trochanter_z': ml_trochanter_z,
    'ml_femur_x': ml_femur_x,
    'ml_femur_y': ml_femur_y,
    'ml_femur_z': ml_femur_z,
    'ml_tibia_x': ml_tibia_x,
    'ml_tibia_y': ml_tibia_y,
    'ml_tibia_z': ml_tibia_z,
    'ml_tarse_metatarse_x': ml_tarse_metatarse_x,
    'ml_tarse_metatarse_y': ml_tarse_metatarse_y,
    'ml_tarse_metatarse_z': ml_tarse_metatarse_z,
    'mr_coxa_x': mr_coxa_x,
    'mr_coxa_y': mr_coxa_y,
    'mr_coxa_z': mr_coxa_z,
    'mr_trochanter_x': mr_trochanter_x,
    'mr_trochanter_y': mr_trochanter_y,
    'mr_trochanter_z': mr_trochanter_z,
    'mr_femur_x': mr_femur_x,
    'mr_femur_y': mr_femur_y,
    'mr_femur_z': mr_femur_z,
    'mr_tibia_x': mr_tibia_x,
    'mr_tibia_y': mr_tibia_y,
    'mr_tibia_z': mr_tibia_z,
    'mr_tarse_metatarse_x': mr_tarse_metatarse_x,
    'mr_tarse_metatarse_y': mr_tarse_metatarse_y,
    'mr_tarse_metatarse_z': mr_tarse_metatarse_z,
    'rl_coxa_x': rl_coxa_x,
    'rl_coxa_y': rl_coxa_y,
    'rl_coxa_z': rl_coxa_z,
    'rl_trochanter_x': rl_trochanter_x,
    'rl_trochanter_y': rl_trochanter_y,
    'rl_trochanter_z': rl_trochanter_z,
    'rl_femur_x': rl_femur_x,
    'rl_femur_y': rl_femur_y,
    'rl_femur_z': rl_femur_z,
    'rl_tibia_x': rl_tibia_x,
    'rl_tibia_y': rl_tibia_y,
    'rl_tibia_z': rl_tibia_z,
    'rl_tarse_metatarse_x': rl_tarse_metatarse_x,
    'rl_tarse_metatarse_y': rl_tarse_metatarse_y,
    'rl_tarse_metatarse_z': rl_tarse_metatarse_z,
    'rr_coxa_x': rr_coxa_x,
    'rr_coxa_y': rr_coxa_y,
  'rr_coxa_z': rr_coxa_z,
  'rr_trochanter_x': rr_trochanter_x,
  'rr_trochanter_y': rr_trochanter_y,
  'rr_trochanter_z': rr_trochanter_z,
  'rr_femur_x': rr_femur_x,
  'rr_femur_y': rr_femur_y,
  'rr_femur_z': rr_femur_z,
  'rr_tibia_x': rr_tibia_x,
  'rr_tibia_y': rr_tibia_y,
  'rr_tibia_z': rr_tibia_z,
  'rr_tarse_metatarse_x': rr_tarse_metatarse_x,
  'rr_tarse_metatarse_y': rr_tarse_metatarse_y,
  'rr_tarse_metatarse_z': rr_tarse_metatarse_z
})

tableau_Cg_segments = pd.concat([tableau_Cg_segments, new_columns], axis=1)        # Concaténation des nouvelles colonnes créées et la colonne temps du "tableau_Cg_segments" (je n'ai pas réussi à faire autrement)


tableau_Cg_segments.to_excel('C:/Users/pagro/Desktop/PAS SUPPRIMER/Stage L3 BIOMIP/Travaux PAG/2_Calcul_Accelerations_Cg_segments_47_points/3_Tableaux_excel/3_Positions_Cg_segments.xlsx')# On sauvegarde les nouvelles données dans un tableur
 
print("Opération terminée")