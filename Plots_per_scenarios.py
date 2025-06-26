#prendre les données de case_studies et d'un dossier qu'on donnera le nom et les plots
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tabulate
import math

sys.path.append("c:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/case_studies")
folder = "Data/2050_scenario1_trends"
folder = "Data/2050_scenario2_sobriety"
folder = "Data/2050_scenario3_efficiency"

#get access to the folder which is the folder after the case_studiesr
path = os.path.join("c:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/case_studies", folder)
path = os.path.join(path, "output")

consumptionperarea = False
fleetsize = False
costtransportsector = True

#colors 
#NONELEC color other than the others
NONELEC_color = "#ff7f0e"
elec_color = "#1f77b4"
PHEV_color = "#419ede"
HEV_color = "#41b8de"
gasoline_color = "#ff7f0e"
diesel_color = "#2ca02c"
gas_color = "#d62728"
h2_color = "#9467bd"
total_color = "#8c564b"

if costtransportsector :
    #take the data year_balance.txt
    filename = "cost_breakdown.txt"

    #open the file in a dataframe
    data = np.genfromtxt(os.path.join(path, filename), delimiter="\t", skip_header=0, dtype=None, encoding=None)

    df = pd.read_csv(os.path.join(path, filename), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces

    #plot the data if the first of the row is a specific name in a list and isELECTRICITY	GASOLINE	DIESEL	LFO	GAS H2
    #list of the names we want to plot

    # Liste des énergies et noms
    list_name = [
        "BIKE_NONELEC_URBAN",
        "BIKE_ELEC_URBAN",
        "MOTORCYCLE_GASOLINE_URBAN",
        "MOTORCYCLE_BEV_URBAN",
        "CAR_GASOLINE_URBAN",
        "CAR_DIESEL_URBAN",
        "CAR_HEV_URBAN",
        "CAR_PHEV_URBAN",
        "CAR_BEV_URBAN",
        "CAR_FC_URBAN",
        "CAR_NG_URBAN",
        "BUS_DIESEL_URBAN",
        "BUS_HYDIESEL_URBAN",
        "BUS_ELEC_URBAN",
        "BUS_FC_URBAN",
        "BUS_NG_URBAN",
        "TRAMWAY_ELEC_URBAN",
        "METRO_ELEC_URBAN",
        "BIKE_NONELEC_RURAL",
        "BIKE_ELEC_RURAL",
        "MOTORCYCLE_GASOLINE_RURAL",
        "MOTORCYCLE_BEV_RURAL",
        "CAR_GASOLINE_RURAL",
        "CAR_DIESEL_RURAL",
        "CAR_HEV_RURAL",
        "CAR_PHEV_RURAL",
        "CAR_BEV_RURAL",
        "CAR_FC_RURAL",
        "CAR_NG_RURAL",
        "BUS_DIESEL_RURAL",
        "BUS_HYDIESEL_RURAL",
        "BUS_ELEC_RURAL",
        "TRAIN_ELEC_RURAL"
    ]
    list_costs = ['C_inv', 'C_maint']
    
    #faire un graphe avec comme  truc non active road , active road  and railways and total

    non_active_road_inv = 0
    non_active_road_main = 0
    non_active_road_op = 0
    non_active_road_inf_inv = 0
    non_active_road_inf_main = 0
    active_road_inv = 0
    active_road_main = 0
    active_road_op = 0
    active_road_inf_inv = 0
    active_road_inf_main = 0
    railways_inv = 0
    railways_main = 0
    railways_op = 0
    railways_inf_inv = 0
    railways_inf_main = 0
    cout_public_inv = 0
    cout_public_main = 0
    cout_public_op = 0
    cout_public_inf_inv = 0
    cout_public_inf_main = 0
    cout_prive_inv = 0
    cout_prive_main = 0
    cout_prive_op = 0

    # Boucle sur les noms à chercher
    for name in list_name:
        for i in range(len(df)):
            if name in df.iloc[i, 0]:
                # Parcours des énergies
                for cost in list_costs:
                    if cost in df.columns:
                        value = float(df.loc[i, cost])
                        value = round(value, 3)
                        if value != 0:
                            if "BIKE_NONELEC" in name and "C_inv" in cost:
                                active_road_inv += value
                            if "BIKE_NONELEC" in name and "C_maint" in cost:
                                active_road_main += value
                            if "BIKE_ELEC" in name and "C_inv" in cost:
                                active_road_inv += value
                            if "BIKE_ELEC" in name and "C_maint" in cost:
                                active_road_main += value
                            if "MOTORCYCLE_GASOLINE" in name and "C_inv" in cost:
                                non_active_road_inv += value
                            if "MOTORCYCLE_GASOLINE" in name and "C_maint" in cost:
                                non_active_road_main += value
                            if "MOTORCYCLE_BEV" in name and "C_inv" in cost:
                                non_active_road_inv += value
                            if "MOTORCYCLE_BEV" in name and "C_maint" in cost:
                                non_active_road_main += value
                            if "CAR_GASOLINE" in name and "C_inv" in cost:
                                non_active_road_inv += value    
                            if "CAR_GASOLINE" in name and "C_maint" in cost:
                                non_active_road_main += value
                            if "CAR_DIESEL" in name and "C_inv" in cost:
                                non_active_road_inv += value    
                            if "CAR_DIESEL" in name and "C_maint" in cost:
                                non_active_road_main += value
                            if "CAR_HEV" in name and "C_inv" in cost:
                                non_active_road_inv += value
                            if "CAR_HEV" in name and "C_maint" in cost:
                                non_active_road_main += value
                            if "CAR_PHEV" in name and "C_inv" in cost:
                                non_active_road_inv += value
                            if "CAR_PHEV" in name and "C_maint" in cost:
                                non_active_road_main += value
                            if "CAR_BEV" in name and "C_inv" in cost:
                                non_active_road_inv += value
                            if "CAR_BEV" in name and "C_maint" in cost:
                                non_active_road_main += value
                            if "CAR_FC" in name and "C_inv" in cost:
                                non_active_road_inv += value
                            if "CAR_FC" in name and "C_maint" in cost:
                                non_active_road_main += value
                            if "CAR_NG" in name and "C_inv" in cost:
                                non_active_road_inv += value
                            if "CAR_NG" in name and "C_maint" in cost:
                                non_active_road_main += value
                            if "BUS_DIESEL" in name and "C_inv" in cost:
                                non_active_road_inv += value
                                cout_public_inv += value
                                cout_prive_inv-= value
                            if "BUS_DIESEL" in name and "C_maint" in cost:
                                non_active_road_main += value
                                cout_public_main += value
                                cout_prive_main -= value
                            if "BUS_HYDIESEL" in name and "C_inv" in cost:
                                non_active_road_inv += value
                                cout_public_inv += value
                                cout_prive_inv -= value
                            if "BUS_HYDIESEL" in name and "C_maint" in cost:
                                non_active_road_main += value
                                cout_public_main += value
                                cout_prive_main-= value
                            if "BUS_ELEC" in name and "C_inv" in cost:
                                non_active_road_inv += value
                                cout_public_inv += value
                                cout_prive_main -= value
                            if "BUS_ELEC" in name and "C_maint" in cost:
                                non_active_road_main += value
                                cout_public_main += value
                                cout_prive_main -= value
                            if "BUS_FC" in name and "C_inv" in cost:
                                non_active_road_inv += value
                                cout_public_inv += value
                                cout_prive_inv -= value
                            if "BUS_FC" in name and "C_maint" in cost:
                                non_active_road_main += value
                                cout_public_main += value
                                cout_prive_main -= value
                            if "BUS_NG" in name and "C_inv" in cost:
                                non_active_road_inv += value
                                cout_public_inv += value
                                cout_prive_inv -= value
                            if "BUS_NG" in name and "C_maint" in cost:
                                non_active_road_main += value
                                cout_public_main += value
                                cout_prive_main -= value
                            if "TRAIN_ELEC" in name and "C_inv" in cost:
                                railways_inv += value
                            if "TRAIN_ELEC" in name and "C_maint" in cost:
                                railways_main += value
                            if "TRAMWAY_ELEC" in name and "C_inv" in cost:
                                railways_inv += value
                            if "TRAMWAY_ELEC" in name and "C_maint" in cost:
                                railways_main += value
                            if "METRO_ELEC" in name and "C_inv" in cost:
                                railways_inv += value
                            if "METRO_ELEC" in name and "C_maint" in cost:
                                railways_main += value
    
    
    #open this excel file and take the data of the lifetime of the infrastructure
    filename = "C:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/" + folder +"/Infrastructure_info.xlsx"
    data_infra = pd.read_excel(filename, engine='openpyxl')
    
    #take the data of the lifetime of the infrastructure
    #open the file
    def annualisation(lifetime):
        i_rate = 0.015
        return i_rate * (1 + i_rate)**lifetime / (((1 + i_rate)**lifetime) - 1)

    #annualised the c_inv which is the second column in the data_infra and plot it by adding a table
    #add new columns to the data_infra names c_inv annualised
    data_infra["c_inv_annualised"] = data_infra["c_inv"] * annualisation(data_infra["lifetime"]) * data_infra["[#]"]
    data_infra["c_maint_total"] = 0.0
    #mettre dans la colonne c_maint_total et ligne km_active_road le produit de c_maint et [#] tjs dans la ligne km_active_road
    data_infra.loc[data_infra["Categories"] == "km_active_road", "c_maint_total"] = data_infra["c_maint"] * data_infra["[#]"]

    filenamebis = "year_balance.txt"
    dfbis = pd.read_csv(os.path.join(path, filenamebis), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    listdeskm = ["MOB_PUBLIC_RURAL", "MOB_PUBLIC_URBAN"]


    for i in range(len(dfbis)):
        if "BUS" in dfbis.iloc[i, 0]:
            for km in listdeskm:
                if km in dfbis.columns:
                    value = float(dfbis.loc[i, km])
                    value = round(value, 3)
                    if value != 0:
                        value = value * 10**6
                        data_infra.loc[data_infra["Categories"] == "km_non_active_road", "c_maint_total"] += value * data_infra.loc[data_infra["Categories"] == "km_non_active_road", "c_maint"] / data_infra.loc[data_infra["Categories"] == "km_non_active_road", "occupancy"]
                        
    for i in range(len(dfbis)):
        if "TRAM" in dfbis.iloc[i, 0]:
            for km in listdeskm:
                if km in dfbis.columns:
                    value = float(dfbis.loc[i, km])
                    value = round(value, 3)
                    if value != 0:
                        value = value * 10**6
                        data_infra.loc[data_infra["Categories"] == "km_railways", "c_maint_total"] += value * data_infra.loc[data_infra["Categories"] == "km_railways", "c_maint"] / data_infra.loc[data_infra["Categories"] == "km_railways", "occupancy"]
    
    for i in range(len(dfbis)):
        if "METRO" in dfbis.iloc[i, 0]:
            for km in listdeskm:
                if km in dfbis.columns:
                    value = float(dfbis.loc[i, km])
                    value = round(value, 3)
                    if value != 0:
                        value = value * 10**6
                        data_infra.loc[data_infra["Categories"] == "km_railways", "c_maint_total"] += value * data_infra.loc[data_infra["Categories"] == "km_railways", "c_maint"] / data_infra.loc[data_infra["Categories"] == "km_railways", "occupancy"]
    
    for i in range(len(dfbis)):
        if "TRAIN" in dfbis.iloc[i, 0]:
            for km in listdeskm:
                if km in dfbis.columns:
                    value = float(dfbis.loc[i, km])
                    value = round(value, 3)
                    if value != 0:
                        value = value * 10**6
                        data_infra.loc[data_infra["Categories"] == "km_train", "c_maint_total"] += value * data_infra.loc[data_infra["Categories"] == "km_train", "c_maint"] / data_infra.loc[data_infra["Categories"] == "km_train", "occupancy"]
    listkmprivate = ["MOB_PRIVATE_NA_RURAL", "MOB_PRIVATE_NA_URBAN", "MOB_PRIVATE_A_RURAL", "MOB_PRIVATE_A_URBAN","MOB_PUBLIC_URBAN", "MOB_PUBLIC_RURAL"]
    for i in range(len(dfbis)):
        typesofcars = ["CAR_GASOLINE", "CAR_DIESEL", "CAR_HEV", "CAR_PHEV", "CAR_FC", "CAR_NG"]
        for cars in typesofcars:
            if cars in dfbis.iloc[i, 0]:
                for km in listkmprivate:
                    if km in dfbis.columns:
                        value = float(dfbis.loc[i, km])
                        #toujours arrondir la valeur value vers l'unité d'au dessus
                        value = round(value, 3)

                        if value >= 1:
                            value = value * 10**6
                            idx = data_infra.index[data_infra["Categories"] == "number_fuelstation"]
                            data_infra.at[idx[0], "[#]"] += round(value / 
                                                                    data_infra.loc[data_infra["Categories"] == "km_active_road", "occupancy"].values[0] /
                                                                    data_infra.loc[data_infra["Categories"] == "km_active_road", "vehcap"].values[0] /
                                                                    1900, 2)
        if "CAR_BEV" in dfbis.iloc[i, 0]: 
             for km in listkmprivate:
                    if km in dfbis.columns:
                        value = float(dfbis.loc[i, km])
                        #toujours arrondir la valeur value vers l'unité d'au dessus
                        value = round(value, 3)
                        if value >= 1:
                            value = value * 10**6
                            idx = data_infra.index[data_infra["Categories"] == "number_elec_charging_voiture"]
                            data_infra.at[idx[0], "[#]"] += round(value /(data_infra.loc[data_infra["Categories"] == "km_active_road", "occupancy"].values[0] *
                                                                    data_infra.loc[data_infra["Categories"] == "km_active_road", "vehcap"].values[0]) * 1.3, 0)
                    

        if "MOTORCYCLE_GASOLINE" in dfbis.iloc[i, 0]:
            for km in listkmprivate:
                if km in dfbis.columns:
                    value = float(dfbis.loc[i, km])
                    value = round(value, 3)
                    if value >= 1:
                        value = value * 10**6
                        idx = data_infra.index[data_infra["Categories"] == "number_fuelstation"]
                        data_infra.at[idx[0], "[#]"] += round(value /1790/ 1900, 2)
        
        typesofbuses = ["BUS_DIESEL", "BUS_HYDIESEL", "BUS_FC", "BUS_NG"]
        for buses in typesofbuses:
            if buses in dfbis.iloc[i, 0]:
                for km in listkmprivate:
                    if km in dfbis.columns:
                        value = float(dfbis.loc[i, km])
                        value = round(value, 3)
                        if value >= 1:
                            value = value * 10**6
                            idx = data_infra.index[data_infra["Categories"] == "number_fuelstation"]
                            data_infra.at[idx[0], "[#]"] += round(value / 
                                                                    data_infra.loc[data_infra["Categories"] == "km_non_active_road", "occupancy"].values[0] /
                                                                    data_infra.loc[data_infra["Categories"] == "km_non_active_road", "vehcap"].values[0] /
                                                                    1900, 2)
                            idx = data_infra.index[data_infra["Categories"] == "number_elec_charging_bus"]
                            data_infra.at[idx[0], "[#]"] += round(value / 
                                                                    data_infra.loc[data_infra["Categories"] == "km_non_active_road", "occupancy"].values[0] /
                                                                    data_infra.loc[data_infra["Categories"] == "km_non_active_road", "vehcap"].values[0], 0)

        

    #ceil the [#] of number_fuelstation
    idx = data_infra.index[data_infra["Categories"] == "number_fuelstation"]
    data_infra.at[idx[0], "[#]"] = math.ceil(data_infra.at[idx[0], "[#]"])
    data_infra.loc[data_infra["Categories"] == "number_fuelstation", "c_inv_annualised"] += data_infra.at[idx[0], "[#]"] * annualisation(data_infra["lifetime"]) * data_infra.loc[data_infra["Categories"] == "number_fuelstation", "c_inv"].values[0]
    data_infra.loc[data_infra["Categories"] == "number_fuelstation", "c_maint_total"] += data_infra.at[idx[0], "[#]"] * data_infra.loc[data_infra["Categories"] == "number_fuelstation", "c_maint"].values[0]
    idx = data_infra.index[data_infra["Categories"] == "number_elec_charging_voiture"]
    data_infra.at[idx[0], "[#]"] = math.ceil(data_infra.at[idx[0], "[#]"])
    data_infra.loc[data_infra["Categories"] == "number_elec_charging_voiture", "c_inv_annualised"] += data_infra.at[idx[0], "[#]"] * annualisation(data_infra["lifetime"]) * data_infra.loc[data_infra["Categories"] == "number_elec_charging_voiture", "c_inv"].values[0]
    data_infra.loc[data_infra["Categories"] == "number_elec_charging_voiture", "c_maint_total"] += data_infra.at[idx[0], "[#]"] * data_infra.loc[data_infra["Categories"] == "number_elec_charging_voiture", "c_maint"].values[0]
    idx = data_infra.index[data_infra["Categories"] == "number_elec_charging_bus"]
    data_infra.at[idx[0], "[#]"] = math.ceil(data_infra.at[idx[0], "[#]"])    
    data_infra.loc[data_infra["Categories"] == "number_elec_charging_bus", "c_inv_annualised"] += data_infra.at[idx[0], "[#]"] * annualisation(data_infra["lifetime"]) * data_infra.loc[data_infra["Categories"] == "number_elec_charging_bus", "c_inv"].values[0]
    data_infra.loc[data_infra["Categories"] == "number_elec_charging_bus", "c_maint_total"] += data_infra.at[idx[0], "[#]"] * data_infra.loc[data_infra["Categories"] == "number_elec_charging_bus", "c_maint"].values[0]
    idx = data_infra.index[data_infra["Categories"] == "number_trainstation"]
    data_infra.at[idx[0], "[#]"] = math.ceil(data_infra.at[idx[0], "[#]"])
    data_infra.loc[data_infra["Categories"] == "number_trainstation", "c_inv_annualised"] += data_infra.at[idx[0], "[#]"] * annualisation(data_infra["lifetime"]) * data_infra.loc[data_infra["Categories"] == "number_trainstation", "c_inv"].values[0]
    data_infra.loc[data_infra["Categories"] == "number_trainstation", "c_maint_total"] += data_infra.at[idx[0], "[#]"] * data_infra.loc[data_infra["Categories"] == "number_trainstation", "c_maint"].values[0]

    active_road_inf_inv = data_infra.loc[data_infra["Categories"] == "km_active_road", "c_inv_annualised"].iloc[0] / 10**6
    active_road_inf_main = data_infra.loc[data_infra["Categories"] == "km_active_road", "c_maint_total"].iloc[0] / 10**6

    non_active_road_inf_inv = (
        data_infra.loc[data_infra["Categories"] == "km_non_active_road", "c_inv_annualised"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "number_fuelstation", "c_inv_annualised"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "number_elec_charging_voiture", "c_inv_annualised"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "number_elec_charging_bus", "c_inv_annualised"].iloc[0]
    ) / 10**6

    non_active_road_inf_main = (
        data_infra.loc[data_infra["Categories"] == "km_non_active_road", "c_maint_total"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "number_fuelstation", "c_maint_total"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "number_elec_charging_voiture", "c_maint_total"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "number_elec_charging_bus", "c_maint_total"].iloc[0]
    ) / 10**6
    railways_inf_inv = (data_infra.loc[data_infra["Categories"] == "km_tram", "c_inv_annualised"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "km_tram", "c_inv_annualised"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "km_metro", "c_inv_annualised"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "km_train", "c_inv_annualised"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "number_trainstation", "c_inv_annualised"].iloc[0]
    ) / 10**6

    railways_inf_main = (
        data_infra.loc[data_infra["Categories"] == "km_tram", "c_maint_total"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "km_metro", "c_maint_total"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "km_train", "c_maint_total"].iloc[0] +
        data_infra.loc[data_infra["Categories"] == "number_trainstation", "c_maint_total"].iloc[0]
    ) / 10**6
    
    #operational costs take into account the elec production and the gas costs
    #find the elec price /kWh
    list_name_elecprodcution = ['NUCLEAR','CCGT', 'CCGT_AMMONIA','COAL_US','COAL_IGCC','PV', 'WIND_ONSHORE', 'WIND_OFFSHORE', 'HYDRO_RIVER', 'GEOTHERMAL', 'IND_COGEN_GAS','IND_COGEN_WOOD','IND_COGEN_WASTE','DHN_COGEN_GAS','DHN_COGEN_WOOD','DHN_COGEN_WASTE','DHN_COGEN_WET_BIOMASS','DHN_COGEN_BIO_HYDROLYSIS','PHS', 'BATT_LI','ELEC_EXPORT','GRID_ELEC'] 
    list_costs = ['C_inv', 'C_maint', 'C_op']
    elec_total_price = 0
    elec_total_prod = 0

    for name in list_name_elecprodcution:
        for i in range(len(df)):
            if name in df.iloc[i, 0]:
                for cost in list_costs:
                    if cost in df.columns:
                        value = float(df.loc[i, cost])
                        value = round(value, 3) 
                        if value != 0:
                            if "COGEN" in name :
                                #prendre dans la liste de yearbalance ou dfbis la production d'lectricitié qui est dans la ligne IND_COGEN_GAS et colonne ELECTRICITY
                                elecprod = dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**3
                                heatprod = dfbis.loc[dfbis["Tech"] == name, "HEAT_HIGH_T"].iloc[0]*10**3
                                rendementelec = elecprod/(elecprod+heatprod)
                                #trouver dans la liste de yearbalance le nombre de production d'électricité et de chaleur la liste est dfbis et 
                                elec_total_price += value * rendementelec
                                #prendre ce qu'il y a après IND_COGEN_  de IND_COGEN_WOOD dcp wood et le print
                                #ouvrir un nouveau fichier de technologie 
                                if "IND_COGEN_GAS" in name and  "C_op" in cost:
                                    #add the gas price* the production consumption of gas
                                    elec_total_price +=  -dfbis.loc[dfbis["Tech"] == "IND_COGEN_GAS", "GAS"].iloc[0]*rendementelec*0.05329867
                                if "IND_COGEN_WOOD" in name and  "C_op" in cost:
                                    elec_total_price +=  -dfbis.loc[dfbis["Tech"] == "IND_COGEN_WOOD", "WOOD"].iloc[0]*rendementelec*0.03550648
                                if "IND_COGEN_WASTE" in name and  "C_op" in cost:
                                    elec_total_price +=  -dfbis.loc[dfbis["Tech"] == "IND_COGEN_WASTE", "WASTE"].iloc[0]*rendementelec*0.02497388
                                if "DHN_COGEN_GAS" in name and  "C_op" in cost:
                                    elec_total_price +=  -dfbis.loc[dfbis["Tech"] == "DHN_COGEN_GAS", "GAS"].iloc[0]*rendementelec*0.05329867
                                if "DHN_COGEN_WOOD" in name and  "C_op" in cost:
                                    elec_total_price +=  -dfbis.loc[dfbis["Tech"] == "DHN_COGEN_WOOD", "WOOD"].iloc[0]*rendementelec*0.03550648
                                if "DHN_COGEN_WASTE" in name and  "C_op" in cost:
                                    elec_total_price +=  -dfbis.loc[dfbis["Tech"] == "DHN_COGEN_WASTE", "WASTE"].iloc[0]*rendementelec*0.02497388
                                if "DHN_COGEN_WET_BIOMASS" in name and  "C_op" in cost:
                                    elec_total_price +=  -dfbis.loc[dfbis["Tech"] == "DHN_COGEN_WET_BIOMASS", "WET_BIOMASS"].iloc[0]*rendementelec*0.00622964
                                if "DHN_COGEN_BIO_HYDROLYSIS" in name and  "C_op" in cost:
                                    elec_total_price +=  -dfbis.loc[dfbis["Tech"] == "DHN_COGEN_BIO_HYDROLYSIS", "WET_BIOMASS"].iloc[0]*rendementelec*0.00622964
                            elif "CCGT" in name:
                                elec_total_price += value 
                                if "CCGT" == name and "C_op" == cost:
                                    elec_total_price += -dfbis.loc[dfbis["Tech"] == "CCGT", "GAS"].iloc[0]*0.05329867/2
                                if "CCGT_AMMONIA" == name and "C_op" == cost:
                                    elec_total_price += -dfbis.loc[dfbis["Tech"] == "CCGT_AMMONIA", "AMMONIA"].iloc[0]*0.11407418
                            elif "COAL" in name:
                                elec_total_price += value
                                if "COAL_US" == name and "C_op" == cost:
                                    elec_total_price += -dfbis.loc[dfbis["Tech"] == "COAL_US", "COAL"].iloc[0]*0.01814538
                                if "COAL_IGCC" == name and "C_op" == cost:
                                    elec_total_price += -dfbis.loc[dfbis["Tech"] == "COAL_IGCC", "COAL"].iloc[0]*0.01814538
                            elif "ELEC_EXPORT" in name:
                                elec_total_price += -dfbis.loc[dfbis["Tech"] == "ELEC_EXPORT", "ELECTRICITY"].iloc[0]*0.104928/3
                            else:
                                elec_total_price += value
                
    #take the all the electricity produce by them
    for name in list_name_elecprodcution:
        for i in range(len(dfbis)):
            if name in dfbis.iloc[i, 0]:
                if "CCGT" == name :
                    elec_total_prod += dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6/2
                else : 
                    elec_total_prod += dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6
    print(elec_total_prod)   
    elec_price_per_kwh = elec_total_price*10**6 / elec_total_prod + 0.104928
    gas_price_kwh = 0.05329867 
    diesel_price_kwh = 0.09105369
    gasoline_price_kwh = 0.09404786
    h2_price_kwh = 0.0955067
    print("price of electricity per kWh",elec_price_per_kwh)

    #prendre tt les données de la consommation energétique de la mobilité
    for name in list_name : 
        if "BIKE_NONELEC" in name:
            active_road_op += 0
        if "BIKE_ELEC" in name:
            active_road_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh
        if "MOTORCYCLE_GASOLINE" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "GASOLINE"].iloc[0] * 10**6 * gasoline_price_kwh
        if "MOTORCYCLE_BEV" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh
        if "CAR_GASOLINE" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "GASOLINE"].iloc[0] * 10**6 * gasoline_price_kwh
        if "CAR_DIESEL" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "DIESEL"].iloc[0] * 10**6 * diesel_price_kwh
        if "CAR_HEV" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh
        if "CAR_PHEV" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh
        if "CAR_BEV" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh
        if "CAR_FC" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "H2"].iloc[0] * 10**6 * h2_price_kwh
        if "CAR_NG" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "GAS"].iloc[0] * 10**6 * gas_price_kwh
        if "BUS_DIESEL" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "DIESEL"].iloc[0] * 10**6 * diesel_price_kwh
            cout_public_op += -dfbis.loc[dfbis["Tech"] == name, "DIESEL"].iloc[0] * 10**6 * diesel_price_kwh/10**6
            cout_prive_op -= -dfbis.loc[dfbis["Tech"] == name, "DIESEL"].iloc[0] * 10**6 * diesel_price_kwh/10**6
        if "BUS_HYDIESEL" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "DIESEL"].iloc[0] * 10**6 * diesel_price_kwh
            cout_public_op += -dfbis.loc[dfbis["Tech"] == name, "DIESEL"].iloc[0] * 10**6 * diesel_price_kwh/10**6
            cout_prive_op -= -dfbis.loc[dfbis["Tech"] == name, "DIESEL"].iloc[0] * 10**6 * diesel_price_kwh/10**6
        if "BUS_ELEC" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh
            cout_public_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh/10**6
            cout_prive_op -= -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh/10**6
        if "BUS_FC" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "H2"].iloc[0] * 10**6 * h2_price_kwh
            cout_public_op += -dfbis.loc[dfbis["Tech"] == name, "H2"].iloc[0] * 10**6 * h2_price_kwh/10**6
            cout_prive_op -= -dfbis.loc[dfbis["Tech"] == name, "H2"].iloc[0] * 10**6 * h2_price_kwh/10**6
        if "BUS_NG" in name:
            non_active_road_op += -dfbis.loc[dfbis["Tech"] == name, "GAS"].iloc[0] * 10**6 * gas_price_kwh
            cout_public_op += -dfbis.loc[dfbis["Tech"] == name, "GAS"].iloc[0] * 10**6 * gas_price_kwh/10**6
            cout_prive_op -= -dfbis.loc[dfbis["Tech"] == name, "GAS"].iloc[0] * 10**6 * gas_price_kwh/10**6
        if "TRAMWAY_ELEC" in name:
            railways_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh
        if "METRO_ELEC" in name:
            railways_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh
        if "TRAIN_ELEC" in name:
            railways_op += -dfbis.loc[dfbis["Tech"] == name, "ELECTRICITY"].iloc[0] * 10**6 * elec_price_per_kwh
    
    if active_road_op < 1 :
        active_road_op = 0
    if non_active_road_op < 1 :
        non_active_road_op = 0
    if railways_op < 1 :
        railways_op = 0
    active_road_op = active_road_op / 10**6
    non_active_road_op = non_active_road_op / 10**6
    railways_op = railways_op / 10**6
    
    #créer un tableau avec les valeurs et les prints
    list_costs.append("Total")
    #ajout au début de la liste category
    list_costs.insert(0, "Category")
    table = [
        ['Category'] + ['C_veh_inv [M€]'] + ['C_veh_maint [M€]'] + ['C_veh_op [M€]'] + ['C_infra_inv [M€]'] + ['C_infra_maint [M€]'] + ['Total [M€]'],
        ["Active Road"] + [active_road_inv] + [active_road_main] + [active_road_op]+ [active_road_inf_inv] + [active_road_inf_main]  + [active_road_inv + active_road_main + active_road_op + active_road_inf_inv + active_road_inf_main],
        ["Non-Active Road"] + [non_active_road_inv] + [non_active_road_main] + [non_active_road_op]+ [non_active_road_inf_inv] + [non_active_road_inf_main]  + [non_active_road_inv + non_active_road_main + non_active_road_op+ non_active_road_inf_inv + non_active_road_inf_main],
        ["Railways"] + [railways_inv] + [railways_main] + [railways_op] + [railways_inf_inv] + [railways_inf_main] + [railways_inv + railways_main + railways_inf_inv + railways_inf_main],
        ["Total"] + [non_active_road_inv + active_road_inv + railways_inv] + [non_active_road_main + active_road_main + railways_main] + [non_active_road_op + active_road_op + railways_op] + [non_active_road_inf_inv + active_road_inf_inv + railways_inf_inv]+ [non_active_road_inf_main + active_road_inf_main + railways_inf_main]+[non_active_road_inv + active_road_inv + railways_inv + non_active_road_main + active_road_main + railways_main + non_active_road_op + active_road_op + railways_op + non_active_road_inf_inv + active_road_inf_inv + railways_inf_inv + non_active_road_inf_main + active_road_inf_main + railways_inf_main]
    ]
    print(tabulate.tabulate(table, headers="firstrow", tablefmt="fancy_GRID_ELEC"))
    #prendre tout les coûts C_inv et C_main et C_op
    total_cost = 0
    for i in range(len(df)):
        for cost in list_costs:
            if cost in df.columns:
                value = float(df.loc[i, cost])
                total_cost += value
    print("Total cost of the energetical system [B€/year]:", total_cost/10**3)
    print("Percent of total cost", round(table[-1][-1]/total_cost,2)*100," %")
    
    # Données
    categories = ["Active Road", "Non-Active Road", "Railways", "Total"]
    cost_components = ["C_veh_inv", "C_veh_maint", "C_veh_op", "C_infra_inv", "C_infra_maint", "Total"]

    # Valeurs des coûts (remplace avec tes variables réelles)
    data = np.array([
        [active_road_inv, active_road_main, active_road_op, active_road_inf_inv, active_road_inf_main, 
        active_road_inv + active_road_main + active_road_op + active_road_inf_inv + active_road_inf_main],
        [non_active_road_inv, non_active_road_main, non_active_road_op, non_active_road_inf_inv, non_active_road_inf_main, 
        non_active_road_inv + non_active_road_main + non_active_road_op + non_active_road_inf_inv + non_active_road_inf_main],
        [railways_inv, railways_main, railways_op, railways_inf_inv, railways_inf_main, 
        railways_inv + railways_main + railways_op + railways_inf_inv + railways_inf_main],
        [
            non_active_road_inv + active_road_inv + railways_inv,
            non_active_road_main + active_road_main + railways_main,
            non_active_road_op + active_road_op + railways_op,
            non_active_road_inf_inv + active_road_inf_inv + railways_inf_inv,
            non_active_road_inf_main + active_road_inf_main + railways_inf_main,
            non_active_road_inv + active_road_inv + railways_inv +
            non_active_road_main + active_road_main + railways_main +
            non_active_road_op + active_road_op + railways_op +
            non_active_road_inf_inv + active_road_inf_inv + railways_inf_inv +
            non_active_road_inf_main + active_road_inf_main + railways_inf_main
        ]
    ])
    #diviser le data par 10**3
    data = data/10**3

    # Paramètres du graphique
    x = np.arange(len(categories))
    width = 0.12
    colors = ["blue", "orange", "green", "red", "purple", "brown"]

    fig, ax = plt.subplots(figsize=(12, 6))

    # Tracer les barres
    for i, (cost, color) in enumerate(zip(cost_components, colors)):
        ax.bar(x + (i - 2.5) * width, data[:, i], width, label=cost, color=color)

    #mettre des hbar tous les 500
    ax.set_yticks(np.arange(0, 27.5, 2.5))
    #mettre une ligne horizontale au même endroit que le yticks
    for i in np.arange(0, 27.5, 2.5):
        plt.axhline(y=i, color='grey', linestyle='--', linewidth=0.5)

    

    # Labels et mise en forme
    ax.set_ylabel("Cost [B€/year]", fontsize=14)
    ax.set_title("Cost Distribution type of mobility", fontsize=18)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=14)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=6, fontsize=12, frameon=False)

    # Ajustements de style
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", labelsize=14)
    plt.show()

    #plot cout prive vs cout public
    cout_prive_inv += active_road_inv + non_active_road_inv
    cout_prive_main += active_road_main + non_active_road_main
    cout_prive_op += active_road_op + non_active_road_op
    cout_public_inv += railways_inv
    cout_public_main += railways_main
    cout_public_op += railways_op
    #créer un graphe bar stackplot
    # Données
    categories = ["Private", "Public"]
    cost_components = ["C_veh_inv", "C_veh_maint", "C_veh_op", "C_infra_inv", "C_infra_maint"]
    data = np.array([
        [cout_prive_inv, cout_prive_main, cout_prive_op, 0, 0],
        [cout_public_inv, cout_public_main, cout_public_op, non_active_road_inf_inv + active_road_inf_inv + railways_inf_inv, non_active_road_inf_main + active_road_inf_main + railways_inf_main]
    ])
    #diviser le data par 10**3
    data = data/10**3

    #make the percent
    cout_prive = cout_prive_inv + cout_prive_main + cout_prive_op
    cout_public = cout_public_inv + cout_public_main + cout_public_op + non_active_road_inf_inv + active_road_inf_inv + railways_inf_inv + non_active_road_inf_main + active_road_inf_main + railways_inf_main
    cout_prive_percent = cout_prive / (cout_prive + cout_public) * 100
    cout_public_percent = cout_public / (cout_prive + cout_public) * 100

    # Paramètres du graphique
    x = np.arange(len(categories))
    width = 0.25

    fig, ax = plt.subplots(figsize=(12, 6))

    # Tracer les barres de type stack plot et le pourcentage
    for i, (cost, color) in enumerate(zip(cost_components, colors)):
        ax.bar(x, data[:, i], width, label=cost, color=color, bottom=np.sum(data[:, :i], axis=1))

    #mettre des lignes horizontales tous les 2.5
    ax.set_yticks(np.arange(0, 17.5, 2.5))
    for i in np.arange(0, 17.5, 2.5):
        plt.axhline(y=i, color='grey', linestyle='--', linewidth        =0.5)

    # Labels et mise en forme
    ax.set_ylabel("Cost [B€/year]", fontsize=14)
    ax.set_title("Cost Distribution type of mobility", fontsize=18)
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=14)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.25), ncol=6, fontsize=14, frameon=False)

    # Labels et mise en forme
    total_costs = np.sum(data, axis=1)
    for i, total in enumerate(total_costs):
        ax.text(i, total + 0.5, f"{total/sum(total_costs)*100:.1f} %", ha='center', fontsize=14)
    # Ajustements de style
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", labelsize=14)
    plt.show()
if consumptionperarea :
    #take the data year_balance.txt
    filename = "year_balance.txt"

    #open the file in a dataframe
    data = np.genfromtxt(os.path.join(path, filename), delimiter="\t", skip_header=0, dtype=None, encoding=None)

    df = pd.read_csv(os.path.join(path, filename), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    
    #plot the data if the first of the row is a specific name in a list and isELECTRICITY	GASOLINE	DIESEL	LFO	GAS H2
    #list of the names we want to plot


    # Liste des énergies et noms
    list_name = [
        "BIKE_NONELEC_URBAN",
        "BIKE_ELEC_URBAN",
        "MOTORCYCLE_GASOLINE_URBAN",
        "MOTORCYCLE_BEV_URBAN",
        "CAR_GASOLINE_URBAN",
        "CAR_DIESEL_URBAN",
        "CAR_HEV_URBAN",
        "CAR_PHEV_URBAN",
        "CAR_BEV_URBAN",
        "CAR_FC_URBAN",
        "CAR_NG_URBAN",
        "BUS_DIESEL_URBAN",
        "BUS_HYDIESEL_URBAN",
        "BUS_ELEC_URBAN",
        "BUS_FC_URBAN",
        "BUS_NG_URBAN",
        "TRAMWAY_ELEC_URBAN",
        "METRO_ELEC_URBAN",
        "BIKE_NONELEC_RURAL",
        "BIKE_ELEC_RURAL",
        "MOTORCYCLE_GASOLINE_RURAL",
        "MOTORCYCLE_BEV_RURAL",
        "CAR_GASOLINE_RURAL",
        "CAR_DIESEL_RURAL",
        "CAR_HEV_RURAL",
        "CAR_PHEV_RURAL",
        "CAR_BEV_RURAL",
        "CAR_FC_RURAL",
        "CAR_NG_RURAL",
        "BUS_DIESEL_RURAL",
        "BUS_HYDIESEL_RURAL",
        "BUS_ELEC_RURAL",
        "BUS_FC_RURAL",
        "BUS_NG_RURAL",
        "TRAIN_ELEC_RURAL"
    ]
    list_energy = ['ELECTRICITY', 'GASOLINE', 'DIESEL', 'GAS', 'H2']

    sum_active_rural = np.zeros(len(list_energy) +1 )
    sum_nonactive_rural = np.zeros(len(list_energy) +1 )
    sum_public_rural = np.zeros(len(list_energy) +1 )
    sum_active_urban = np.zeros(len(list_energy) +1 )
    sum_nonactive_urban = np.zeros(len(list_energy) +1 )
    sum_public_urban = np.zeros(len(list_energy) +1 )


    plt.figure(figsize=(12, 6), layout="constrained")

    # Boucle sur les noms à chercher
    for name in list_name:
        for i in range(len(df)):
            if name in df.iloc[i, 0]:  # Vérifie si le nom est dans la première colonne
                # Parcours des énergies
                sum = 0
                for energy in list_energy:
                    if energy in df.columns:  # Vérifie si l'énergie est bien une colonne
                        value = float(df.loc[i, energy]) / 10**3  # Convertir en TWh
                        value = round(value, 3)
                        if value != 0:
                            # Attribution des valeurs aux bonnes catégories
                            if "BIKE" in name and "RURAL" in name:
                                sum_active_rural[sum] -= value
                                sum_active_rural[-1] -=value
                            if "BIKE" in name and "URBAN" in name:
                                sum_active_urban[sum] -= value
                                sum_active_urban[-1] -= value
                            if "MOTORCYCLE" in name and "RURAL" in name:
                                sum_nonactive_rural[sum] -= value
                                sum_nonactive_rural[-1] -= value
                            if "MOTORCYCLE" in name and "URBAN" in name:
                                sum_nonactive_urban[sum] -= value
                                sum_nonactive_urban[-1] -= value
                            if "CAR" in name and "RURAL" in name:
                                sum_nonactive_rural[sum] -= value
                                sum_nonactive_rural[-1] -= value
                            if "CAR" in name and "URBAN" in name:
                                sum_nonactive_urban[sum] -= value
                                sum_nonactive_urban[-1] -= value
                            if "BUS" in name and "URBAN" in name:
                                sum_public_urban[sum] -= value
                                sum_public_urban[-1] -= value
                            if "BUS" in name and "RURAL" in name:
                                sum_public_rural[sum] -= value
                                sum_public_rural[-1] -= value
                            if "METRO" in name:
                                sum_public_urban[sum] -= value
                                sum_public_urban[-1] -= value
                            if "TRAM" in name:
                                sum_public_urban[sum] -= value
                                sum_public_urban[-1] -= value
                            if "TRAIN_ELEC_RURAL" in name:
                                sum_public_rural[sum] -= value
                                sum_public_rural[-1] -= value
                    sum += 1
    list_energy.append("Total")
    #ajout au début de la liste category
    list_energy.insert(0, "Category")
    table = [
        list_energy,
        ["Active Rural"] + list(sum_active_rural),
        ["Non-Active Rural"] + list(sum_nonactive_rural),
        ["Public Rural"] + list(sum_public_rural),
        ["Active Urban"] + list(sum_active_urban),
        ["Non-Active Urban"] + list(sum_nonactive_urban),
        ["Public Urban"] + list(sum_public_urban)
    ]
    print(tabulate.tabulate(table, headers="firstrow", tablefmt="fancy_GRID_ELEC"))

    # Données (exemple basé sur l'image)
    scenarios = ["URBAN", "RURAL", "TOTAL"]
    #en se basant de table
    electricity = [sum_active_urban[0] + sum_nonactive_urban[0] + sum_public_urban[0], sum_active_rural[0] + sum_nonactive_rural[0] + sum_public_rural[0], sum_active_urban[0] + sum_nonactive_urban[0] + sum_public_urban[0] + sum_active_rural[0] + sum_nonactive_rural[0] + sum_public_rural[0]]
    gasoline = [sum_active_urban[1] + sum_nonactive_urban[1] + sum_public_urban[1], sum_active_rural[1] + sum_nonactive_rural[1] + sum_public_rural[1], sum_active_urban[1] + sum_nonactive_urban[1] + sum_public_urban[1] + sum_active_rural[1] + sum_nonactive_rural[1] + sum_public_rural[1]]
    diesel = [sum_active_urban[2] + sum_nonactive_urban[2] + sum_public_urban[2], sum_active_rural[2] + sum_nonactive_rural[2] + sum_public_rural[2], sum_active_urban[2] + sum_nonactive_urban[2] + sum_public_urban[2] + sum_active_rural[2] + sum_nonactive_rural[2] + sum_public_rural[2]]
    gas = [sum_active_urban[3] + sum_nonactive_urban[3] + sum_public_urban[3], sum_active_rural[3] + sum_nonactive_rural[3] + sum_public_rural[3], sum_active_urban[3] + sum_nonactive_urban[3] + sum_public_urban[3] + sum_active_rural[3] + sum_nonactive_rural[3] + sum_public_rural[3]]
    hydrogen = [sum_active_urban[4] + sum_nonactive_urban[4] + sum_public_urban[4], sum_active_rural[4] + sum_nonactive_rural[4] + sum_public_rural[4], sum_active_urban[4] + sum_nonactive_urban[4] + sum_public_urban[4] + sum_active_rural[4] + sum_nonactive_rural[4] + sum_public_rural[4]]
    total = [sum_active_urban[-1] + sum_nonactive_urban[-1] + sum_public_urban[-1], sum_active_rural[-1] + sum_nonactive_rural[-1] + sum_public_rural[-1], sum_active_urban[-1] + sum_nonactive_urban[-1] + sum_public_urban[-1] + sum_active_rural[-1] + sum_nonactive_rural[-1] + sum_public_rural[-1]]

    # Bar width and x positions
    x = np.arange(len(scenarios))
    width = 0.08  # Reduced width to fit 6 bars

    # Create the figure and axis
    fig, ax = plt.subplots(figsize=(12, 6))

    # Plot bars with specific colors
    ax.bar(x - 2*width, electricity, width, label="Electricity", color=elec_color)  # Blue
    ax.bar(x - width, gasoline, width-0.01, label="Gasoline", color=gasoline_color)     # Orange
    ax.bar(x, diesel, width-0.01, label="Diesel", color= diesel_color)                 # Green
    ax.bar(x + width, gas, width-0.01, label="Natural Gas", color= gas_color)       # Red
    ax.bar(x + 2*width, hydrogen, width-0.01, label="Hydrogen", color= h2_color)   # Purple
    ax.bar(x + 3*width, total, width-0.01, label="Total", color= total_color)         # Brown


    # Labels and title
    ax.set_ylabel("Final energy consumption [TWh]", fontsize=14)
    ax.set_title("Final energy consumption in the transport sector", fontsize=18)
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios, fontsize=14)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=6, fontsize=14, frameon=False)

    #ajouter des lignes horizontaux tous les 10
    for i in range(0, 35, 5):
        plt.axhline(i, color="black", linewidth=0.5, linestyle="--")
    # Style adjustments
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", labelsize=14)  # Set y-axis label size

    plt.show()

    #créer un graphe qui regarde la taille de stockage,la construction en MW des renouvlables et non renouvlables
    #df_cost vient du fichier cost_breakdown
    df_cost = pd.read_csv(os.path.join(path, "cost_breakdown.txt"), sep=",", engine="python")
    df_gwp = pd.read_csv(os.path.join(path, "gwp_breakdown.txt"), sep=",", engine="python")

    list_storage = []
    #pour les énergie renouvable et non renouvelable divisé par le c_inv
    #pour le PHS et lithium batterie diviser par gwp_inv
if fleetsize :
    #take the data year_balance.txt
    filename = "year_balance.txt"

    #open the file in a dataframe
    data = np.genfromtxt(os.path.join(path, filename), delimiter="\t", skip_header=0, dtype=None, encoding=None)

    df = pd.read_csv(os.path.join(path, filename), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    
    #plot the data if the first of the row is a specific name in a list and isELECTRICITY	GASOLINE	DIESEL	LFO	GAS H2
    #list of the names we want to plot

    # Liste des énergies et noms
    list_name = [
        "BIKE_NONELEC_URBAN",
        "BIKE_ELEC_URBAN",
        "MOTORCYCLE_GASOLINE_URBAN",
        "MOTORCYCLE_BEV_URBAN",
        "CAR_GASOLINE_URBAN",
        "CAR_DIESEL_URBAN",
        "CAR_HEV_URBAN",
        "CAR_PHEV_URBAN",
        "CAR_BEV_URBAN",
        "CAR_FC_URBAN",
        "CAR_NG_URBAN",
        "BUS_DIESEL_URBAN",
        "BUS_HYDIESEL_URBAN",
        "BUS_ELEC_URBAN",
        "BUS_FC_URBAN",
        "BUS_NG_URBAN",
        "TRAMWAY_ELEC_URBAN",
        "METRO_ELEC_URBAN",
        "BIKE_NONELEC_RURAL",
        "BIKE_ELEC_RURAL",
        "MOTORCYCLE_GASOLINE_RURAL",
        "MOTORCYCLE_BEV_RURAL",
        "CAR_GASOLINE_RURAL",
        "CAR_DIESEL_RURAL",
        "CAR_HEV_RURAL",
        "CAR_PHEV_RURAL",
        "CAR_BEV_RURAL",
        "CAR_FC_RURAL",
        "CAR_NG_RURAL",
        "BUS_DIESEL_RURAL",
        "BUS_HYDIESEL_RURAL",
        "BUS_ELEC_RURAL",
        "BUS_FC_RURAL",
        "BUS_NG_RURAL",
        "TRAIN_ELEC_RURAL"
    ]
    list_mobility = ['MOB_PUBLIC_URBAN', 'MOB_PRIVATE_NA_URBAN','MOB_PRIVATE_A_URBAN','MOB_PUBLIC_RURAL','MOB_PRIVATE_NA_RURAL','MOB_PRIVATE_A_RURAL']

    BUS_DIESEL_URBAN = 0
    BUS_HYDIESEL_URBAN = 0
    BUS_ELEC_URBAN = 0
    BUS_FC_URBAN = 0
    BUS_NG_URBAN = 0
    TRAMWAY_ELEC_URBAN= 0 
    METRO_ELEC_URBAN = 0
    W2_GASOLINE_URBAN = 0
    W2_BEV_URBAN = 0
    CAR_GASOLINE_URBAN= 0 
    CAR_DIESEL_URBAN = 0
    CAR_HEV_URBAN = 0
    CAR_PHEV_URBAN = 0
    CAR_BEV_URBAN = 0
    CAR_FC_URBAN = 0
    CAR_NG_URBAN = 0
    BIKE_NONELEC_URBAN = 0
    BIKE_ELEC_URBAN = 0
    BUS_DIESEL_RURAL = 0
    BUS_HYDIESEL_RURAL = 0
    BUS_ELEC_RURAL = 0
    BUS_FC_RURAL = 0
    BUS_NG_RURAL = 0
    TRAIN_ELEC_RURAL = 0
    W2_GASOLINE_RURAL = 0
    W2_BEV_RURAL = 0
    CAR_GASOLINE_RURAL = 0 
    CAR_DIESEL_RURAL = 0
    CAR_HEV_RURAL = 0
    CAR_PHEV_RURAL = 0
    CAR_BEV_RURAL = 0
    CAR_FC_RURAL = 0
    CAR_NG_RURAL = 0
    BIKE_NONELEC_RURAL = 0 
    BIKE_ELEC_RURAL = 0
    occupancycar = 1.24
    occupancybus = 14.86
    occupancytram = 55
    occupancymetro = 116
    occupancytrain = 178

    #if scenario1 dans le folder :
    if "scenario1" in path:
        occupancycar *=1
        occupancybus *=1
        occupancytram *=1
        occupancymetro *=1
        occupancytrain *=1
        print("it is working")
    if "scenario2" in path:
        occupancycar = 2.0
        occupancybus *=1.2
        occupancytram *=1.2
        occupancymetro *=1.2
        occupancytrain *=1.2
        print("it is working")
    
    if "scenario3" in path:
        occupancycar = 1.8
        occupancybus *=1
        occupancytram *=1
        occupancymetro *=1
        occupancytrain *=1
        print("it is working")
    Bike_NONELEC = np.array([1, 3120])
    Bike_BEV = np.array([1, 3120])
    MOTORCYCLE_Petrol = np.array([1, 1790])
    MOTORCYCLE_BEV = np.array([1, 1790])
    Car_Petrol = np.array([occupancycar, 15000])
    Car_HEV = np.array([occupancycar, 15000])
    Car_PHEV = np.array([occupancycar, 15000])
    Car_Diesel = np.array([occupancycar, 15000])
    Car_BEV = np.array([occupancycar, 15000])
    Car_FC = np.array([occupancycar, 15000])
    Car_NG = np.array([occupancycar, 15000])
    Bus_Diesel = np.array([occupancybus, 40000])
    Bus_HEV = np.array([occupancybus, 40000])
    Bus_BEV = np.array([occupancybus, 40000])
    Bus_FC = np.array([occupancybus, 40000])
    Bus_NG = np.array([occupancybus, 40000])
    Tram_BEV = np.array([occupancytram, 39463])
    Metro_BEV = np.array([occupancymetro, 69328])
    Train_BEV = np.array([occupancytrain, 273890])

    

    # Boucle sur les noms à chercher
    for name in list_name:
        for i in range(len(df)):
            if name in df.iloc[i, 0]:
                # Parcours des énergies
                for mobility in list_mobility:
                    if mobility in df.columns:
                        value = float(df.loc[i, mobility])
                        value = round(value, 3)
                        if value >= 1:
                            value = value * 10**6
                            if "BIKE_NONELEC_RURAL" in name:
                                BIKE_NONELEC_RURAL += value/(Bike_NONELEC[0]*Bike_NONELEC[1])
                                print((Bike_NONELEC[0]*Bike_NONELEC[1]))
                            if "BIKE_ELEC_RURAL" in name:
                                BIKE_ELEC_RURAL += value/(Bike_BEV[0]*Bike_BEV[1])
                            if "MOTORCYCLE_GASOLINE_RURAL" in name:
                                W2_GASOLINE_RURAL += value/(MOTORCYCLE_Petrol[0]*MOTORCYCLE_Petrol[1])
                            if "MOTORCYCLE_BEV_RURAL" in name:
                                W2_BEV_RURAL += value/(MOTORCYCLE_BEV[0]*MOTORCYCLE_BEV[1])
                            if "CAR_GASOLINE_RURAL" in name:
                                CAR_GASOLINE_RURAL += value/(Car_Petrol[0]*Car_Petrol[1])
                            if "CAR_DIESEL_RURAL" in name:
                                CAR_DIESEL_RURAL += value/(Car_Diesel[0]*Car_Diesel[1])
                            if "CAR_HEV_RURAL" in name:
                                CAR_HEV_RURAL += value/(Car_HEV[0]*Car_HEV[1])
                            if "CAR_PHEV_RURAL" in name:
                                CAR_PHEV_RURAL += value/(Car_PHEV[0]*Car_PHEV[1])
                            if "CAR_BEV_RURAL" in name:
                                CAR_BEV_RURAL += value/(Car_BEV[0]*Car_BEV[1])
                            if "CAR_FC_RURAL" in name:
                                CAR_FC_RURAL += value/(Car_FC[0]*Car_FC[1])
                            if "CAR_NG_RURAL" in name:
                                CAR_NG_RURAL += value/(Car_NG[0]*Car_NG[1])
                            if "BUS_DIESEL_RURAL" in name:
                                BUS_DIESEL_RURAL += value/(Bus_Diesel[0]*Bus_Diesel[1])
                            if "BUS_HYDIESEL_RURAL" in name:
                                BUS_HYDIESEL_RURAL += value/(Bus_HEV[0]*Bus_HEV[1])
                            if "BUS_ELEC_RURAL" in name:
                                BUS_ELEC_RURAL += value/(Bus_BEV[0]*Bus_BEV[1])
                            if "BUS_FC_RURAL" in name:
                                BUS_FC_RURAL += value/(Bus_FC[0]*Bus_FC[1])
                            if "BUS_NG_RURAL" in name:
                                BUS_NG_RURAL += value/(Bus_NG[0]*Bus_NG[1])
                            if "TRAIN_ELEC_RURAL" in name:
                                TRAIN_ELEC_RURAL += value/(Train_BEV[0]*Train_BEV[1])
                            if "BIKE_NONELEC_URBAN" in name:
                                BIKE_NONELEC_URBAN += value/(Bike_NONELEC[0]*Bike_NONELEC[1])
                            if "BIKE_ELEC_URBAN" in name:
                                BIKE_ELEC_URBAN += value/(Bike_BEV[0]*Bike_BEV[1])
                            if "MOTORCYCLE_GASOLINE_URBAN" in name:
                                W2_GASOLINE_URBAN += value/(MOTORCYCLE_Petrol[0]*MOTORCYCLE_Petrol[1])
                            if "MOTORCYCLE_BEV_URBAN" in name:
                                W2_BEV_URBAN += value/(MOTORCYCLE_BEV[0]*MOTORCYCLE_BEV[1])
                            if "CAR_GASOLINE_URBAN" in name:
                                CAR_GASOLINE_URBAN += value/(Car_Petrol[0]*Car_Petrol[1])
                            if "CAR_DIESEL_URBAN" in name:
                                CAR_DIESEL_URBAN += value/(Car_Diesel[0]*Car_Diesel[1])
                            if "CAR_HEV_URBAN" in name:
                                CAR_HEV_URBAN += value/(Car_HEV[0]*Car_HEV[1])
                            if "CAR_PHEV_URBAN" in name:
                                CAR_PHEV_URBAN += value/(Car_PHEV[0]*Car_PHEV[1])
                            if "CAR_BEV_URBAN" in name:
                                CAR_BEV_URBAN += value/(Car_BEV[0]*Car_BEV[1])
                            if "CAR_FC_URBAN" in name:
                                CAR_FC_URBAN += value/(Car_FC[0]*Car_FC[1])
                            if "CAR_NG_URBAN" in name:
                                CAR_NG_URBAN += value/(Car_NG[0]*Car_NG[1])
                            if "BUS_DIESEL_URBAN" in name:
                                BUS_DIESEL_URBAN += value/(Bus_Diesel[0]*Bus_Diesel[1])
                            if "BUS_HYDIESEL_URBAN" in name:
                                BUS_HYDIESEL_URBAN += value/(Bus_HEV[0]*Bus_HEV[1])
                            if "BUS_ELEC_URBAN" in name:
                                BUS_ELEC_URBAN += value/(Bus_BEV[0]*Bus_BEV[1])
                            if "BUS_FC_URBAN" in name:
                                BUS_FC_URBAN += value/(Bus_FC[0]*Bus_FC[1])
                            if "BUS_NG_URBAN" in name:
                                BUS_NG_URBAN += value/(Bus_NG[0]*Bus_NG[1])
                            if "TRAMWAY_ELEC_URBAN" in name:
                                TRAMWAY_ELEC_URBAN += value/(Tram_BEV[0]*Tram_BEV[1])
                            if "METRO_ELEC_URBAN" in name:
                                METRO_ELEC_URBAN += value/(Metro_BEV[0]*Metro_BEV[1])

    #faire un tableau et le plot
    list_mobility.append("Total")
    #ajout au début de la liste category
    list_mobility.insert(0, "Category")
    table = [
    list_mobility,
    ["BIKE_NONELEC"] + [BIKE_NONELEC_URBAN] + [BIKE_NONELEC_RURAL] + [BIKE_NONELEC_URBAN + BIKE_NONELEC_RURAL],
    ["BIKE_ELEC"] + [BIKE_ELEC_URBAN] + [BIKE_ELEC_RURAL] + [BIKE_ELEC_URBAN + BIKE_ELEC_RURAL],
    ["W2_GASOLINE"] + [W2_GASOLINE_URBAN] + [W2_GASOLINE_RURAL] + [W2_GASOLINE_URBAN + W2_GASOLINE_RURAL],
    ["W2_BEV"] + [W2_BEV_URBAN] + [W2_BEV_RURAL] + [W2_BEV_URBAN + W2_BEV_RURAL],
    ["CAR_GASOLINE"] + [CAR_GASOLINE_URBAN] + [CAR_GASOLINE_RURAL] + [CAR_GASOLINE_URBAN + CAR_GASOLINE_RURAL],
    ["CAR_DIESEL"] + [CAR_DIESEL_URBAN] + [CAR_DIESEL_RURAL] + [CAR_DIESEL_URBAN + CAR_DIESEL_RURAL],
    ["CAR_HEV"] + [CAR_HEV_URBAN] + [CAR_HEV_RURAL] + [CAR_HEV_URBAN + CAR_HEV_RURAL],
    ["CAR_PHEV"] + [CAR_PHEV_URBAN] + [CAR_PHEV_RURAL] + [CAR_PHEV_URBAN + CAR_PHEV_RURAL],
    ["CAR_BEV"] + [CAR_BEV_URBAN] + [CAR_BEV_RURAL] + [CAR_BEV_URBAN + CAR_BEV_RURAL],
    ["CAR_FC"] + [CAR_FC_URBAN] + [CAR_FC_RURAL] + [CAR_FC_URBAN + CAR_FC_RURAL],
    ["CAR_NG"] + [CAR_NG_URBAN] + [CAR_NG_RURAL] + [CAR_NG_URBAN + CAR_NG_RURAL],
    ["BUS_DIESEL"] + [BUS_DIESEL_URBAN] + [BUS_DIESEL_RURAL] + [BUS_DIESEL_URBAN + BUS_DIESEL_RURAL],
    ["BUS_HYDIESEL"] + [BUS_HYDIESEL_URBAN] + [BUS_HYDIESEL_RURAL] + [BUS_HYDIESEL_URBAN + BUS_HYDIESEL_RURAL],
    ["BUS_ELEC"] + [BUS_ELEC_URBAN] + [BUS_ELEC_RURAL] + [BUS_ELEC_URBAN + BUS_ELEC_RURAL],
    ["BUS_FC"] + [BUS_FC_URBAN] + [BUS_FC_RURAL] + [BUS_FC_URBAN + BUS_FC_RURAL],
    ["BUS_NG"] + [BUS_NG_URBAN] + [BUS_NG_RURAL] + [BUS_NG_URBAN + BUS_NG_RURAL],
    ["TRAMWAY_ELEC"] + [TRAMWAY_ELEC_URBAN] + [0] + [TRAMWAY_ELEC_URBAN],
    ["METRO_ELEC"] + [METRO_ELEC_URBAN] + [0] + [METRO_ELEC_URBAN],
    ["TRAIN_ELEC"] + [0] + [TRAIN_ELEC_RURAL] + [TRAIN_ELEC_RURAL],
]

    print(tabulate.tabulate(table, headers="firstrow", tablefmt="fancy_GRID_ELEC"))

    categories = ["Urban", "Rural", "Total"]
    factorofdivision = 10**6
    values_NONELEC = np.array([BIKE_NONELEC_URBAN, BIKE_NONELEC_RURAL, BIKE_NONELEC_URBAN + BIKE_NONELEC_RURAL])/factorofdivision
    values_elec = np.array([BIKE_ELEC_URBAN, BIKE_ELEC_RURAL, BIKE_ELEC_URBAN + BIKE_ELEC_RURAL])/factorofdivision
    values_total = np.array([BIKE_NONELEC_URBAN + BIKE_ELEC_URBAN, BIKE_NONELEC_RURAL + BIKE_ELEC_RURAL, BIKE_NONELEC_URBAN + BIKE_ELEC_URBAN + BIKE_NONELEC_RURAL + BIKE_ELEC_RURAL])/factorofdivision

    # Paramètres pour décaler les barres
    x = np.arange(len(categories))  # Position des catégories
    width = 0.08  # Largeur des barres

    # Création de la figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Ajout des barres avec un décalage
    ax.bar(x - 1.5 * width, values_NONELEC, width -0.01, label="Non-electric Bike", color=NONELEC_color)
    ax.bar(x, values_elec, width -0.01, label="Electric Bike", color=elec_color)
    ax.bar(x + 1.5 * width, values_total, width -0.01, label="Total", color=total_color)

    # Configuration des axes
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=14)
    ax.set_ylabel("Number of vehicles [M#]", fontsize=14)
    ax.set_title("Number of bikes", fontsize=18)

    # Ajouter des lignes horizontales tous les 5 unités
    for i in range(0, 6, 1):
        ax.axhline(i, color="black", linewidth=0.5, linestyle="--", alpha=0.7)

    # Ajout de la légende
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=3, fontsize=14, frameon=False)

    # Suppression des bordures inutiles
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", labelsize=14)

    # Affichage
    plt.show()

    #do the same for the W2
    categories = ["Urban", "Rural", "Total"]
    factorofdivision = 1
    values_gasoline = np.array([W2_GASOLINE_URBAN, W2_GASOLINE_RURAL, W2_GASOLINE_URBAN + W2_GASOLINE_RURAL])/factorofdivision
    values_elec = np.array([W2_BEV_URBAN, W2_BEV_RURAL, W2_BEV_URBAN + W2_BEV_RURAL])/factorofdivision
    values_total = np.array([W2_GASOLINE_URBAN + W2_BEV_URBAN, W2_GASOLINE_RURAL + W2_BEV_RURAL, W2_GASOLINE_URBAN + W2_BEV_URBAN + W2_GASOLINE_RURAL + W2_BEV_RURAL])/factorofdivision

    # Paramètres pour décaler les barres
    x = np.arange(len(categories))  # Position des catégories
    width = 0.08  # Largeur des barres

    # Création de la figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Ajout des barres avec un décalage
    ax.bar(x - 1.5 * width, values_gasoline/10**6, width -0.01, label="Gasoline MOTORCYCLE", color=gasoline_color)
    ax.bar(x, values_elec/10**6, width -0.01, label="Electric MOTORCYCLE", color=elec_color)
    ax.bar(x + 1.5 * width, values_total/10**6, width -0.01, label="Total", color=total_color)

    # Configuration des axes
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=14)
    ax.set_ylabel("Number of vehicles [M#]", fontsize=14)
    ax.set_title("Number of MOTORCYCLE", fontsize=18)

    # Ajouter des lignes horizontales tous les 5 unités
    for i in np.arange(0, 2.25, 0.25):
        ax.axhline(i, color="black", linewidth=0.5, linestyle="--", alpha=0.7)

    # Ajout de la légende
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=3, fontsize=14, frameon=False)

    # Suppression des bordures inutiles
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.tick_params(axis="y", labelsize=14)

    # Affichage
    plt.show()


    #do the same for the all the type of cars
    categories = ["Urban", "Rural", "Total"]
    factorofdivision = 10**6
    values_gasoline = np.array([CAR_GASOLINE_URBAN, CAR_GASOLINE_RURAL, CAR_GASOLINE_URBAN + CAR_GASOLINE_RURAL])/factorofdivision
    values_elec = np.array([CAR_BEV_URBAN, CAR_BEV_RURAL, CAR_BEV_URBAN + CAR_BEV_RURAL])/factorofdivision
    values_diesel = np.array([CAR_DIESEL_URBAN, CAR_DIESEL_RURAL, CAR_DIESEL_URBAN + CAR_DIESEL_RURAL])/factorofdivision
    values_hev = np.array([CAR_HEV_URBAN, CAR_HEV_RURAL, CAR_HEV_URBAN + CAR_HEV_RURAL])/factorofdivision
    values_phev = np.array([CAR_PHEV_URBAN, CAR_PHEV_RURAL, CAR_PHEV_URBAN + CAR_PHEV_RURAL])/factorofdivision
    values_FC = np.array([CAR_FC_URBAN, CAR_FC_RURAL, CAR_FC_URBAN + CAR_FC_RURAL])/factorofdivision
    values_NG = np.array([CAR_NG_URBAN, CAR_NG_RURAL, CAR_NG_URBAN + CAR_NG_RURAL])/factorofdivision
    values_total = np.array([CAR_GASOLINE_URBAN + CAR_BEV_URBAN + CAR_DIESEL_URBAN + CAR_HEV_URBAN + CAR_PHEV_URBAN + CAR_FC_URBAN + CAR_NG_URBAN, CAR_GASOLINE_RURAL + CAR_BEV_RURAL + CAR_DIESEL_RURAL + CAR_HEV_RURAL + CAR_PHEV_RURAL + CAR_FC_RURAL + CAR_NG_RURAL, CAR_GASOLINE_URBAN + CAR_BEV_URBAN + CAR_DIESEL_URBAN + CAR_HEV_URBAN + CAR_PHEV_URBAN + CAR_FC_URBAN + CAR_NG_URBAN + CAR_GASOLINE_RURAL + CAR_BEV_RURAL + CAR_DIESEL_RURAL + CAR_HEV_RURAL + CAR_PHEV_RURAL + CAR_FC_RURAL + CAR_NG_RURAL])/factorofdivision
    # Paramètres pour décaler les barres
    x = np.arange(len(categories))  # Position des catégories
    width = 0.08  # Largeur des barres

    # Création de la figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Ajout des barres avec un décalage
    ax.bar(x - 3.5 * width, values_gasoline, width -0.01, label="Gasoline Car", color=gasoline_color)
    ax.bar(x - 2.5 * width, values_diesel, width -0.01, label="Diesel Car", color=diesel_color)
    ax.bar(x - 1.5 * width, values_hev, width -0.01, label="HEV Car", color=HEV_color)
    ax.bar(x - 0.5 * width, values_phev, width -0.01, label="PHEV Car", color=PHEV_color)
    ax.bar(x + 0.5 * width, values_elec, width -0.01, label="BEV Car", color=elec_color)
    ax.bar(x + 1.5 * width, values_FC, width -0.01, label="FC Car", color=h2_color)
    ax.bar(x + 2.5 * width, values_NG, width -0.01, label="NG Car", color=gas_color)
    ax.bar(x + 3.5 * width, values_total, width -0.01, label="Total", color=total_color)

    # Configuration des axes
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=14)
    ax.set_ylabel("Number of vehicles [M#]", fontsize=14)
    ax.set_title("Number of cars", fontsize=18)

    # Ajouter des lignes horizontales tous les 5 unités
    for i in range(0, 9, 1):
        ax.axhline(i, color="black", linewidth=0.5, linestyle="--", alpha=0.7)

    # Ajout de la légende
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), ncol=4, fontsize=14, frameon=False)

    # Suppression des bordures inutiles
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Affichage
    plt.show()

    #do the same for the all the type of buses
    categories = ["Urban", "Rural", "Total"]
    factorofdivision = 10**3
    values_diesel = np.array([BUS_DIESEL_URBAN, BUS_DIESEL_RURAL, BUS_DIESEL_URBAN + BUS_DIESEL_RURAL])/factorofdivision
    values_hev = np.array([BUS_HYDIESEL_URBAN, BUS_HYDIESEL_RURAL, BUS_HYDIESEL_URBAN + BUS_HYDIESEL_RURAL])/factorofdivision
    values_elec = np.array([BUS_ELEC_URBAN, BUS_ELEC_RURAL, BUS_ELEC_URBAN + BUS_ELEC_RURAL])/factorofdivision
    values_FC = np.array([BUS_FC_URBAN, BUS_FC_RURAL, BUS_FC_URBAN + BUS_FC_RURAL])/factorofdivision
    values_NG = np.array([BUS_NG_URBAN, BUS_NG_RURAL, BUS_NG_URBAN + BUS_NG_RURAL])/factorofdivision
    values_total = np.array([BUS_DIESEL_URBAN + BUS_HYDIESEL_URBAN + BUS_ELEC_URBAN + BUS_FC_URBAN + BUS_NG_URBAN, BUS_DIESEL_RURAL + BUS_HYDIESEL_RURAL + BUS_ELEC_RURAL + BUS_FC_RURAL + BUS_NG_RURAL, BUS_DIESEL_URBAN + BUS_HYDIESEL_URBAN + BUS_ELEC_URBAN + BUS_FC_URBAN + BUS_NG_URBAN + BUS_DIESEL_RURAL + BUS_HYDIESEL_RURAL + BUS_ELEC_RURAL + BUS_FC_RURAL + BUS_NG_RURAL])/factorofdivision
    
    x = np.arange(len(categories))  # Position des catégories
    width = 0.08  # Largeur des barres

    # Création de la figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Ajout des barres avec un décalage
    ax.bar(x - 2.5 * width, values_diesel, width -0.01, label="Diesel Bus", color=diesel_color)
    ax.bar(x - 1.5 * width, values_hev, width -0.01, label="HEV Bus", color=PHEV_color)
    ax.bar(x - 0.5 * width, values_elec, width -0.01, label="BEV Bus", color=elec_color)
    ax.bar(x + 0.5 * width, values_FC, width -0.01, label="FC Bus", color=h2_color)
    ax.bar(x + 1.5 * width, values_NG, width -0.01, label="NG Bus", color=gas_color)
    ax.bar(x + 2.5 * width, values_total, width -0.01, label="Total", color=total_color)

    # Configuration des axes
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=14)
    ax.set_ylabel("Number of vehicles [k#]", fontsize=14)
    ax.set_title("Number of buses", fontsize=18)

    # Ajouter des lignes horizontales tous les 5 unités
    for i in range(0, 40, 5):
        ax.axhline(i, color="black", linewidth=0.5, linestyle="--", alpha=0.7)


    # Ajout de la légende
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=6, fontsize=14, frameon=False)

    # Suppression des bordures inutiles
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Affichage
    plt.show()

    #do the same for the all the type of rail

    categories = ["Urban", "Rural", "Total"]
    factorofdivision = 10**3
    values_tram = np.array([TRAMWAY_ELEC_URBAN, 0, TRAMWAY_ELEC_URBAN])/factorofdivision
    values_metro = np.array([METRO_ELEC_URBAN, 0, METRO_ELEC_URBAN])/factorofdivision
    values_train = np.array([0, TRAIN_ELEC_RURAL, TRAIN_ELEC_RURAL])/factorofdivision
    values_total = np.array([TRAMWAY_ELEC_URBAN + METRO_ELEC_URBAN, TRAIN_ELEC_RURAL, TRAMWAY_ELEC_URBAN + METRO_ELEC_URBAN + TRAIN_ELEC_RURAL])/factorofdivision
    # Paramètres pour décaler les barres
    x = np.arange(len(categories))  # Position des catégories
    width = 0.08  # Largeur des barres

    # Création de la figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Ajout des barres avec un décalage
    ax.bar(x - 1.5 * width, values_tram, width -0.01, label="Tramway", color=HEV_color)
    ax.bar(x - 0.5 * width, values_metro, width -0.01, label="Metro", color=PHEV_color)
    ax.bar(x + 0.5 * width, values_train, width -0.01, label="Train", color=elec_color)
    ax.bar(x + 1.5 * width, values_total, width -0.01, label="Total", color=total_color)

    # Configuration des axes
    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=14)
    ax.set_ylabel("Number of vehicles [k#]", fontsize=14)
    ax.set_title("Number of rail", fontsize=18)

    for i in np.arange(0, 9, 1):
        ax.axhline(i, color="black", linewidth=0.5, linestyle="--", alpha=0.7)

    
    # Ajout de la légende
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), ncol=4, fontsize=14, frameon=False)

    # Suppression des bordures inutiles
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_visible(False)

    # Affichage
    plt.show()

