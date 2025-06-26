import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tabulate
import math

PEC = False
shareoflocal = False
shareofHTheat = False
shareofLHTheat = False
shareofelecprod = False
consumptionmobility = False
passengerfleetsize = False
costmobility = False
CO2origins = True
freightfleetconsumption = False
if costmobility :
    passengerfleetsize = True

sys.path.append("c:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/case_studies")
folder1 = "Data/2050_scenario1_trends"
folder2 = "Data/2050_scenario2_sobriety"
folder3 = "Data/2050_scenario3_efficiency"

#get access to the folder which is the folder after the case_studiesr
path1 = os.path.join("c:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/case_studies", folder1)
path1 = os.path.join(path1, "output")
path2 = os.path.join("c:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/case_studies", folder2)
path2 = os.path.join(path2, "output")
path3 = os.path.join("c:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/case_studies", folder3)
path3 = os.path.join(path3, "output")

ressource = {
    "ELECTRICITY": {"display_name": "Imp. electricity", "color": "#8ed1f7"},       # Bleu clair (observé)
    "GASOLINE": {"display_name": "Gasoline", "color": "#8b0000"},
    "DIESEL": {"display_name": "Imp. diesel", "color": "#d3d3d3"},                   # Gris clair
    "BIOETHANOL": {"display_name": "Imp. bioethanol", "color": "#9acd32"},
    "BIODIESEL": {"display_name": "Imp Bio-diesel", "color": "#dcdcdc"},               # Gris clair (ressemble à Imp. Bio-diesel)
    "LFO": {"display_name": "Light Fuel Oil", "color": "#a9a9a9"},
    "GAS": {"display_name": "Imp. Fossil gas", "color": "#ffd700"},
    "GAS_RE": {"display_name": "Imp. Re. gas", "color": "#ffd700"},                      # Jaune vif
    "WOOD": {"display_name": "Wood", "color": "#c9a378"},                          # Brun clair (observé)
    "WET_BIOMASS": {"display_name": "Wet biomass", "color": "#c3916e"},            # Brun plus foncé (observé)
    "COAL": {"display_name": "Coal", "color": "#a97c73"},                          # Brun rougeâtre (observé)
    "URANIUM": {"display_name": "Uranium", "color": "#556b2f"},
    "WASTE": {"display_name": "Waste", "color": "#2e4a62"},                        # Bleu foncé/gris
    "H2": {"display_name": "Imp. Hydrogen", "color": "#87cefa"},
    "H2_RE": {"display_name": "Imp. Re. H2", "color": "#ff00ff"},                        # Rose/magenta
    "AMMONIA": {"display_name": "Imp. Ammonia", "color": "#0000cd"},
    "METHANOL": {"display_name": "Methanol", "color": "#ba55d3"},
    "AMMONIA_RE": {"display_name": "Imp. Re. Ammonia ", "color": "#756fd0"},         # Bleu-violet (observé)
    "METHANOL_RE": {"display_name": "Imp.Re. Methanol ", "color": "#e273ac"},       # Rose foncé (observé)
    "ELEC_EXPORT": {"display_name": "ELECTRICITY export", "color": "#1e90ff"},
    "RES_WIND": {"display_name": "Wind", "color": "#96d8b0"},                      # Vert doux (observé)
    "RES_SOLAR": {"display_name": "Solar", "color": "#f8f05c"},                    # Jaune pâle (observé)
    "RES_HYDRO": {"display_name": "Hydro", "color": "#000000"},                    # Noir (observé pour Hydro-River)
    "RES_GEO": {"display_name": "Geothermal", "color": "#0000ff"},                 # Bleu
    "CO2_ATM": {"display_name": "CO2 in atmosphere", "color": "#cd5c5c"},
    "CO2_INDUSTRY": {"display_name": "Industrial CO2", "color": "#708090"},
    "CO2_CAPTURED": {"display_name": "CO2 captured", "color": "#20b2aa"},
}

HT_HEAT_TECHNO = {
    "IND_COGEN_GAS": {"display_name": "Cogeneration - Gas", "color": "#ffd700"},  # Tomate
    "IND_COGEN_WOOD": {"display_name": "Cogeneration - Wood ", "color": "#8b4513"},  # Marron
    "IND_COGEN_WASTE": {"display_name": "Cogeneration - Waste ", "color": "#228b22"},  # Vert forêt
    "IND_BOILER_GAS": {"display_name": "Boiler - Gas", "color": "#f8f05c"},  # Rouge bordeaux
    "IND_BOILER_WOOD": {"display_name": "Boiler - Wood ", "color": "#deb887"},  # Bois clair
    "IND_BOILER_OIL": {"display_name": "Boiler - Oil ", "color": "#d2691e"},  # Chocolat
    "IND_BOILER_COAL": {"display_name": "Boiler - Coal ", "color": "#2f4f4f"},  # Gris ardoise
    "IND_BOILER_WASTE": {"display_name": "Boiler - Waste ", "color": "#2e4a62"},  # Gris
    "IND_DIRECT_ELEC": {"display_name": "Resistors - Electric ", "color": "#1f77b4"},  # Lavande
}

LT_HEAT_TECHNO = {
    "DHN_HP_ELEC": {"display_name": "Heat pump - DHN", "color": "#4682b4"},  # Bleu acier
    "DHN_COGEN_GAS": {"display_name": "Cogeneration gas (DHN)", "color": "#ff4500"},  # Orange rougeâtre
    "DHN_COGEN_WOOD": {"display_name": "Cogeneration wood (DHN)", "color": "#8b4513"},  # Marron
    "DHN_COGEN_WASTE": {"display_name": "Cogeneration waste (DHN)", "color": "#228b22"},  # Vert forêt
    "DHN_COGEN_WET_BIOMASS": {"display_name": "Cogeneration wet biomass (DHN)", "color": "#2e8b57"},  # Vert moyen
    "DHN_COGEN_BIO_HYDROLYSIS": {"display_name": "Cogeneration bio hydrolysis (DHN)", "color": "#c3916e"},  # Rose profond
    "DHN_BOILER_GAS": {"display_name": "Boiler gas (DHN)", "color": "#b22222"},  # Rouge bordeaux
    "DHN_BOILER_WOOD": {"display_name": "Boiler wood (DHN)", "color": "#deb887"},  # Bois clair
    "DHN_BOILER_OIL": {"display_name": "Boiler oil (DHN)", "color": "#d2691e"},  # Chocolat
    "DHN_DEEP_GEO": {"display_name": "Geothermal (DHN)", "color": "#556b2f"},  # Vert forêt sombre
    "DHN_SOLAR": {"display_name": "Solar thermal (DHN)", "color": "#f8f05c"},  # Jaune pâle
    "DEC_HP_ELEC": {"display_name": "Heat pump - DEC", "color": "#87cefa"},  # Bleu ciel
    "DEC_THHP_GAS": {"display_name": "Thermal heat pump gas (DEC)", "color": "#dcdcdc"},  # Gris clair
    "DEC_COGEN_GAS": {"display_name": "Cogeneration gas (DEC)", "color": "#ff6347"},  # Tomate
    "DEC_COGEN_OIL": {"display_name": "Cogeneration oil (DEC)", "color": "#cd5c5c"},  # Rouge clair
    "DEC_ADVCOGEN_GAS": {"display_name": "Advanced cogeneration (Fuel cell) gas (DEC)", "color": "#ff4500"},  # Orange rougeâtre
    "DEC_ADVCOGEN_H2": {"display_name": "Advanced cogeneration (Fuel cell) gas (DEC)", "color": "#32cd32"},  # Vert lime
    "DEC_BOILER_GAS": {"display_name": "Bioler gas (DEC)", "color": "#b22222"},  # Rouge bordeaux
    "DEC_BOILER_WOOD": {"display_name": "Boiler wood (DEC)", "color": "#8b4513"},  # Marron
    "DEC_BOILER_OIL": {"display_name": "Boiler oil (DEC)", "color": "#d2691e"},  # Chocolat
    "DEC_SOLAR": {"display_name": "Solar thermal (DEC)", "color": "#ffcc00"},  # Jaune vif
    "DEC_DIRECT_ELEC": {"display_name": "Direct electrical heaters (DEC)", "color": "#f4a300"},  # Orange vif
}
ELEC_TECHNO = {
    "ELECTRICITY": {
        "display_name": "Imp. electricity",
        "color": "#8ed1f7"  # DodgerBlue (reste)
    },
    "NUCLEAR": {
        "display_name": "Nuclear",
        "color": "#a9a9a9"
    },
    "CCGT": {
        "display_name": "Combined Cycle Gas Turbine",
        "color": "#ff8c00"
    },
    "CCGT_AMMONIA": {
        "display_name": "CCGT - Ammonia",
        "color": "#756fd0"
    },
    "COAL_US": {
        "display_name": "Ultra-supercritical Coal Power Plant",
        "color": "#2f4f4f"
    },
    "COAL_IGCC": {
        "display_name": "Integrated Gasification Combined Cycle (Coal)",
        "color": "#4b4b4b"
    },
    "PV": {
        "display_name": "PV - Solar",
        "color": "#f8f05c"
    },
    "WIND_ONSHORE": {
        "display_name": "Onshore - Wind",
        "color": "#228b22"
    },
    "WIND_OFFSHORE": {
        "display_name": "Offshore - Wind",
        "color": "#96d8b0"  # SteelBlue (nouveau)
    },
    "HYDRO_RIVER": {
        "display_name": "Hydropower",
        "color": "#000000"  # Turquoise (nouveau)
    },
    "GEOTHERMAL": {
        "display_name": "Geothermal",
        "color": "#8b0000"
    },
    "IND_COGEN_GAS": {
        "display_name": "Cogeneration - Gas",
        "color": "#ffd700"
    },
    "IND_COGEN_WOOD": {
        "display_name": "Cogen Wood",
        "color": "#a0522d"
    },
    "IND_COGEN_WASTE": {
        "display_name": "Cogeneration Waste (Industry)",
        "color": "#696969"
    },
    "DHN_COGEN_GAS": {
        "display_name": "Cogeneration Gas (DHN)",
        "color": "#f08080"
    },
    "DHN_COGEN_WOOD": {
        "display_name": "Cogeneration Wood (DHN)",
        "color": "#8b4513"
    },
    "DHN_COGEN_WASTE": {
        "display_name": "Cogeneration Waste (DHN)",
        "color": "#708090"
    },
    "DHN_COGEN_WET_BIOMASS": {
        "display_name": "Cogeneration Wet Biomass (DHN)",
        "color": "#d2b48c"
    },
    "DHN_COGEN_BIO_HYDROLYSIS": {
        "display_name": "Cogen Hydrolysis (DHN)",
        "color": "#b8860b"
    
    },
    "BIO_HYDROLYSIS": {
        "display_name": "Bio Hydrolysis - Wet Biomass", 
        "color": "#c3916e"}
     
}

transport_technologies = {
    "BIKE_NONELEC_URBAN": {"display_name": "Bike (No ELECTRICITY)", "mode": "bike", "energy": "nonelectric", "energy_bis": "", "energy_display_name": "Non-electric (Bike or similar)", "color": "#ff7f0e", "zone": "urban"},
    "BIKE_ELEC_URBAN": {"display_name": "Electric Bike", "mode": "bike", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "urban"},
    "MOTORCYCLE_GASOLINE_URBAN": {"display_name": "MOTORCYCLE Gasoline", "mode": "MOTORCYCLE", "energy": "GASOLINE", "energy_bis": "", "energy_display_name": "Gasoline", "color": "#ff7f0e", "zone": "urban"},
    "MOTORCYCLE_BEV_URBAN": {"display_name": "MOTORCYCLE Electric", "mode": "MOTORCYCLE", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "urban"},
    "CAR_GASOLINE_URBAN": {"display_name": "Car Gasoline", "mode": "car", "energy": "GASOLINE", "energy_bis": "", "energy_display_name": "Gasoline", "color": "#ff7f0e", "zone": "urban"},
    "CAR_DIESEL_URBAN": {"display_name": "Car Diesel", "mode": "car", "energy": "DIESEL", "energy_bis": "", "energy_display_name": "Diesel", "color": "#dcdcdc", "zone": "urban"},
    "CAR_HEV_URBAN": {"display_name": "Car Hybrid", "mode": "car", "energy": "GASOLINE", "energy_bis": "", "energy_display_name": "Hybrid (HEV)", "color": "#41b8de", "zone": "urban"},
    "CAR_PHEV_URBAN": {"display_name": "Car Plug-in Hybrid", "mode": "car", "energy": "ELECTRICITY", "energy_bis": "GASOLINE", "energy_display_name": "Plug-in Hybrid (PHEV)", "color": "#419ede", "zone": "urban"},
    "CAR_BEV_URBAN": {"display_name": "Car Battery Electric", "mode": "car", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "urban"},
    "CAR_FC_URBAN": {"display_name": "Car Fuel Cell", "mode": "car", "energy": "H2", "energy_bis": "", "energy_display_name": "Hydrogen", "color": "#9467bd", "zone": "urban"},
    "CAR_NG_URBAN": {"display_name": "Car Natural Gas", "mode": "car", "energy": "GAS", "energy_bis": "", "energy_display_name": "Natural Gas", "color": "#ffd700", "zone": "urban"},
    "BUS_DIESEL_URBAN": {"display_name": "Bus Diesel", "mode": "bus", "energy": "DIESEL", "energy_bis": "", "energy_display_name": "Diesel", "color": "#dcdcdc", "zone": "urban"},
    "BUS_HYDIESEL_URBAN": {"display_name": "Bus Hybrid Diesel", "mode": "bus", "energy": "DIESEL", "energy_bis": "", "energy_display_name": "Hybrid Diesel", "color": "#a9a9a9", "zone": "urban"},
    "BUS_ELEC_URBAN": {"display_name": "Bus Electric", "mode": "bus", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "urban"},
    "BUS_FC_URBAN": {"display_name": "Bus Fuel Cell", "mode": "bus", "energy": "H2", "energy_bis": "", "energy_display_name": "Hydrogen", "color": "#9467bd", "zone": "urban"},
    "BUS_NG_URBAN": {"display_name": "Bus Natural Gas", "mode": "bus", "energy": "GAS", "energy_bis": "", "energy_display_name": "Natural Gas", "color": "#ffd700", "zone": "urban"},
    "TRAMWAY_ELEC_URBAN": {"display_name": "Tramway Electric", "mode": "tramway", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "urban"},
    "METRO_ELEC_URBAN": {"display_name": "Metro Electric", "mode": "metro", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "urban"},
    "BIKE_NONELEC_RURAL": {"display_name": "Bike (No ELECTRICITY)", "mode": "bike", "energy": "nonelectric", "energy_bis": "", "energy_display_name": "Non-electric (Bike or similar)", "color": "#ff7f0e", "zone": "rural"},
    "BIKE_ELEC_RURAL": {"display_name": "Electric Bike", "mode": "bike", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "rural"},
    "MOTORCYCLE_GASOLINE_RURAL": {"display_name": "MOTORCYCLE Gasoline", "mode": "MOTORCYCLE", "energy": "GASOLINE", "energy_bis": "", "energy_display_name": "Gasoline", "color": "#ff7f0e", "zone": "rural"},
    "MOTORCYCLE_BEV_RURAL": {"display_name": "MOTORCYCLE Electric", "mode": "MOTORCYCLE", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "rural"},
    "CAR_GASOLINE_RURAL": {"display_name": "Car Gasoline", "mode": "car", "energy": "GASOLINE", "energy_bis": "", "energy_display_name": "Gasoline", "color": "#ff7f0e", "zone": "rural"},
    "CAR_DIESEL_RURAL": {"display_name": "Car Diesel", "mode": "car", "energy": "DIESEL", "energy_bis": "", "energy_display_name": "Diesel", "color": "#dcdcdc", "zone": "rural"},
    "CAR_HEV_RURAL": {"display_name": "Car Hybrid", "mode": "car", "energy": "GASOLINE", "energy_bis": "", "energy_display_name": "Hybrid (HEV)", "color": "#41b8de", "zone": "rural"},
    "CAR_PHEV_RURAL": {"display_name": "Car Plug-in Hybrid", "mode": "car", "energy": "ELECTRICITY", "energy_bis": "GASOLINE", "energy_display_name": "Plug-in Hybrid (PHEV)", "color": "#419ede", "zone": "rural"},
    "CAR_BEV_RURAL": {"display_name": "Car Battery Electric", "mode": "car", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "rural"},
    "CAR_FC_RURAL": {"display_name": "Car Fuel Cell", "mode": "car", "energy": "H2", "energy_bis": "", "energy_display_name": "Hydrogen", "color": "#9467bd", "zone": "rural"},
    "CAR_NG_RURAL": {"display_name": "Car Natural Gas", "mode": "car", "energy": "GAS", "energy_bis": "", "energy_display_name": "Natural Gas", "color": "#ffd700", "zone": "rural"},
    "BUS_DIESEL_RURAL": {"display_name": "Bus Diesel", "mode": "bus", "energy": "DIESEL", "energy_bis": "", "energy_display_name": "Diesel", "color": "#dcdcdc", "zone": "rural"},
    "BUS_HYDIESEL_RURAL": {"display_name": "Bus Hybrid Diesel", "mode": "bus", "energy": "DIESEL", "energy_bis": "", "energy_display_name": "Hybrid Diesel", "color": "#a9a9a9", "zone": "rural"},
    "BUS_ELEC_RURAL": {"display_name": "Bus Electric", "mode": "bus", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "rural"},
    "BUS_FC_RURAL": {"display_name": "Bus Fuel Cell", "mode": "bus", "energy": "H2", "energy_bis": "", "energy_display_name": "Hydrogen", "color": "#9467bd", "zone": "rural"},
    "BUS_NG_RURAL": {"display_name": "Bus Natural Gas", "mode": "bus", "energy": "GAS", "energy_bis": "", "energy_display_name": "Natural Gas", "color": "#ffd700", "zone": "rural"},
    "TRAIN_ELEC_RURAL": {"display_name": "Train Electric", "mode": "train", "energy": "ELECTRICITY", "energy_bis": "", "energy_display_name": "ELECTRICITY", "color": "#1f77b4", "zone": "rural"}
}
colors_mobility = {
    "NONELEC_color": "#8b4513",
    "elec_color": "#1f77b4",
    "BEV_color": "#1f77b4",
    "PHEV_color": "#419ede",
    "HEV_color": "#41b8de",
    "GASOLINE_color": "#ff7f0e",
    "HYDIESEL_color": "#a9a9a9",
    "DIESEL_color": "#dcdcdc",
    "NG_color": "#ffd700",
    "H2_color": "#9467bd",
    "total_color": "#8c564b"
}
real_colors_mobility_private = {
    "Non-motorized": "#8b4513",  # Marron foncé
    "BEV/Electricity": "#1f77b4",
    "PHEV - Gasoline": "#41b8de",
    "HEV - Gasoline": "#8fbc8f",  # Vert clair
    "Gasoline": "#9acd32",
    "Diesel": "#dcdcdc",
    "Gas": "#ffd700",
    "H2": "#ff00ff",
}

real_colors_mobility_public = {
    "BEV/Electricity": "#1f77b4",
    "HEV - Diesel": "#a9a9a9",
    "Diesel": "#dcdcdc",

}

transport_param = {
    "Bike" : {"occupancy" : 1, "Scenario 1" : 1, "Scenario 2" : 1, "Scenario 3" : 1, "distance" : 3120},
    "MOTORCYCLE" : {"occupancy" : 1, "Scenario 1" : 1, "Scenario 2" : 1, "Scenario 3" : 1, "distance" : 1790},
    "Car" : {"occupancy" : 1.24, "Scenario 1" : 1, "Scenario 2" : 1.61, "Scenario 3" : 1.45, "distance" : 15000},
    "Bus" : {"occupancy" : 14.86, "Scenario 1" : 1, "Scenario 2" : 1.2, "Scenario 3" : 1, "distance" : 40000},
    "Tramway" : {"occupancy" : 55, "Scenario 1" : 1, "Scenario 2" : 1.2, "Scenario 3" : 1, "distance" : 39463},
    "Metro" : {"occupancy" : 116, "Scenario 1" : 1, "Scenario 2" : 1.2, "Scenario 3" : 1, "distance" : 69328},
    "Train" : {"occupancy" : 178, "Scenario 1" : 1, "Scenario 2" : 1.2, "Scenario 3" : 1, "distance" : 53922},
}

CO2poss = {
    "NUCLEAR": 0,
    "CCGT": 0,
    "CCGT_AMMONIA": 0,
    "COAL_US": 0,
    "COAL_IGCC": 0,
    "PV": 0,
    "WIND_ONSHORE": 0,
    "WIND_OFFSHORE": 0,
    "HYDRO_RIVER": 0,
    "GEOTHERMAL": 0,
    "IND_COGEN_GAS": 0,
    "IND_COGEN_WOOD": 0,
    "IND_COGEN_WASTE": 0,
    "IND_BOILER_GAS": 0,
    "IND_BOILER_WOOD": 0,
    "IND_BOILER_OIL": 0,
    "IND_BOILER_COAL": 0,
    "IND_BOILER_WASTE": 0,
    "IND_DIRECT_ELEC": 0,
    "DHN_HP_ELEC": 0,
    "DHN_COGEN_GAS": 0,
    "DHN_COGEN_WOOD": 0,
    "DHN_COGEN_WASTE": 0,
    "DHN_COGEN_WET_BIOMASS": 0,
    "DHN_COGEN_BIO_HYDROLYSIS": 0,
    "DHN_BOILER_GAS": 0,
    "DHN_BOILER_WOOD": 0,
    "DHN_BOILER_OIL": 0,
    "DHN_DEEP_GEO": 0,
    "DHN_SOLAR": 0,
    "DEC_HP_ELEC": 0,
    "DEC_THHP_GAS": 0,
    "DEC_COGEN_GAS": 0,
    "DEC_COGEN_OIL": 0,
    "DEC_ADVCOGEN_GAS": 0,
    "DEC_ADVCOGEN_H2": 0,
    "DEC_BOILER_GAS": 0,
    "DEC_BOILER_WOOD": 0,
    "DEC_BOILER_OIL": 0,
    "DEC_SOLAR": 0,
    "DEC_DIRECT_ELEC": 0,
    "BUS_DIESEL_URBAN": 0,
    "BUS_HYDIESEL_URBAN": 0,
    "BUS_ELEC_URBAN": 0,
    "BUS_FC_URBAN": 0,
    "BUS_NG_URBAN": 0,
    "TRAMWAY_ELEC_URBAN": 0,
    "METRO_ELEC_URBAN": 0,
    "MOTORCYCLE_GASOLINE_URBAN": 0,
    "MOTORCYCLE_BEV_URBAN": 0,
    "CAR_GASOLINE_URBAN": 0,
    "CAR_DIESEL_URBAN": 0,
    "CAR_HEV_URBAN": 0,
    "CAR_PHEV_URBAN": 0,
    "CAR_BEV_URBAN": 0,
    "CAR_FC_URBAN": 0,
    "CAR_NG_URBAN": 0,
    "BIKE_NONELEC_URBAN": 0,
    "BIKE_ELEC_URBAN": 0,
    "BUS_DIESEL_RURAL": 0,
    "BUS_HYDIESEL_RURAL": 0,
    "BUS_ELEC_RURAL": 0,
    "BUS_FC_RURAL": 0,
    "BUS_NG_RURAL": 0,
    "TRAIN_ELEC_RURAL": 0,
    "MOTORCYCLE_GASOLINE_RURAL": 0,
    "MOTORCYCLE_BEV_RURAL": 0,
    "CAR_GASOLINE_RURAL": 0,
    "CAR_DIESEL_RURAL": 0,
    "CAR_HEV_RURAL": 0,
    "CAR_PHEV_RURAL": 0,
    "CAR_BEV_RURAL": 0,
    "CAR_FC_RURAL": 0,
    "CAR_NG_RURAL": 0,
    "BIKE_NONELEC_RURAL": 0,
    "BIKE_ELEC_RURAL": 0,
    "TRAIN_FREIGHT": 0,
    "BOAT_FREIGHT_DIESEL": 0,
    "BOAT_FREIGHT_NG": 0,
    "BOAT_FREIGHT_METHANOL": 0,
    "TRUCK_DIESEL": 0,
    "TRUCK_METHANOL": 0,
    "TRUCK_FUEL_CELL": 0,
    "TRUCK_ELEC": 0,
    "TRUCK_NG": 0,
    "HABER_BOSCH": 0,
    "SYN_METHANOLATION": 0,
    "METHANE_TO_METHANOL": 0,
    "BIOMASS_TO_METHANOL": 0,
    "OIL_TO_HVC": 0,
    "GAS_TO_HVC": 0,
    "BIOMASS_TO_HVC": 0,
    "METHANOL_TO_HVC": 0,
    "PHS": 0,
    "BATT_LI": 0,
    "BEV_BATT_URBAN": 0,
    "PHEV_BATT_URBAN": 0,
    "BEV_BATT_RURAL": 0,
    "PHEV_BATT_RURAL": 0,
    "TS_DEC_DIRECT_ELEC": 0,
    "TS_DEC_HP_ELEC": 0,
    "TS_DEC_THHP_GAS": 0,
    "TS_DEC_COGEN_GAS": 0,
    "TS_DEC_COGEN_OIL": 0,
    "TS_DEC_ADVCOGEN_GAS": 0,
    "TS_DEC_ADVCOGEN_H2": 0,
    "TS_DEC_BOILER_GAS": 0,
    "TS_DEC_BOILER_WOOD": 0,
    "TS_DEC_BOILER_OIL": 0,
    "TS_DHN_DAILY": 0,
    "TS_DHN_SEASONAL": 0,
    "TS_HIGH_TEMP": 0,
    "GAS_STORAGE": 0,
    "H2_STORAGE": 0,
    "DIESEL_STORAGE": 0,
    "GASOLINE_STORAGE": 0,
    "LFO_STORAGE": 0,
    "AMMONIA_STORAGE": 0,
    "METHANOL_STORAGE": 0,
    "CO2_STORAGE": 0,
    "EFFICIENCY": 0,
    "DHN": 0,
    "GRID_ELEC": 0,
    "GRID_NG": 0,
    "GRID_H2": 0,
    "H2_ELECTROLYSIS": 0,
    "SMR": 0,
    "H2_BIOMASS": 0,
    "GASIFICATION_SNG": 0,
    "SYN_METHANATION": 0,
    "BIOMETHANATION": 0,
    "BIO_HYDROLYSIS": 0,
    "PYROLYSIS_TO_LFO": 0,
    "PYROLYSIS_TO_FUELS": 0,
    "ATM_CCS": 0,
    "INDUSTRY_CCS": 0,
    "AMMONIA_TO_H2": 0,
    "ELECTRICITY": 0,
    "GASOLINE": 0,
    "DIESEL": 0,
    "BIOETHANOL": 0,
    "BIODIESEL": 0,
    "LFO": 0,
    "WOOD": 0,
    "WET_BIOMASS": 0,
    "COAL": 0,
    "URANIUM": 0,
    "WASTE": 0,
    "GAS": 0,
    "GAS_RE": 0,
    "H2": 0,
    "H2_RE": 0,
    "AMMONIA": 0,
    "METHANOL": 0,
    "AMMONIA_RE": 0,
    "METHANOL_RE": 0,
    "ELEC_EXPORT": 0,
    "CO2_EMISSIONS": 0,
    "RES_WIND": 0,
    "RES_SOLAR": 0,
    "RES_HYDRO": 0,
    "RES_GEO": 0,
    "CO2_ATM": 0,
    "CO2_INDUSTRY": 0,
    "CO2_CAPTURED": 0
}
freight_transport_technologies = {
    "TRAIN_FREIGHT": {
        "display_name": "Freight Train (Electricity)", 
        "mode": "train", 
        "energy": "ELECTRICITY", 
        "energy_bis": "", 
        "energy_display_name": "Electricity", 
        "color": "#1f77b4", 
        "zone": "8ed1f7"
    },
    "BOAT_FREIGHT_DIESEL": {
        "display_name": "Freight Boat (Diesel)", 
        "mode": "boat", 
        "energy": "DIESEL", 
        "energy_bis": "", 
        "energy_display_name": "Imp. Bio Diesel", 
        "color": "#dcdcdc", 
        "zone": "freight"
    },
    "BOAT_FREIGHT_NG": {
        "display_name": "Freight Boat (Natural Gas)", 
        "mode": "boat", 
        "energy": "GAS", 
        "energy_bis": "", 
        "energy_display_name": "Imp. Re. Gas", 
        "color": "#ffd700", 
        "zone": "freight"
    },
    "BOAT_FREIGHT_METHANOL": {
        "display_name": "Freight Boat (Methanol)", 
        "mode": "boat", 
        "energy": "METHANOL", 
        "energy_bis": "", 
        "energy_display_name": "Imp. Re. Methanol", 
        "color": "#e273ac",  # rose pour différencier
        "zone": "freight"
    },
    "TRUCK_DIESEL": {
        "display_name": "Freight Truck (Diesel)", 
        "mode": "truck", 
        "energy": "DIESEL", 
        "energy_bis": "", 
        "energy_display_name": "Imp. Bio Diesel", 
        "color": "#dcdcdc", 
        "zone": "freight"
    },
    "TRUCK_METHANOL": {
        "display_name": "Freight Truck (Methanol)", 
        "mode": "truck", 
        "energy": "METHANOL", 
        "energy_bis": "", 
        "energy_display_name": "Imp. Re. Methanol", 
        "color": "#e273ac", 
        "zone": "freight"
    },
    "TRUCK_FUEL_CELL": {
        "display_name": "Freight Truck (Fuel Cell)", 
        "mode": "truck", 
        "energy": "H2", 
        "energy_bis": "", 
        "energy_display_name": "Imp. Re. Hydrogen", 
        "color": "#ff00ff", 
        "zone": "freight"
    },
    "TRUCK_ELEC": {
        "display_name": "Freight Truck (Electric)", 
        "mode": "truck", 
        "energy": "ELECTRICITY", 
        "energy_bis": "", 
        "energy_display_name": "Electricity", 
        "color": "#1f77b4", 
        "zone": "8ed1f7"
    },
    "TRUCK_NG": {
        "display_name": "Freight Truck (Natural Gas)", 
        "mode": "truck", 
        "energy": "GAS", 
        "energy_bis": "", 
        "energy_display_name": "Imp. Re. Gas", 
        "color": "#ffd700", 
        "zone": "freight"
    }
}

chargingstation = {
    "PRIVATE_ICE_STATION": {"display_name": "Private ICE Station", "color": "#ff7f0e"},
    "PUBLIC_ICE_STATION": {"display_name": "Public ICE Station", "color": "#ff7f0e"},
    "PRIVATE_CNG_STATION": {"display_name": "Private CNG Station", "color": "#ffd700"},
    "PUBLIC_CNG_STATION": {"display_name": "Public CNG Station", "color": "#ffd700"},
    "PRIVATE_H2_STATION": {"display_name": "Private H2 Station", "color": "#9467bd"},
    "PUBLIC_H2_STATION": {"display_name": "Public H2 Station", "color": "#9467bd"},
    "PRIVATE_EV_CHARGER": {"display_name": "Private EV Charger", "color": "#1f77b4"},
    "PUBLIC_EV_CHARGER": {"display_name": "Public EV Charger", "color": "#1f77b4"}
}
if CO2origins:
    df1 = pd.read_csv(os.path.join(path1, "gwp_breakdown.txt"), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, "gwp_breakdown.txt"), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, "gwp_breakdown.txt"), sep=r'\s+', engine='python')

    CO2value_op = np.zeros((len(df1), 3))

    # Parcours des lignes du tableau
    for i in range(len(df1)):
        CO2value_op[i][0] = df1.iloc[i, 2]  # Valeur de CO2 pour le scénario 1
        CO2value_op[i][1] = df2.iloc[i, 2]  # Valeur de CO2 pour le scénario 2
        CO2value_op[i][2] = df3.iloc[i, 2]  # Valeur de CO2 pour le scénario 3

    # Filtrer les technologies avec des valeurs de CO2 supérieures à 1 pour au moins un scénario
    filtered_indices = [i for i in range(len(CO2value_op)) if CO2value_op[i, 0] > 1 or CO2value_op[i, 1] > 1 or CO2value_op[i, 2] > 1]
    filtered_CO2value_op = CO2value_op[filtered_indices]
    filtered_technologies = df1.iloc[filtered_indices, 0]

    # Réorganiser les technologies pour que "GAS" soit en dernier
    reordered_indices = [i for i, tech in enumerate(filtered_technologies) if tech != "GAS"]
    if "GAS" in filtered_technologies.values:
        gas_index = filtered_technologies[filtered_technologies == "GAS"].index
        if len(gas_index) > 0 and gas_index[0] < len(filtered_technologies):
            reordered_indices.append(gas_index[0])
    filtered_technologies = filtered_technologies.iloc[reordered_indices]
    filtered_CO2value_op = filtered_CO2value_op[reordered_indices]

    #ajouter manuellement à la fin de la liste "GAS" pour qu'il soit en dernier
    if "GAS" not in filtered_technologies.values:
        filtered_technologies = pd.concat([filtered_technologies, pd.Series(["GAS"])], ignore_index=False)
        filtered_CO2value_op = np.vstack([filtered_CO2value_op, np.zeros((1, 3))])
        gas_index = df1[df1.iloc[:, 0] == "GAS"].index[0]
        filtered_CO2value_op[-1, :] = CO2value_op[gas_index, :]
    
    # Préparer les données pour le stackbarplot
    scenarios = ["S3: Techno", "S2: Sufficiency", "S1: Trends"]

    # Créer le stackbarplot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Initialiser les barres empilées
    left_scenario_1 = np.zeros(len(scenarios))
    left_scenario_2 = np.zeros(len(scenarios))
    left_scenario_3 = np.zeros(len(scenarios))

    for i, tech in enumerate(filtered_technologies):
        color = ressource.get(tech, {}).get("color", f"C{i}")  # Utiliser la couleur de ressource si disponible
        display_name = "Imp. Fossil Gas" if tech == "GAS" else tech  # Renommer "GAS" en "Fossil Gas"
        if tech == "WOOD" :
            display_name = "Wood"  # Renommer "WOOD" en "Wood" et mettre en minuscule
        if tech == "WET_BIOMASS" :
            display_name = "Wet Biomass"
        if tech == "WASTE" :
            display_name = "Waste"
        ax.barh(scenarios[2], filtered_CO2value_op[i, 2] / 1000, left=left_scenario_3[2], label=display_name, color=color)
        ax.barh(scenarios[1], filtered_CO2value_op[i, 1] / 1000, left=left_scenario_2[1], color=color)
        ax.barh(scenarios[0], filtered_CO2value_op[i, 0] / 1000, left=left_scenario_1[0], color=color)

        # Mettre à jour les bases pour empiler les barres
        left_scenario_1[0] += filtered_CO2value_op[i, 0] / 1000
        left_scenario_2[1] += filtered_CO2value_op[i, 1] / 1000
        left_scenario_3[2] += filtered_CO2value_op[i, 2] / 1000

        

    # Configurer les axes et les étiquettes
    ax.set_yticks(np.arange(len(scenarios)))
    ax.set_yticklabels(scenarios, fontsize=16)
    ax.tick_params(axis='x', labelsize=16)
    ax.set_xlabel("GWP emissions [MtCO2-eq./year]", fontsize=16)
    #ax.set_title("Operational CO2-eq emissions by source", fontsize=18)

    # Ajouter une légende
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Éviter les doublons dans la légende
    ax.legend(by_label.values(), by_label.keys(), fontsize=16, loc="center left", bbox_to_anchor=(1, 0.5), frameon=False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()

    # Importer toutes les valeurs et noms des dfs
    CO2value_const = np.zeros((len(df1), 3))
    technologies = df1.iloc[:, 0].copy()  # Copier les noms des technologies

    for i in range(len(df1)):
        CO2value_const[i][0] = df1.iloc[i, 1]
        CO2value_const[i][1] = df2.iloc[i, 1]
        CO2value_const[i][2] = df3.iloc[i, 1]

    # Filtrer les technologies avec des valeurs de CO2 supérieures à 1 pour au moins un scénario
    filtered_indices = [i for i in range(len(CO2value_const)) if CO2value_const[i, 0] > 1 or CO2value_const[i, 1] > 1 or CO2value_const[i, 2] > 1]
    filtered_CO2value_const = CO2value_const[filtered_indices]
    filtered_technologies = technologies.iloc[filtered_indices].reset_index(drop=True)

    # Fusionner les technologies portant le nom "CAR"
    car_indices = [i for i, tech in enumerate(filtered_technologies) if "CAR" in tech]
    if car_indices:
        car_CO2value_const = np.sum(filtered_CO2value_const[car_indices], axis=0, keepdims=True)
        filtered_CO2value_const = np.delete(filtered_CO2value_const, car_indices, axis=0)
        filtered_CO2value_const = np.vstack([filtered_CO2value_const, car_CO2value_const])
        filtered_technologies = filtered_technologies.drop(car_indices).reset_index(drop=True)
        filtered_technologies = pd.concat([filtered_technologies, pd.Series(["CAR"])], ignore_index=True)

    wind_indices = [i for i, tech in enumerate(filtered_technologies) if "WIND" in tech]
    if wind_indices:
        wind_CO2value_const = np.sum(filtered_CO2value_const[wind_indices], axis=0, keepdims=True)
        filtered_CO2value_const = np.delete(filtered_CO2value_const, wind_indices, axis=0)
        filtered_CO2value_const = np.vstack([filtered_CO2value_const, wind_CO2value_const])
        filtered_technologies = filtered_technologies.drop(wind_indices).reset_index(drop=True)
        filtered_technologies = pd.concat([filtered_technologies, pd.Series(["WIND"])], ignore_index=True)
        #print la valeur de CO2 de la technologie "WIND"
        #print("WIND CO2 value:", wind_CO2value_const)
    # Calculer la somme des émissions pour chaque technologie
    total_CO2 = np.sum(filtered_CO2value_const, axis=1)

    # Trier les technologies par émissions totales (descendant)
    sorted_indices = np.argsort(total_CO2)[::-1]

    # Séparer les 5 plus grandes consommations et les autres
    top_5_indices = sorted_indices[:5]
    other_indices = sorted_indices[5:]

    # Créer des données pour les 5 plus grandes consommations
    top_5_CO2value_const = filtered_CO2value_const[top_5_indices]
    top_5_technologies = filtered_technologies.iloc[top_5_indices]

    # Ajouter les autres sous un même label "Other"
    if len(other_indices) > 0:
        other_CO2value_const = np.sum(filtered_CO2value_const[other_indices], axis=0, keepdims=False)
        top_5_CO2value_const = np.vstack([top_5_CO2value_const, other_CO2value_const])
        top_5_technologies = pd.concat([top_5_technologies, pd.Series(["Other"])], ignore_index=True)
    
    # Réorganiser les technologies pour que "GAS" soit en dernier
    reordered_indices = [i for i, tech in enumerate(top_5_technologies) if tech != "GAS"]
    if "GAS" in top_5_technologies.values:
        reordered_indices.append(top_5_technologies[top_5_technologies == "GAS"].index[0])
    top_5_technologies = top_5_technologies.iloc[reordered_indices]
    top_5_CO2value_const = top_5_CO2value_const[reordered_indices]

    # Réorganiser les technologies pour que "Car" soit en dernier
    reordered_indices = [i for i, tech in enumerate(top_5_technologies) if tech != "CAR"]
    if "CAR" in top_5_technologies.values:
        reordered_indices.append(top_5_technologies[top_5_technologies == "CAR"].index[0])
    top_5_technologies = top_5_technologies.iloc[reordered_indices]
    top_5_CO2value_const = top_5_CO2value_const[reordered_indices]

    # Créer le stackbarplot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Initialiser les barres empilées
    left_scenario_1 = np.zeros(len(scenarios))
    left_scenario_2 = np.zeros(len(scenarios))
    left_scenario_3 = np.zeros(len(scenarios))

    for i, tech in enumerate(top_5_technologies):
        color = ressource.get(tech, {}).get("color", f"C{i}")  # Utiliser la couleur de ressource si disponible
        color = {
            "Car": "#1f77b4",
            "PV": "#f8f05c",
            "Wind": "#96d8b0",
            "Cogeneration - Gas": "#ffd700",
            "Heat Pump - dec": "#87cefa",  # the color of other must be dark
            "Other": "#8b4513",
        }
        if tech == "GAS":
            display_name = "Fossil gas"  # Renommer "GAS" en "fossil gas" et mettre en minuscule
        elif tech == "CAR":
            display_name = "Car"  # Renommer "CAR" en "Car"
        elif tech == "WIND":
            display_name = "Wind"
        elif tech == "IND_COGEN_GAS":
            display_name = "Cogeneration - Gas"
        elif tech == "DEC_HP_ELEC":
            display_name = "Heat Pump - Dec"
        else:
            display_name = tech
        ax.barh(scenarios[2], top_5_CO2value_const[i, 2] / 1000, left=left_scenario_3[2], label=display_name, color=color.get(display_name, "#1f77b4"))
        ax.barh(scenarios[1], top_5_CO2value_const[i, 1] / 1000, left=left_scenario_2[1], color=color.get(display_name, "#1f77b4"))
        ax.barh(scenarios[0], top_5_CO2value_const[i, 0] / 1000, left=left_scenario_1[0], color=color.get(display_name, "#1f77b4"))

        # Mettre à jour les bases pour empiler les barres
        left_scenario_1[0] += top_5_CO2value_const[i, 0] / 1000
        left_scenario_2[1] += top_5_CO2value_const[i, 1] / 1000
        left_scenario_3[2] += top_5_CO2value_const[i, 2] / 1000

    # Configurer les axes et les étiquettes
    ax.set_yticks(np.arange(len(scenarios)))
    ax.set_yticklabels(scenarios, fontsize=16)
    ax.tick_params(axis='x', labelsize=16)
    ax.set_xlabel("GWP emissions [MtCO2-eq./year]", fontsize=16)
    # ax.set_title("Construction CO2-eq emissions by source", fontsize=18)

    # Ajouter une légende
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Éviter les doublons dans la légende
    ax.legend(by_label.values(), by_label.keys(), fontsize=16, loc="center left", bbox_to_anchor=(1, 0.5), frameon=False)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()

    #print the sum of the CO2 emissions construction for each scenario
    sum_scenario_1 = np.sum(top_5_CO2value_const[:, 0])
    sum_scenario_2 = np.sum(top_5_CO2value_const[:, 1])
    sum_scenario_3 = np.sum(top_5_CO2value_const[:, 2])
    print("Total CO2 emissions construction for scenario 1:", sum_scenario_1, "MtCO2-eq./year")
    print("Total CO2 emissions construction for scenario 2:", sum_scenario_2, "MtCO2-eq./year")
    print("Total CO2 emissions construction for scenario 3:", sum_scenario_3, "MtCO2-eq./year")
if passengerfleetsize:
    df1 = pd.read_csv(os.path.join(path1, "year_balance.txt"), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, "year_balance.txt"), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, "year_balance.txt"), sep=r'\s+', engine='python')    

    # Liste des noms à chercher basée sur transport_param
    list_name = []
    for mode in transport_param.keys():
        for tech in transport_technologies.keys():
            if mode.lower() in tech.lower():
                list_name.append(tech)

    list_mobility = ['MOB_PUBLIC_URBAN', 'MOB_PRIVATE_NA_URBAN', 'MOB_PRIVATE_A_URBAN', 'MOB_PUBLIC_RURAL', 'MOB_PRIVATE_NA_RURAL', 'MOB_PRIVATE_A_RURAL']

    # Initialisation des variables pour chaque technologie et scénario
    tech_totals_scenario_1 = {tech: 0 for tech in list_name}
    tech_totals_scenario_2 = {tech: 0 for tech in list_name}
    tech_totals_scenario_3 = {tech: 0 for tech in list_name}

    # Fonction pour calculer les totaux pour un scénario donné
    def calculate_totals(df, tech_totals, scenario_key):
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
                                mode = next((mode for mode in transport_param.keys() if mode.lower() in name.lower()), None)
                                if mode:
                                    tech_totals[name] += value / (transport_param[mode]["occupancy"] * transport_param[mode]["distance"] * transport_param[mode][scenario_key])

    # Calcul des totaux pour chaque scénario
    calculate_totals(df1, tech_totals_scenario_1, "Scenario 1")
    calculate_totals(df2, tech_totals_scenario_2, "Scenario 2")
    calculate_totals(df3, tech_totals_scenario_3, "Scenario 3")

    # Création de la liste contenant les technologies et leurs résultats pour les 3 scénarios
    results = []
    for tech in list_name:
        results.append([tech, tech_totals_scenario_1[tech], tech_totals_scenario_2[tech], tech_totals_scenario_3[tech]])
    
    # Affichage des résultats sous forme de tableau avec pandas
    results_df = pd.DataFrame(results, columns=["Technology", "Scenario 1", "Scenario 2", "Scenario 3"])
    print(tabulate.tabulate(results_df, headers="keys", tablefmt="grid", showindex=False))


    # Extract the number of bikes needed for urban and rural areas based on fuel type
    bike_scenario = {fuel: [0, 0, 0] for fuel in colors_mobility.keys()}
    MOTORCYCLE_scenario = {fuel: [0, 0, 0] for fuel in colors_mobility.keys()}
    car_scenario = {fuel: [0, 0, 0] for fuel in colors_mobility.keys()}
    bus_scenario = {fuel: [0, 0, 0] for fuel in colors_mobility.keys()}
    tramway_scenario = {fuel: [0, 0, 0] for fuel in colors_mobility.keys()}
    metro_scenario = {fuel: [0, 0, 0] for fuel in colors_mobility.keys()}
    train_scenario = {fuel: [0, 0, 0] for fuel in colors_mobility.keys()}

    for row in results:
        tech, scenario_1, scenario_2, scenario_3 = row
        if "bike" in tech.lower():  # Check if "bike" is in the technology name
            for fuel, color in colors_mobility.items():
                if fuel.split("_")[0].lower() in tech.lower():
                    bike_scenario[fuel][0] += scenario_1
                    bike_scenario[fuel][1] += scenario_2
                    bike_scenario[fuel][2] += scenario_3
        elif "MOTORCYCLE" in tech:  # Check if "MOTORCYCLE" (MOTORCYCLE) is in the technology name
            for fuel, color in colors_mobility.items():
                if fuel.split("_")[0].lower() in tech.lower():
                    MOTORCYCLE_scenario[fuel][0] += scenario_1
                    MOTORCYCLE_scenario[fuel][1] += scenario_2
                    MOTORCYCLE_scenario[fuel][2] += scenario_3
        elif "car" in tech.lower():  # Check if "car" is in the technology name
            for fuel, color in colors_mobility.items():
                if fuel.split("_")[0].lower() in tech.lower():
                    car_scenario[fuel][0] += scenario_1
                    car_scenario[fuel][1] += scenario_2*0.
                    car_scenario[fuel][2] += scenario_3
        elif "bus" in tech.lower():  # Check if "bus" is in the technology name
            for fuel, color in colors_mobility.items():
                fuel_prefix = fuel.split("_")[0].lower()
                if fuel_prefix in tech.lower() and not (fuel_prefix == "diesel" and "hydiesel" in tech.lower()):
                    bus_scenario[fuel][0] += scenario_1
                    bus_scenario[fuel][1] += scenario_2
                    bus_scenario[fuel][2] += scenario_3
        elif "tram" in tech.lower():  # Check if "tram" is in the technology name
            for fuel, color in colors_mobility.items():
                if fuel.split("_")[0].lower() in tech.lower():
                    tramway_scenario[fuel][0] += scenario_1
                    tramway_scenario[fuel][1] += scenario_2
                    tramway_scenario[fuel][2] += scenario_3
        elif "metro" in tech.lower():  # Check if "metro" is in the technology name
            for fuel, color in colors_mobility.items():
                if fuel.split("_")[0].lower() in tech.lower():
                    metro_scenario[fuel][0] += scenario_1
                    metro_scenario[fuel][1] += scenario_2
                    metro_scenario[fuel][2] += scenario_3
        elif "train" in tech.lower():  # Check if "train" is in the technology name
            for fuel, color in colors_mobility.items():
                if fuel.split("_")[0].lower() in tech.lower():
                    train_scenario[fuel][0] += scenario_1
                    train_scenario[fuel][1] += scenario_2
                    train_scenario[fuel][2] += scenario_3
        
    #print the sum of each type of vehicle and per scenario in a table
    # Create a DataFrame for the results
    results_df = pd.DataFrame({
        "Technology": ["Bike", "MOTORCYCLE", "Car", "Bus", "Tramway", "Metro", "Train","Total"],
        "Scenario 1": [sum(bike_scenario[fuel][0] for fuel in bike_scenario), sum(MOTORCYCLE_scenario[fuel][0] for fuel in MOTORCYCLE_scenario), sum(car_scenario[fuel][0] for fuel in car_scenario), sum(bus_scenario[fuel][0] for fuel in bus_scenario), sum(tramway_scenario[fuel][0] for fuel in tramway_scenario), sum(metro_scenario[fuel][0] for fuel in metro_scenario), sum(train_scenario[fuel][0] for fuel in train_scenario),sum(bike_scenario[fuel][0] for fuel in bike_scenario) + sum(MOTORCYCLE_scenario[fuel][0] for fuel in MOTORCYCLE_scenario) + sum(car_scenario[fuel][0] for fuel in car_scenario) + sum(bus_scenario[fuel][0] for fuel in bus_scenario) + sum(tramway_scenario[fuel][0] for fuel in tramway_scenario) + sum(metro_scenario[fuel][0] for fuel in metro_scenario) + sum(train_scenario[fuel][0] for fuel in train_scenario)],
        "Scenario 2": [sum(bike_scenario[fuel][1] for fuel in bike_scenario), sum(MOTORCYCLE_scenario[fuel][1] for fuel in MOTORCYCLE_scenario), sum(car_scenario[fuel][1] for fuel in car_scenario), sum(bus_scenario[fuel][1] for fuel in bus_scenario), sum(tramway_scenario[fuel][1] for fuel in tramway_scenario), sum(metro_scenario[fuel][1] for fuel in metro_scenario), sum(train_scenario[fuel][1] for fuel in train_scenario),sum(bike_scenario[fuel][1] for fuel in bike_scenario) + sum(MOTORCYCLE_scenario[fuel][1] for fuel in MOTORCYCLE_scenario) + sum(car_scenario[fuel][1] for fuel in car_scenario) + sum(bus_scenario[fuel][1] for fuel in bus_scenario) + sum(tramway_scenario[fuel][1] for fuel in tramway_scenario) + sum(metro_scenario[fuel][1] for fuel in metro_scenario) + sum(train_scenario[fuel][1] for fuel in train_scenario)],
        "Scenario 3": [sum(bike_scenario[fuel][2] for fuel in bike_scenario), sum(MOTORCYCLE_scenario[fuel][2] for fuel in MOTORCYCLE_scenario), sum(car_scenario[fuel][2] for fuel in car_scenario), sum(bus_scenario[fuel][2] for fuel in bus_scenario), sum(tramway_scenario[fuel][2] for fuel in tramway_scenario), sum(metro_scenario[fuel][2] for fuel in metro_scenario), sum(train_scenario[fuel][2] for fuel in train_scenario),sum(bike_scenario[fuel][2] for fuel in bike_scenario) + sum(MOTORCYCLE_scenario[fuel][2] for fuel in MOTORCYCLE_scenario) + sum(car_scenario[fuel][2] for fuel in car_scenario) + sum(bus_scenario[fuel][2] for fuel in bus_scenario) + sum(tramway_scenario[fuel][2] for fuel in tramway_scenario) + sum(metro_scenario[fuel][2] for fuel in metro_scenario) + sum(train_scenario[fuel][2] for fuel in train_scenario)],
    })
    print(tabulate.tabulate(results_df, headers="keys", tablefmt="grid", showindex=False))


    
    # Create the subplots with adjusted height ratios for more spacing
    fig, axes = plt.subplots(3, 1, figsize=(10, 18), gridspec_kw={'hspace': 0.2}, sharex=True)

    scenarios = ["S1: Trends", "S2: Sufficiency", "S3: Techno"]
    y = np.arange(len(scenarios))[::-1]  # Reverse the order for proper display

    # Plot bikes by fuel type
    left_bike = np.zeros(len(scenarios))
    for fuel, values in bike_scenario.items():
        values = np.array(values)/10**6  # Convert to numpy array for easier manipulation
        if any(values):  # Only include labels with non-zero values
            axes[0].barh(y, values, left=left_bike, color=colors_mobility[fuel])
            left_bike += values

    # Configure the bike plot
    axes[0].set_yticks(y)
    axes[0].set_yticklabels(scenarios, fontsize=16)
    axes[0].text(0.01, 1, "Bike", fontsize=16, ha="left", va="bottom", transform=axes[0].transAxes)
    axes[0].text(0.99, 0.02, r"$\times 10^6$", fontsize=16, ha="right", va="bottom", transform=axes[0].transAxes)
    axes[0].tick_params(axis='x', labelbottom=False)  # Hide x-axis ticks for this subplot

    # Plot MOTORCYCLEs by fuel type
    left_MOTORCYCLE = np.zeros(len(scenarios))
    for fuel, values in MOTORCYCLE_scenario.items():
        values = np.array(values)/10**6  # Convert to numpy array for easier manipulation
        if any(values):  # Only include labels with non-zero values
            axes[1].barh(y, values, left=left_MOTORCYCLE, color=colors_mobility[fuel])
            left_MOTORCYCLE += values

    # Configure the MOTORCYCLE plot
    axes[1].set_yticks(y)
    axes[1].set_yticklabels(scenarios, fontsize=16)
    axes[1].text(0.01, 1, "Motorcycle", fontsize=16, ha="left", va="bottom", transform=axes[1].transAxes)
    axes[1].text(0.99, 0.02, r"$\times 10^6$", fontsize=16, ha="right", va="bottom", transform=axes[1].transAxes)
    axes[1].tick_params(axis='x', labelbottom=False)  # Hide x-axis ticks for this subplot

    # Plot cars by fuel type
    left_car = np.zeros(len(scenarios))
    for fuel, values in car_scenario.items():
        values = np.array(values)/10**6  # Convert to numpy array for easier manipulation
        if any(values):  # Only include labels with non-zero values
            axes[2].barh(y, values, left=left_car, color=colors_mobility[fuel])
            left_car += values

    # Configure the car plot
    axes[2].set_yticks(y)
    axes[2].set_yticklabels(scenarios, fontsize=16)
    axes[2].text(0.01, 1, "Car", fontsize=16, ha="left", va="bottom", transform=axes[2].transAxes)
    axes[2].text(0.99, 0.02, r"$\times 10^6$", fontsize=16, ha="right", va="bottom", transform=axes[2].transAxes)
    axes[2].tick_params(axis='x', labelsize=16)  # Show x-axis ticks only for the bottom subplot

    # Add a single legend for all plots
    handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in real_colors_mobility_private.values()]
    labels = list(real_colors_mobility_private.keys())
    fig.legend(handles, labels, fontsize=16, loc="center right", bbox_to_anchor=(1.005, 0.5), ncol=1, frameon=False)

    # Add x-axis label
    axes[2].set_xlabel("Number of vehicles [#]", fontsize=16)

    # Add a global title
    #fig.suptitle("Number of operational private vehicles", fontsize=18)

 


    # Create the subplots for bus, tram, metro, and train
    fig, axes = plt.subplots(4, 1, figsize=(10, 24), sharex=True, gridspec_kw={'hspace': 0.25})

    # Plot buses by fuel type
    left_bus = np.zeros(len(scenarios))
    for fuel, values in bus_scenario.items():
        values = np.array(values)/10**2  # Convert to numpy array for easier manipulation
        if any(values):  # Only include labels with non-zero values
            axes[0].barh(y, values, left=left_bus, color=colors_mobility[fuel])
            left_bus += values

    # Configure the bus plot
    axes[0].set_yticks(y)
    axes[0].set_yticklabels(scenarios, fontsize=16)
    axes[0].text(0.01, 1, "Bus", fontsize=16, ha="left", va="bottom", transform=axes[0].transAxes)
    axes[0].text(0.99, 0.02, r"$\times 10^2$", fontsize=16, ha="right", va="bottom", transform=axes[0].transAxes)
    axes[0].tick_params(axis='x', labelbottom=False)  # Hide x-axis ticks for this subplot

    # Plot trams by fuel type
    left_tram = np.zeros(len(scenarios))
    for fuel, values in tramway_scenario.items():
        values = np.array(values)/10   # Convert to numpy array for easier manipulation
        if any(values):  # Only include labels with non-zero values
            axes[1].barh(y, values, left=left_tram, color=colors_mobility[fuel])
            left_tram += values

    # Configure the tram plot
    axes[1].set_yticks(y)
    axes[1].set_yticklabels(scenarios, fontsize=16)
    axes[1].text(0.01, 1, "Tram", fontsize=16, ha="left", va="bottom", transform=axes[1].transAxes)
    axes[1].text(0.99, 0.02, r"$\times 10^1$", fontsize=16, ha="right", va="bottom", transform=axes[1].transAxes)
    axes[1].tick_params(axis='x', labelbottom=False)  # Hide x-axis ticks for this subplot

    # Plot metros by fuel type
    left_metro = np.zeros(len(scenarios))
    for fuel, values in metro_scenario.items():
        values = np.array(values)   # Convert to numpy array for easier manipulation
        if any(values):  # Only include labels with non-zero values
            axes[2].barh(y, values, left=left_metro, color=colors_mobility[fuel])
            left_metro += values

    # Configure the metro plot
    axes[2].set_yticks(y)
    axes[2].set_yticklabels(scenarios, fontsize=16)
    axes[2].text(0.01, 1, "Metro", fontsize=16, ha="left", va="bottom", transform=axes[2].transAxes)
    axes[2].tick_params(axis='x', labelbottom=False)  # Hide x-axis ticks for this subplot

    # Plot trains by fuel type
    left_train = np.zeros(len(scenarios))
    for fuel, values in train_scenario.items():
        values = np.array(values)/10  # Convert to numpy array for easier manipulation
        if any(values):  # Only include labels with non-zero values
            axes[3].barh(y, values, left=left_train, color=colors_mobility[fuel])
            left_train += values

    # Configure the train plot
    axes[3].set_yticks(y)
    axes[3].set_yticklabels(scenarios, fontsize=16)
    axes[3].text(0.01, 1, "Train", fontsize=16, ha="left", va="bottom", transform=axes[3].transAxes)
    axes[3].text(0.99, 0.02, r"$\times 10^1$", fontsize=16, ha="right", va="bottom", transform=axes[3].transAxes)
    axes[3].tick_params(axis='x', labelsize=16)  # Show x-axis ticks only for the bottom subplot

    # Add a single legend for all plots
    handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in real_colors_mobility_public.values()]
    labels = list(real_colors_mobility_public.keys())
    fig.legend(handles, labels, fontsize=16, loc="center right", bbox_to_anchor=(1.005, 0.5), ncol=1, frameon=False)

    # Add x-axis label
    axes[3].set_xlabel("Number of vehicles [#]", fontsize=16)

    # Add a global title
    #fig.suptitle("Number of operational public vehicles", fontsize=20)
    plt.show()
if costmobility:
    df1 = pd.read_csv(os.path.join(path1, "cost_breakdown.txt"), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, "cost_breakdown.txt"), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, "cost_breakdown.txt"), sep=r'\s+', engine='python')
    df1_bis = pd.read_csv(os.path.join(path1, "year_balance.txt"), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2_bis = pd.read_csv(os.path.join(path2, "year_balance.txt"), sep=r'\s+', engine='python')
    df3_bis = pd.read_csv(os.path.join(path3, "year_balance.txt"), sep=r'\s+', engine='python')
    non_active_road_inv = np.zeros(3)
    non_active_road_main = np.zeros(3)
    non_active_road_op = np.zeros(3)
    non_active_road_inf_inv = np.zeros(3)
    non_active_road_inf_main = np.zeros(3)
    active_road_inv = np.zeros(3)
    active_road_main = np.zeros(3)
    active_road_op = np.zeros(3)
    active_road_inf_inv = np.zeros(3)
    active_road_inf_main = np.zeros(3)
    railways_inv = np.zeros(3)
    railways_main = np.zeros(3)
    railways_op = np.zeros(3)
    railways_inf_inv = np.zeros(3)
    railways_inf_main = np.zeros(3)
    cout_public_inv = np.zeros(3)
    cout_public_main = np.zeros(3)
    cout_public_op = np.zeros(3)
    cout_public_inf_inv = np.zeros(3)
    cout_public_inf_main = np.zeros(3)
    cout_prive_inv = np.zeros(3)
    cout_prive_main = np.zeros(3)
    cout_prive_op = np.zeros(3)
    cout_prive_inf_inv = np.zeros(3)
    cout_prive_inf_main = np.zeros(3)
    
    # Create a dictionary to store 3x3 numpy arrays for each transport technology
    transport_costs = {name: np.zeros((3, 3)) for name in transport_technologies.keys()}
    bike_infra = np.zeros((3, 2))
    motorcycle_infra = np.zeros((3, 2))
    car_infra = np.zeros((3, 2))
    bus_infra = np.zeros((3, 2))
    tramway_infra = np.zeros((3, 2))
    metro_infra = np.zeros((3, 2))
    train_infra = np.zeros((3, 2))
    bike_charging = np.zeros((3, 2))
    motorcycle_charging = np.zeros((3, 2))
    car_charging = np.zeros((3, 2))
    bus_charging = np.zeros((3, 2))
    tramway_charging = np.zeros((3, 2))
    metro_charging = np.zeros((3, 2))
    train_charging = np.zeros((3, 2))
    #bouclé sur les noms de la première colonne qui sont les technologies de mobilié
    for i in range(len(df1)):
        for charger in chargingstation.keys():
            if charger in df1.iloc[i, 0]:
                # Parcours des énergies pour les 3 scénarios
                for j, df in enumerate([df1, df2, df3]):
                    #trouver les pourcentages de moto vs de voiture
                    scenario_idx = j
                    total = sum(results[k][scenario_idx + 1] for k in range(4, 8)) + sum(results[k][scenario_idx + 1] for k in range(9, 23))
                    percentmoto = sum(results[k][scenario_idx + 1] for k in range(4, 8)) / total
                    percentcar = sum(results[k][scenario_idx + 1] for k in range(9, 23)) / total
                    if "PRIVATE_ICE" in charger:
                        non_active_road_inf_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_inf_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_prive_inf_inv[j] += df.loc[i, "C_inv"]
                        cout_prive_inf_main[j] += df.loc[i, "C_maint"]
                        motorcycle_charging[j][0] = df.loc[i, "C_inv"]
                        motorcycle_charging[j][1] = df.loc[i, "C_maint"]
                        car_charging[j][0] = df.loc[i, "C_inv"]
                        car_charging[j][1] = df.loc[i, "C_maint"]
                    if "PUBLIC_ICE" in charger:
                        non_active_road_inf_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_inf_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_public_inf_inv[j] += df.loc[i, "C_inv"]
                        cout_public_inf_main[j] += df.loc[i, "C_maint"]
                        bus_charging[j][0] = df.loc[i, "C_inv"]
                        bus_charging[j][1] = df.loc[i, "C_maint"]
    
                    if "PRIVATE_CNG" in charger:
                        non_active_road_inf_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_inf_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_prive_inf_inv[j] += df.loc[i, "C_inv"]
                        cout_prive_inf_main[j] += df.loc[i, "C_maint"]
                        car_charging[j][0] = df.loc[i, "C_inv"]
                        car_charging[j][1] = df.loc[i, "C_maint"]
                    if "PUBLIC_CNG" in charger:
                        non_active_road_inf_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_inf_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_public_inf_inv[j] += df.loc[i, "C_inv"]
                        cout_public_inf_main[j] += df.loc[i, "C_maint"]
                        cout_public_op[j] += df.loc[i, "C_op"]
                        bus_charging[j][0] = df.loc[i, "C_inv"]
                        bus_charging[j][1] = df.loc[i, "C_maint"]
                    if "PRIVATE_H2" in charger:
                        non_active_road_inf_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_inf_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_prive_inf_inv[j] += df.loc[i, "C_inv"]
                        cout_prive_inf_main[j] += df.loc[i, "C_maint"]
                        car_charging[j][0] = df.loc[i, "C_inv"]
                        car_charging[j][1] = df.loc[i, "C_maint"]
                    if "PUBLIC_H2" in charger:
                        non_active_road_inf_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_inf_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_public_inf_inv[j] += df.loc[i, "C_inv"]
                        cout_public_inf_main[j] += df.loc[i, "C_maint"]
                        cout_public_op[j] += df.loc[i, "C_op"]
                        bus_charging[j][0] = df.loc[i, "C_inv"]
                    if "PRIVATE_EV_CHARGER" in charger:
                        non_active_road_inf_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_inf_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_prive_inf_inv[j] += df.loc[i, "C_inv"] * 0.8
                        cout_prive_inf_main[j] += df.loc[i, "C_maint"] * 0.8
                        cout_public_inf_inv[j] += df.loc[i, "C_inv"] * 0.2
                        cout_public_inf_main[j] += df.loc[i, "C_maint"] * 0.2
                        cout_public_op[j] += df.loc[i, "C_op"] * 0
                        car_charging[j][0] = df.loc[i, "C_inv"]
                        car_charging[j][1] = df.loc[i, "C_maint"]
                    if "PUBLIC_EV_CHARGER" in charger:
                        non_active_road_inf_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_inf_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_public_inf_inv[j] += df.loc[i, "C_inv"]
                        cout_public_inf_main[j] += df.loc[i, "C_maint"]
                        cout_public_op[j] += df.loc[i, "C_op"]
                        bus_charging[j][0] = df.loc[i, "C_inv"]
        #pour chaque technologie de mobilité, on va chercher les coûts dans la colonne correspondante
        for name in transport_technologies.keys():
            if name in df1.iloc[i, 0]:
                # Parcours des énergies pour les 3 scénarios
                for j, df in enumerate([df1, df2, df3]):
                    transport_costs[name][j, 0] += df.loc[i, "C_inv"]
                    transport_costs[name][j, 1] += df.loc[i, "C_maint"]
                    transport_costs[name][j, 2] += df.loc[i, "C_op"]
                    if "BIKE" in name:
                        active_road_inv[j] += df.loc[i, "C_inv"]
                        active_road_main[j] += df.loc[i, "C_maint"]
                        active_road_op[j] += df.loc[i, "C_op"]
                        cout_prive_inv[j] += df.loc[i, "C_inv"]
                        cout_prive_main[j] += df.loc[i, "C_maint"]
                        cout_prive_op[j] += df.loc[i, "C_op"]

                    if "MOTORCYCLE" in name or "CAR" in name:
                        non_active_road_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_prive_inv[j] += df.loc[i, "C_inv"]
                        cout_prive_main[j] += df.loc[i, "C_maint"]
                        cout_prive_op[j] += df.loc[i, "C_op"]
                        
                    if "BUS" in name :
                        non_active_road_inv[j] += df.loc[i, "C_inv"]
                        non_active_road_main[j] += df.loc[i, "C_maint"]
                        non_active_road_op[j] += df.loc[i, "C_op"]
                        cout_public_inv[j] += df.loc[i, "C_inv"]
                        cout_public_main[j] += df.loc[i, "C_maint"]
                        cout_public_op[j] += df.loc[i, "C_op"]
                    if "TRAMWAY" in name or "METRO" in name or "TRAIN" in name:
                        railways_inv[j] += df.loc[i, "C_inv"]
                        railways_main[j] += df.loc[i, "C_maint"]
                        railways_op[j] += df.loc[i, "C_op"]
                        cout_public_inv[j] += df.loc[i, "C_inv"]
                        cout_public_main[j] += df.loc[i, "C_maint"]
                        cout_public_op[j] += df.loc[i, "C_op"]


    #take all the technologies that produce electricity and sum their costs
    coutelectricity = np.zeros(3)
    electricity_production = np.zeros(3)

    #la production d'électricité est la somme de toutes les technologies qui produisent de l'électricité
    for name in ELEC_TECHNO.keys():
        for j, df in enumerate([df1_bis, df2_bis, df3_bis]):
            matching_rows = df[df.iloc[:, 0].str.contains(name, na=False)]
            for _, row in matching_rows.iterrows():
                if "CCGT" in name:
                    electricity_production[j] += row["ELECTRICITY"]/2
                else:
                    electricity_production[j] += row["ELECTRICITY"]

    for i in range(len(df1)):
        for name in ELEC_TECHNO.keys():
            if name in df1.iloc[i, 0]:
                # Parcours des énergies pour les 3 scénarios
                for j, df in enumerate([df1, df2, df3]):
                    if "COGEN" in name:
                        elecprod = [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()
                        heatprod = (
                            [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "HEAT_HIGH_T"].sum() +
                            [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "HEAT_LOW_T_DHN"].sum() +
                            [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "HEAT_LOW_T_DECEN"].sum()
                        )
                        rendement = elecprod / (elecprod + heatprod)
                        if "IND_COGEN_GAS" in name:
                            coutelectricity[j] += (df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]) * rendement
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GAS"].sum() * rendement * 0.05329867
                        if "IND_COGEN_WOOD" in name:
                            coutelectricity[j] += (df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]) * rendement
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "WOOD"].sum() * rendement * 0.03550648
                        if "IND_COGEN_WASTE" in name:
                            coutelectricity[j] += (df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]) * rendement
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "WASTE"].sum() * rendement * 0.02497388
                        if "DHN_COGEN_GAS" in name:
                            coutelectricity[j] += (df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]) * rendement
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GAS"].sum() * rendement * 0.05329867
                        if "DHN_COGEN_WOOD" in name:
                            coutelectricity[j] += (df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]) * rendement
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "WOOD"].sum() * rendement * 0.03550648
                        if "DHN_COGEN_WASTE" in name:
                            coutelectricity[j] += (df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]) * rendement
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "WASTE"].sum() * rendement *0.02497388
                        if "DHN_COGEN_WET_BIOMASS" in name:
                            coutelectricity[j] += (df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]) * rendement
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "WET_BIOMASS"].sum() * rendement * 0.00622964
                        if "DHN_COGEN_BIO_HYDROLYSIS" in name:
                            coutelectricity[j] += (df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]) * rendement
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "WET_BIOMASS"].sum() * rendement * 0.00622964
                            
                    elif "CCGT" in name:
                        coutelectricity[j] += (df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"])/2
                        if "CCGT_AMMONIA" in name:
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "AMMONIA"].sum() * 0.11407418/2
                        else :
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GAS"].sum() * 0.10430636/2
                    elif "ELECTRICITY" in name:
                        coutelectricity[j] += df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]
                        coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum() * 0.104928
                    elif "COAL" in name:
                        coutelectricity[j] += df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]
                        if "COAL_US" in name:
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "COAL"].sum() * 0.01814538
                        else:
                            coutelectricity[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "COAL"].sum() * 0.01814538
                    else:
                        coutelectricity[j] += df.loc[i, "C_inv"] + df.loc[i, "C_maint"] + df.loc[i, "C_op"]
                
    coutelecsup = [
            "PHS",
            "BATT_LI",
            "BEV_BATT_URBAN",
            "PHEV_BATT_URBAN",
            "BEV_BATT_RURAL",
            "PHEV_BATT_RURAL",
            "GRID_ELEC",
            "EFFICIENCY"
        ]
    for j, df in enumerate([df1, df2, df3]):
        for name in coutelecsup:
            matching_rows = df[df.iloc[:, 0].str.contains(name, na=False)]
            for _, row in matching_rows.iterrows():
                coutelectricity[j] += row["C_inv"] + row["C_maint"] + row["C_op"]
    
    elec_price_per_kWh = coutelectricity/electricity_production  # Coût de l'électricité en $/kWh
    gas_price_kwh = 0.05329867 + 0.25
    diesel_price_kwh = 0.09105369
    gasoline_price_kwh = 0.09404786
    h2_price_kwh = 0.0955067
    print("Electricity price per kWh:" , elec_price_per_kWh)
    
    #prendre la consummation de chaque technologie et la multiplier par le prix de l'énergie
    for i in range (len(df1)):
        for name in transport_technologies.keys():
            if name in df1.iloc[i, 0]:
                # Parcours des énergies pour les 3 scénarios
                for j, df in enumerate([df1, df2, df3]):
                    if "BIKE_ELEC" in name:
                        active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]/10**6
                    if "MOTORCYCLE_BEV" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]/10**6
                    if "MOTORCYCLE_GASOLINE" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh/10**6
                    if "CAR_BEV" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]/10**6
                    if "CAR_GASOLINE" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh/10**6
                    if "CAR_DIESEL" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "DIESEL"].sum()* 10**6 * diesel_price_kwh
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "DIESEL"].sum()* 10**6 * diesel_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "DIESEL"].sum()* 10**6 * diesel_price_kwh/10**6
                    if "CAR_NG" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GAS"].sum()* 10**6 * gas_price_kwh
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GAS"].sum()* 10**6 * gas_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GAS"].sum()* 10**6 * gas_price_kwh/10**6
                    if "CAR_HEV" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh/10**6
                    if "CAR_PHEV" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]/10**6
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GASOLINE"].sum()* 10**6 * gasoline_price_kwh/10**6
                    if "CAR_FC" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "H2"].sum()* 10**6 * h2_price_kwh
                        cout_prive_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "H2"].sum()* 10**6 * h2_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "H2"].sum()* 10**6 * h2_price_kwh/10**6
                    if "BUS_ELEC" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        cout_public_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]/10**6
                    if "BUS_DIESEL" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "DIESEL"].sum()* 10**6 * diesel_price_kwh
                        cout_public_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "DIESEL"].sum()* 10**6 * diesel_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "DIESEL"].sum()* 10**6 * diesel_price_kwh/10**6
                    if "BUS_HYDIESEL" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "DIESEL"].sum()* 10**6 * diesel_price_kwh
                        cout_public_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "DIESEL"].sum()* 10**6 * diesel_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "DIESEL"].sum()* 10**6 * diesel_price_kwh/10**6
                    if "BUS_FC" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "H2"].sum()* 10**6 * h2_price_kwh
                        cout_public_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "H2"].sum()* 10**6 * h2_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "H2"].sum()* 10**6 * h2_price_kwh/10**6
                    if "BUS_NG" in name:
                        non_active_road_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GAS"].sum()* 10**6 * gas_price_kwh
                        cout_public_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GAS"].sum()* 10**6 * gas_price_kwh
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "GAS"].sum()* 10**6 * gas_price_kwh/10**6
                    if "TRAMWAY_ELEC" in name:
                        railways_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        cout_public_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]/10**6
                    if "METRO" in name:
                        railways_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        cout_public_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]/10**6
                    if "TRAIN" in name:
                        railways_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        cout_public_op[j] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]
                        transport_costs[name][j, 2] -= [df1_bis, df2_bis, df3_bis][j].loc[[name in str(row) for row in [df1_bis, df2_bis, df3_bis][j]["Tech"]], "ELECTRICITY"].sum()* 10**6 * elec_price_per_kWh[j]/10**6
    non_active_road_op = non_active_road_op /10**6
    active_road_op = active_road_op /10**6
    railways_op = railways_op /10**6
    cout_public_op = cout_public_op /10**6
    cout_prive_op = cout_prive_op /10**6

    filename_1 = "C:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/Data/2050_scenario1_trends/Infrastructure_info.xlsx"
    data_infra1 = pd.read_excel(filename_1, engine='openpyxl')
    filename_2 = "C:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/Data/2050_scenario2_sobriety/Infrastructure_info.xlsx"
    data_infra2 = pd.read_excel(filename_2, engine='openpyxl')
    filename_3 = "C:/Users/Dam/Documents/memoire/Programs/EnergyScope-EnergyScope.py/Data/2050_scenario3_efficiency/Infrastructure_info.xlsx"
    data_infra3 = pd.read_excel(filename_3, engine='openpyxl')

    def annualisation(lifetime):
        i_rate = 0.015
        return i_rate * (1 + i_rate)**lifetime / (((1 + i_rate)**lifetime) - 1)
    
    for scenario_idx, data_infra in enumerate([data_infra1, data_infra2, data_infra3]):
        for i in range(len(data_infra)):
            if "Bike" in data_infra.iloc[i, 0]:
                active_road_inf_inv[scenario_idx] += data_infra.iloc[i, 1] * data_infra.iloc[i, 2] * annualisation(data_infra.iloc[i, 4]) /10**6
                active_road_inf_main[scenario_idx] += data_infra.iloc[i, 1] * data_infra.iloc[i, 3] /10**6
                bike_infra[scenario_idx][0] += data_infra.iloc[i, 1] * data_infra.iloc[i, 2] * annualisation(data_infra.iloc[i, 4]) /10**6
                bike_infra[scenario_idx][1] += data_infra.iloc[i, 1] * data_infra.iloc[i, 3] /10**6
            if "Motorcycle" in data_infra.iloc[i, 0]:
                non_active_road_inf_inv[scenario_idx] += data_infra.iloc[i, 2] * sum(results[j][scenario_idx + 1] for j in range(4, 8)) * transport_param["MOTORCYCLE"]["distance"] /10**6
                non_active_road_inf_main[scenario_idx] += data_infra.iloc[i, 3] * sum(results[j][scenario_idx + 1] for j in range(4, 8)) * transport_param["MOTORCYCLE"]["distance"] /10**6
                motorcycle_infra[scenario_idx][0] += data_infra.iloc[i, 2] * sum(results[j][scenario_idx + 1] for j in range(4, 8)) * transport_param["MOTORCYCLE"]["distance"] /10**6
                motorcycle_infra[scenario_idx][1] += data_infra.iloc[i, 3] * sum(results[j][scenario_idx + 1] for j in range(4, 8)) * transport_param["MOTORCYCLE"]["distance"] /10**6
            if "Car" in data_infra.iloc[i, 0]:
                non_active_road_inf_inv[scenario_idx] += data_infra.iloc[i, 2] * sum(results[j][scenario_idx + 1] for j in range(9, 23)) * transport_param["Car"]["distance"] /10**6
                non_active_road_inf_main[scenario_idx] += data_infra.iloc[i, 3] * sum(results[j][scenario_idx + 1] for j in range(9, 23)) * transport_param["Car"]["distance"] /10**6  
                car_infra[scenario_idx][0] += data_infra.iloc[i, 2] * sum(results[j][scenario_idx + 1] for j in range(9, 23)) * transport_param["Car"]["distance"] /10**6
                car_infra[scenario_idx][1] += data_infra.iloc[i, 3] * sum(results[j][scenario_idx + 1] for j in range(9, 23)) * transport_param["Car"]["distance"] /10**6          
            if "Bus" in data_infra.iloc[i, 0]:
                non_active_road_inf_inv[scenario_idx] += data_infra.iloc[i, 2] * sum(results[j][scenario_idx + 1] for j in range(-13, -4)) * transport_param["Bus"]["distance"] /10**6
                non_active_road_inf_main[scenario_idx] += data_infra.iloc[i, 3] * sum(results[j][scenario_idx + 1] for j in range(-13, -4)) * transport_param["Bus"]["distance"] /10**6
                bus_infra[scenario_idx][0] += data_infra.iloc[i, 2] * sum(results[j][scenario_idx + 1] for j in range(-13, -4)) * transport_param["Bus"]["distance"] /10**6
                bus_infra[scenario_idx][1] += data_infra.iloc[i, 3] * sum(results[j][scenario_idx + 1] for j in range(-13, -4)) * transport_param["Bus"]["distance"] /10**6
            if "Tram" in data_infra.iloc[i, 0]:
                railways_inf_inv[scenario_idx] += data_infra.iloc[i, 2] * results[-3][scenario_idx + 1] * transport_param["Tramway"]["distance"] /10**6
                railways_inf_main[scenario_idx] += data_infra.iloc[i, 3] * results[-3][scenario_idx + 1] * transport_param["Tramway"]["distance"] /10**6  
                tramway_infra[scenario_idx][0] += data_infra.iloc[i, 2] * results[-3][scenario_idx + 1] * transport_param["Tramway"]["distance"] /10**6
                tramway_infra[scenario_idx][1] += data_infra.iloc[i, 3] * results[-3][scenario_idx + 1] * transport_param["Tramway"]["distance"] /10**6    
            if "Metro" in data_infra.iloc[i, 0]:
                railways_inf_inv[scenario_idx] += data_infra.iloc[i, 2] * results[-2][scenario_idx + 1] * transport_param["Metro"]["distance"] /10**6
                railways_inf_main[scenario_idx] += data_infra.iloc[i, 3] * results[-2][scenario_idx + 1] * transport_param["Metro"]["distance"] /10**6
                metro_infra[scenario_idx][0] += data_infra.iloc[i, 2] * results[-2][scenario_idx + 1] * transport_param["Metro"]["distance"] /10**6
                metro_infra[scenario_idx][1] += data_infra.iloc[i, 3] * results[-2][scenario_idx + 1] * transport_param["Metro"]["distance"] /10**6   
            if "Train" in data_infra.iloc[i, 0]:
                railways_inf_inv[scenario_idx] += data_infra.iloc[i, 2] * results[-1][scenario_idx + 1] * transport_param["Train"]["distance"] /10**6
                railways_inf_main[scenario_idx] += data_infra.iloc[i, 3] * results[-1][scenario_idx + 1] * transport_param["Train"]["distance"] /10**6
                train_infra[scenario_idx][0] += data_infra.iloc[i, 2] * results[-1][scenario_idx + 1] * transport_param["Train"]["distance"] /10**6
                train_infra[scenario_idx][1] += data_infra.iloc[i, 3] * results[-1][scenario_idx + 1] * transport_param["Train"]["distance"] /10**6            
            '''
            if "number_trainstation" in data_infra.iloc[i, 0]:
                railways_inf_inv[scenario_idx] += data_infra.iloc[i, 1] * data_infra.iloc[i, 2] * annualisation(data_infra.iloc[i, 4]) /10**6
                railways_inf_main[scenario_idx] += data_infra.iloc[i, 1] * data_infra.iloc[i, 3] /10**6
            '''
     
    table = {
        "Category": ["Active road", "Non-active road", "Railways", "Total"],
        "Investment": [active_road_inv[2], non_active_road_inv[2], railways_inv[2], active_road_inv[2] + non_active_road_inv[2] + railways_inv[2]],
        "Maintenance": [active_road_main[2], non_active_road_main[2], railways_main[2], active_road_main[2] + non_active_road_main[2] + railways_main[2]],
        "Operation": [active_road_op[2], non_active_road_op[2], railways_op[2], active_road_op[2] + non_active_road_op[2] + railways_op[2]],
        "Infrastructure Investment": [active_road_inf_inv[2], non_active_road_inf_inv[2], railways_inf_inv[2], active_road_inf_inv[2] + non_active_road_inf_inv[2] + railways_inf_inv[2]],
        "Infrastructure Maintenance": [active_road_inf_main[2], non_active_road_inf_main[2], railways_inf_main[2], active_road_inf_main[2] + non_active_road_inf_main[2] + railways_inf_main[2]],
        "Total" : [active_road_inv[2] + active_road_main[2] + active_road_op[2] + active_road_inf_inv[2] + active_road_inf_main[2],
                     non_active_road_inv[2] + non_active_road_main[2] + non_active_road_op[2] + non_active_road_inf_inv[2] + non_active_road_inf_main[2],
                     railways_inv[2] + railways_main[2] + railways_op[2] + railways_inf_inv[2] + railways_inf_main[2],
                     active_road_inv[2] + active_road_main[2] + active_road_op[2] + active_road_inf_inv[2] + active_road_inf_main[2] +
                     non_active_road_inv[2] + non_active_road_main[2] + non_active_road_op[2] + non_active_road_inf_inv[2] + non_active_road_inf_main[2] +
                     railways_inv[2] + railways_main[2] + railways_op[2] + railways_inf_inv[2] + railways_inf_main[2]]
    }
    #print(tabulate.tabulate(table, headers="keys", tablefmt="grid", showindex=False))

    cout_public_inf_inv += railways_inf_inv + active_road_inf_inv + non_active_road_inf_inv - cout_prive_inf_inv
    cout_public_inf_main += railways_inf_main + active_road_inf_main + non_active_road_inf_main - cout_prive_inf_main

    table = {
        "Category": ["Private", "Public", "Total"],
        "Veh Inv" : [cout_prive_inv[2], cout_public_inv[2], cout_prive_inv[2] + cout_public_inv[2]],
        "Veh Main" : [cout_prive_main[2], cout_public_main[2], cout_prive_main[2] + cout_public_main[2]],
        "Veh Op" : [cout_prive_op[2], cout_public_op[2], cout_prive_op[2] + cout_public_op[2]],
        "Infr Inv" : [cout_prive_inf_inv[2], cout_public_inf_inv[2], cout_public_inf_inv[2] + cout_prive_inf_inv[2]],
        "Infr Main" : [cout_prive_inf_main[2], cout_public_inf_main[2], cout_public_inf_main[2] + cout_prive_inf_main[2]],
        "Total" : [cout_prive_inv[2] + cout_prive_main[2] + cout_prive_op[2] + cout_prive_inf_inv[2] + cout_prive_inf_main[2], cout_public_inf_inv[2] + cout_public_inf_main[2] + cout_public_op[2] + cout_public_inf_inv[2] + cout_public_main[2], cout_prive_inv[2] + cout_prive_main[2] + cout_prive_op[2] + cout_prive_inf_inv[2] + cout_prive_inf_main[2] + cout_public_inf_inv[2] + cout_public_inf_main[2] + cout_public_op[2] + cout_public_inf_inv[2] + cout_public_main[2]]
    }
    #print(tabulate.tabulate(table, headers="keys", tablefmt="grid", showindex=False))

    # Print a table with transport costs by type of transport and infrastructure costs for Scenario 0, 1, and 2
    transport_types = ["Bike", "Motorcycle", "Car", "Bus", "Tramway", "Metro", "Train"]

    for scenario_idx in range(3):  # Loop through Scenario 0, 1, and 2
        scenario = f"Scenario {scenario_idx + 1}"

        # Initialize the table data
        table_data = []

        for transport_type in transport_types:
            if transport_type == "Bike":
                inv = sum(transport_costs[name][scenario_idx, 0] for name in transport_technologies if "BIKE" in name)
                main = sum(transport_costs[name][scenario_idx, 1] for name in transport_technologies if "BIKE" in name)
                op = sum(transport_costs[name][scenario_idx, 2] for name in transport_technologies if "BIKE" in name)
                infrainv = bike_infra[scenario_idx][0]
                inframain = bike_infra[scenario_idx][1]
                charginginv = bike_charging[scenario_idx][0]
                chargingmain = bike_charging[scenario_idx][1]
            elif transport_type == "Motorcycle":
                inv = sum(transport_costs[name][scenario_idx, 0] for name in transport_technologies if "MOTORCYCLE" in name)
                main = sum(transport_costs[name][scenario_idx, 1] for name in transport_technologies if "MOTORCYCLE" in name)
                op = sum(transport_costs[name][scenario_idx, 2] for name in transport_technologies if "MOTORCYCLE" in name)
                infrainv = motorcycle_infra[scenario_idx][0]
                inframain = motorcycle_infra[scenario_idx][1]
                charginginv = motorcycle_charging[scenario_idx][0]
                chargingmain = motorcycle_charging[scenario_idx][1]
            elif transport_type == "Car":
                inv = sum(transport_costs[name][scenario_idx, 0] for name in transport_technologies if "CAR" in name)
                main = sum(transport_costs[name][scenario_idx, 1] for name in transport_technologies if "CAR" in name)
                op = sum(transport_costs[name][scenario_idx, 2] for name in transport_technologies if "CAR" in name)
                infrainv = car_infra[scenario_idx][0]
                inframain = car_infra[scenario_idx][1]
                charginginv = car_charging[scenario_idx][0]
                chargingmain = car_charging[scenario_idx][1]
            elif transport_type == "Bus":
                inv = sum(transport_costs[name][scenario_idx, 0] for name in transport_technologies if "BUS" in name)
                main = sum(transport_costs[name][scenario_idx, 1] for name in transport_technologies if "BUS" in name)
                op = sum(transport_costs[name][scenario_idx, 2] for name in transport_technologies if "BUS" in name)
                infrainv = bus_infra[scenario_idx][0]
                inframain = bus_infra[scenario_idx][1]
                charginginv = bus_charging[scenario_idx][0]
                chargingmain = bus_charging[scenario_idx][1]
            elif transport_type == "Tramway":
                inv = sum(transport_costs[name][scenario_idx, 0] for name in transport_technologies if "TRAMWAY" in name)
                main = sum(transport_costs[name][scenario_idx, 1] for name in transport_technologies if "TRAMWAY" in name)
                op = sum(transport_costs[name][scenario_idx, 2] for name in transport_technologies if "TRAMWAY" in name)
                infrainv = tramway_infra[scenario_idx][0]
                inframain = tramway_infra[scenario_idx][1]
                charginginv = tramway_charging[scenario_idx][0]
                chargingmain = tramway_charging[scenario_idx][1]
            elif transport_type == "Metro":
                inv = sum(transport_costs[name][scenario_idx, 0] for name in transport_technologies if "METRO" in name)
                main = sum(transport_costs[name][scenario_idx, 1] for name in transport_technologies if "METRO" in name)
                op = sum(transport_costs[name][scenario_idx, 2] for name in transport_technologies if "METRO" in name)
                infrainv = metro_infra[scenario_idx][0]
                inframain = metro_infra[scenario_idx][1]
                charginginv = metro_charging[scenario_idx][0]
                chargingmain = metro_charging[scenario_idx][1]
            elif transport_type == "Train":
                inv = sum(transport_costs[name][scenario_idx, 0] for name in transport_technologies if "TRAIN" in name)
                main = sum(transport_costs[name][scenario_idx, 1] for name in transport_technologies if "TRAIN" in name)
                op = sum(transport_costs[name][scenario_idx, 2] for name in transport_technologies if "TRAIN" in name)
                infrainv = train_infra[scenario_idx][0]
                inframain = train_infra[scenario_idx][1]
                charginginv = train_charging[scenario_idx][0]
                chargingmain = train_charging[scenario_idx][1]

            # Calculate the total cost for the transport type
            total_cost = inv + main + op + infrainv + inframain + charginginv + chargingmain

            # Append the row to the table data
            table_data.append([scenario, transport_type, inv, main, op, infrainv, inframain, charginginv, chargingmain, total_cost])

        # Add a row for the total sum of each cost type
        total_inv = sum(row[2] for row in table_data)
        total_main = sum(row[3] for row in table_data)
        total_op = sum(row[4] for row in table_data)
        total_infrainv = sum(row[5] for row in table_data)
        total_inframain = sum(row[6] for row in table_data)
        total_charginginv = sum(row[7] for row in table_data)
        total_chargingmain = sum(row[8] for row in table_data)
        total_sum = sum(row[9] for row in table_data)

        table_data.append(["Total", "-", total_inv, total_main, total_op, total_infrainv, total_inframain, total_charginginv, total_chargingmain, total_sum])

        # Print the table
        print(tabulate.tabulate(table_data, headers=["Scenario", "Transport Type", "Investment", "Maintenance", "Operation", "Infra Inv.", "Infra Main.", "Charging Inv.", "Charging Main.", "Total"], tablefmt="grid", floatfmt=".2f"))
    
    # Calculate private and public costs for all three scenarios
    private_costs = []
    public_costs = []

    for scenario_idx in range(3):
        # Private cost
        private_cost = (
            sum(transport_costs[name][scenario_idx, 0] + transport_costs[name][scenario_idx, 1] + transport_costs[name][scenario_idx, 2] for name in transport_technologies if "BIKE" in name) +  # Bike
            sum(transport_costs[name][scenario_idx, 0] + transport_costs[name][scenario_idx, 1] + transport_costs[name][scenario_idx, 2] for name in transport_technologies if "MOTORCYCLE" in name) +  # Motorcycle
            sum(transport_costs[name][scenario_idx, 0] + transport_costs[name][scenario_idx, 1] + transport_costs[name][scenario_idx, 2] for name in transport_technologies if "CAR" in name) +  # Car
            car_charging[scenario_idx][0] * 0.8 + car_charging[scenario_idx][1] * 0.8  # 80% Charging Inv. and Main. for Cars
        )
        private_costs.append(private_cost)

        # Public cost
        public_cost = (
            bike_infra[scenario_idx][0] + bike_infra[scenario_idx][1] + bike_charging[scenario_idx][0] + bike_charging[scenario_idx][1] +  # Bike Infra and Charging
            motorcycle_infra[scenario_idx][0] + motorcycle_infra[scenario_idx][1] + motorcycle_charging[scenario_idx][0] + motorcycle_charging[scenario_idx][1] +  # Motorcycle Infra and Charging
            car_infra[scenario_idx][0] + car_infra[scenario_idx][1] + car_charging[scenario_idx][0] * 0.2 + car_charging[scenario_idx][1] * 0.2 +  # Car Infra and 20% Charging
            sum(transport_costs[name][scenario_idx, 0] + transport_costs[name][scenario_idx, 1] + transport_costs[name][scenario_idx, 2] for name in transport_technologies if "BUS" in name) +  # Bus
            bus_infra[scenario_idx][0] + bus_infra[scenario_idx][1] + bus_charging[scenario_idx][0] + bus_charging[scenario_idx][1] +  # Bus Infra and Charging
            sum(transport_costs[name][scenario_idx, 0] + transport_costs[name][scenario_idx, 1] + transport_costs[name][scenario_idx, 2] for name in transport_technologies if "TRAMWAY" in name) +  # Tramway
            tramway_infra[scenario_idx][0] + tramway_infra[scenario_idx][1] + tramway_charging[scenario_idx][0] + tramway_charging[scenario_idx][1] +  # Tramway Infra and Charging
            sum(transport_costs[name][scenario_idx, 0] + transport_costs[name][scenario_idx, 1] + transport_costs[name][scenario_idx, 2] for name in transport_technologies if "METRO" in name) +  # Metro
            metro_infra[scenario_idx][0] + metro_infra[scenario_idx][1] + metro_charging[scenario_idx][0] + metro_charging[scenario_idx][1] +  # Metro Infra and Charging
            sum(transport_costs[name][scenario_idx, 0] + transport_costs[name][scenario_idx, 1] + transport_costs[name][scenario_idx, 2] for name in transport_technologies if "TRAIN" in name) +  # Train
            train_infra[scenario_idx][0] + train_infra[scenario_idx][1] + train_charging[scenario_idx][0] + train_charging[scenario_idx][1]  # Train Infra and Charging
        )
        public_costs.append(public_cost)

        print(f"Private cost for Scenario {scenario_idx + 1}: {private_cost:.2f} M€/year")
        print(f"Public cost for Scenario {scenario_idx + 1}: {public_cost:.2f} M€/year")

    # Calculate percentages
    total_costs = [private_costs[i] + public_costs[i] for i in range(3)]
    private_percentages = [private_costs[i] / total_costs[i] * 100 for i in range(3)]
    public_percentages = [public_costs[i] / total_costs[i] * 100 for i in range(3)]

    # Plot the percentages
    scenarios = ["S1: Trends", "S2: Sufficiency", "S3: Techno"]
    x = np.arange(len(scenarios))

    fig, ax = plt.subplots(figsize=(10, 6))
    private_costs_billion = [cost / 1000 for cost in private_costs]  # Convert to B€/year
    public_costs_billion = [cost / 1000 for cost in public_costs]  # Convert to B€/year

    # Plot the stackplot with actual values
    ax.barh(y, private_costs_billion, label="Private Cost", color="#1f77b4")
    ax.barh(y, public_costs_billion, left=private_costs_billion, label="Public Cost", color="#ff7f0e")

    # Add total amounts at the right of the bars
    for i in range(len(scenarios)):
        total_cost = private_costs_billion[i] + public_costs_billion[i]
        ax.text(total_cost + 0.5, y[i], f"{total_cost:.1f} $B€_{{2015}}/y$", va="center", fontsize=16, color="black")

    # Add labels and legend
    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, fontsize=16)
    # Remove x-tick labels
    ax.set_xticks([])

    ax.legend(fontsize=16, loc='lower center', bbox_to_anchor=(0.5, -0.2), frameon=False, ncol=2, columnspacing=0.7)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    # Add percentage labels on the bars
    for i in range(len(scenarios)):
        private_percentage = private_costs_billion[i] / (private_costs_billion[i] + public_costs_billion[i]) * 100
        public_percentage = public_costs_billion[i] / (private_costs_billion[i] + public_costs_billion[i]) * 100
        ax.text(private_costs_billion[i] / 2, y[i], f"{private_percentage:.1f}%", ha="center", va="center", color="black", fontsize=16)
        ax.text(private_costs_billion[i] + public_costs_billion[i] / 2, y[i], f"{public_percentage:.1f}%", ha="center", va="center", color="black", fontsize=16)

    plt.tight_layout()
    plt.show()
    # Create a figure with two subplots for investment and maintenance costs by scenario
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'wspace': 0.3})

    # Data preparation
    transport_types = ["Bike", "Motorcycle", "Car", "Bus", "Tramway", "Metro", "Train"]
    investment_data = [
        [bike_infra[i][0], motorcycle_infra[i][0], car_infra[i][0], bus_infra[i][0], tramway_infra[i][0], metro_infra[i][0], train_infra[i][0]]
        for i in range(3)
    ]
    maintenance_data = [
        [bike_infra[i][1], motorcycle_infra[i][1], car_infra[i][1], bus_infra[i][1], tramway_infra[i][1], metro_infra[i][1], train_infra[i][1]]
        for i in range(3)
    ]

    # Colors for each transport type
    colors = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494"]
    scenarios = ["S3: Techno", "S2: Sufficiency", "S1: Trends"]
    y = np.arange(len(scenarios))  # Keep the order for Scenario 1 on top

    # Plot investment costs as a stackplot
    left_investment = np.zeros(len(scenarios))
    for i, transport_type in enumerate(transport_types):
        values = [investment_data[j][i] / 1000 for j in range(3)]  # Divide values by 1000
        axes[0].barh(y, values[::-1], left=left_investment, color=colors[i], label=transport_type)
        left_investment += values[::-1]
    
    #write the investment costs after the barplot
    for j, total in enumerate(left_investment):
        axes[0].text(total + 0.1, y[j], f"{total:.1f} $B€_{{2015}}/y$", va='center', fontsize=16, color="black")

    axes[0].text(0.03, 1, "Investment", fontsize=20, ha="left", va="bottom", transform=axes[0].transAxes)
    axes[0].set_yticks(y)
    axes[0].set_yticklabels(scenarios, fontsize=16)
    axes[0].set_xticks([])  # Remove x-axis ticks for the first plot
    axes[0].set_xlim(0, 5)
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    axes[0].spines['bottom'].set_visible(False)
    axes[0].legend(fontsize=16, loc='lower center', bbox_to_anchor=(1.15, -0.2), frameon=False, ncol=8, columnspacing=0.7)

    # Plot maintenance costs as a stackplot
    left_maintenance = np.zeros(len(scenarios))
    for i, transport_type in enumerate(transport_types):
        values = [maintenance_data[j][i] / 1000 for j in range(3)]  # Divide values by 1000
        axes[1].barh(y, values[::-1], left=left_maintenance, color=colors[i], label=transport_type)
        left_maintenance += values[::-1]
    
    #write the total maintenance costs at the end of each bar
    for j, total in enumerate(left_maintenance):
        axes[1].text(total + 0.1, y[j], f"{total:.1f} $B€_{{2015}}/y$", va='center', fontsize=16, color="black")
    axes[1].text(0.03, 1, "Maintenance", fontsize=20, ha="left", va="bottom", transform=axes[1].transAxes)
    axes[1].set_yticks(y)
    axes[1].set_xticks([])  # Remove x-axis ticks for the second plot
    axes[1].set_yticklabels([])  # Remove y-axis labels for the second plot 
    axes[1].set_xlim(0, 5)   
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    axes[1].spines['bottom'].set_visible(False)
    

    # Adjust layout
    plt.tight_layout()
    plt.show()

    # Create three stacked bar plots: one for investment, one for maintenance, and one for operation
    fig, axes = plt.subplots(1, 3, figsize=(20, 6),gridspec_kw={'wspace': 0.9, 'width_ratios': [2.5, 1, 1]})

    # Data preparation
    scenarios = ["S1: Trends", "S2: Sufficiency", "S3: Techno"]
    y = np.arange(len(scenarios))[::-1]  # Reverse the order for proper display

    # Investment data
    investment_data = [
        [sum(transport_costs[name][i, 0] for name in transport_technologies if "BIKE" in name) for i in range(3)],  # Bike investments
        [sum(transport_costs[name][i, 0] for name in transport_technologies if "MOTORCYCLE" in name) for i in range(3)],  # Motorcycle investments
        [sum(transport_costs[name][i, 0] for name in transport_technologies if "CAR" in name) for i in range(3)],  # Car investments
        [sum(transport_costs[name][i, 0] for name in transport_technologies if "BUS" in name) for i in range(3)],  # Bus investments
        [sum(transport_costs[name][i, 0] for name in transport_technologies if "TRAMWAY" in name) for i in range(3)],  # Tram investments
        [sum(transport_costs[name][i, 0] for name in transport_technologies if "METRO" in name) for i in range(3)],  # Metro investments
        [sum(transport_costs[name][i, 0] for name in transport_technologies if "TRAIN" in name) for i in range(3)]   # Train investments
    ]

    # Maintenance data
    maintenance_data = [
        [sum(transport_costs[name][i, 1] for name in transport_technologies if "BIKE" in name) for i in range(3)],  # Bike maintenance
        [sum(transport_costs[name][i, 1] for name in transport_technologies if "MOTORCYCLE" in name) for i in range(3)],  # Motorcycle maintenance
        [sum(transport_costs[name][i, 1] for name in transport_technologies if "CAR" in name) for i in range(3)],  # Car maintenance
        [sum(transport_costs[name][i, 1] for name in transport_technologies if "BUS" in name) for i in range(3)],  # Bus maintenance
        [sum(transport_costs[name][i, 1] for name in transport_technologies if "TRAMWAY" in name) for i in range(3)],  # Tram maintenance
        [sum(transport_costs[name][i, 1] for name in transport_technologies if "METRO" in name) for i in range(3)],  # Metro maintenance
        [sum(transport_costs[name][i, 1] for name in transport_technologies if "TRAIN" in name) for i in range(3)]   # Train maintenance
    ]

    # Operation data
    operation_data = [
        [sum(transport_costs[name][i, 2] for name in transport_technologies if "BIKE" in name) for i in range(3)],  # Bike operation
        [sum(transport_costs[name][i, 2] for name in transport_technologies if "MOTORCYCLE" in name) for i in range(3)],  # Motorcycle operation
        [sum(transport_costs[name][i, 2] for name in transport_technologies if "CAR" in name) for i in range(3)],  # Car operation
        [sum(transport_costs[name][i, 2] for name in transport_technologies if "BUS" in name) for i in range(3)],  # Bus operation
        [sum(transport_costs[name][i, 2] for name in transport_technologies if "TRAMWAY" in name) for i in range(3)],  # Tram operation
        [sum(transport_costs[name][i, 2] for name in transport_technologies if "METRO" in name) for i in range(3)],  # Metro operation
        [sum(transport_costs[name][i, 2] for name in transport_technologies if "TRAIN" in name) for i in range(3)]   # Train operation
    ]

    # Labels and colors
    labels = ["Bike", "Motorcycle", "Car", "Bus", "Tram", "Metro", "Train"]
    colors = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f", "#e5c494"]  # Softer and more visually appealing colors

    # Plot investment
    left = np.zeros(len(scenarios))
    for i, (label, values) in enumerate(zip(labels, investment_data)):
        axes[0].barh(y, np.array(values) / 1000, left=left, label=label, color=colors[i])
        left += np.array(values) / 1000  # Convert to B€
    
    for j, total in enumerate(left):
        axes[0].text(total + 0.5, y[j], f"{total:.1f} $B€_{{2015}}/y$", va='center', fontsize=16, color="black")
    axes[0].text(0.03, 1, "Investments", fontsize=20, ha="left", va="bottom", transform=axes[0].transAxes)

    axes[0].set_yticks(y)
    axes[0].set_yticklabels(scenarios, fontsize=16)
    axes[0].legend(fontsize=16, loc="lower center", frameon=False, bbox_to_anchor=(1.5, -0.2), ncol=8, columnspacing=0.7)
    axes[0].set_xlim(0, 10) 
    axes[0].set_xticks([])
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    axes[0].spines['bottom'].set_visible(False)

    # Plot maintenance
    left = np.zeros(len(scenarios))
    for i, (label, values) in enumerate(zip(labels, maintenance_data)):
        axes[1].barh(y, np.array(values) / 1000, left=left, label=label, color=colors[i])
        left += np.array(values) / 1000  # Convert to B€
    
    for j, total in enumerate(left):
        axes[1].text(total + 0.5, y[j], f"{total:.1f} $B€_{{2015}}/y$", va='center', fontsize=16, color="black")
    
    axes[1].text(0.03, 1, "Maintenance", fontsize=20, ha="left", va="bottom", transform=axes[1].transAxes)
    axes[1].set_yticks(y)
    axes[1].set_yticklabels([])
    axes[1].set_xlim(0, 10)
    axes[1].set_xticks([])
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    axes[1].spines['bottom'].set_visible(False)



    # Plot operation
    left = np.zeros(len(scenarios))
    for i, (label, values) in enumerate(zip(labels, operation_data)):
        axes[2].barh(y, np.array(values) / 1000, left=left, label=label, color=colors[i])
        left += np.array(values) / 1000  # Convert to B€

    for j, total in enumerate(left):
        axes[2].text(total + 0.5, y[j], f"{total:.1f} $B€_{{2015}}/y$", va='center', fontsize=16, color="black")
    axes[2].set_yticks(y)
    axes[2].set_yticklabels([])
    axes[2].text(0.03, 1, "Operation", fontsize=20, ha="left", va="bottom", transform=axes[2].transAxes)
    axes[2].set_xlim(0, 10)
    axes[2].set_xticks([])
    axes[2].spines['top'].set_visible(False)
    axes[2].spines['right'].set_visible(False)
    axes[2].spines['bottom'].set_visible(False)


    # Adjust layout
    plt.tight_layout()
    plt.show()

    # Créer 3 plots alignés horizontalement
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), gridspec_kw={'wspace': 0.7, 'width_ratios': [2, 1, 1]})


    # Scénarios
    scenarios = ["S1: Trends", "S2: Sufficiency", "S3: Techno"]
    y = np.arange(len(scenarios))[::-1]  # Inverser l'ordre pour un affichage correct

    # Couleurs spécifiques pour chaque catégorie
    colors = ["#f28e2b", "#76b7b2", "#e15759"]  # Orange pour Vehicle, Vert pour Infrastructure, Rouge pour Charging

    # Plot des investissements
    left = np.zeros(len(scenarios))
    labels = ["Vehicle", "Network", "Charging/Fueling"]
    data = [
        [sum(transport_costs[name][i, 0] for name in transport_technologies) for i in range(3)],  # Vehicle investments
        [bike_infra[i][0] + motorcycle_infra[i][0] + car_infra[i][0] + bus_infra[i][0] + tramway_infra[i][0] + metro_infra[i][0] + train_infra[i][0] for i in range(3)],  # Transport infrastructure investments
        [bike_charging[i][0] + motorcycle_charging[i][0] + car_charging[i][0] + bus_charging[i][0] + tramway_charging[i][0] + metro_charging[i][0] + train_charging[i][0] for i in range(3)]  # Charging/Fueling investments
    ]
    print(data)
    for i, (label, values) in enumerate(zip(labels, data)):
        axes[0].barh(y, np.array(values)/1000, left=left, label=label, color=colors[i])
        left += np.array(values)/1000  # Convertir en B€

    # Ajouter les totaux à la fin de chaque scénario
    for j, total in enumerate(left):
        axes[0].text(total + 0.5, y[j], f"{total:.1f} $B€_{{2015}}/y$", va='center', fontsize=16, color="black")
    axes[0].text(0.03, 1, "Investments", fontsize=20, ha="left", va="bottom", transform=axes[0].transAxes)
    axes[0].set_yticks(y)
    axes[0].set_yticklabels(scenarios, fontsize=16)
    axes[0].set_xticks([])
    axes[0].legend(fontsize=16, loc="lower center", frameon=False, bbox_to_anchor=(0.9, -0.2), ncol=3, columnspacing=0.5)
    axes[0].set_xlim(0, 15)  # Limiter l'axe des x à 15
    axes[0].spines['top'].set_visible(False)
    axes[0].spines['right'].set_visible(False)
    axes[0].spines['bottom'].set_visible(False)

    # Plot de la maintenance
    left = np.zeros(len(scenarios))

    maintenance = [
        [sum(transport_costs[name][i, 1] for name in transport_technologies) for i in range(3)],  # Vehicle maintenance
        [bike_infra[i][1] + motorcycle_infra[i][1] + car_infra[i][1] + bus_infra[i][1] + tramway_infra[i][1] + metro_infra[i][1] + train_infra[i][1] for i in range(3)],  # Transport infrastructure maintenance
        [bike_charging[i][1] + motorcycle_charging[i][1] + car_charging[i][1] + bus_charging[i][1] + tramway_charging[i][1] + metro_charging[i][1] + train_charging[i][1] for i in range(3)]  # Charging/Fueling maintenance
    ]

    for i, (label, values) in enumerate(zip(labels, maintenance)):
        axes[1].barh(y, np.array(values)/1000, left=left, label=label, color=colors[i])
        left += np.array(values)/1000  # Convertir en B€
    
    # Ajouter les totaux à la fin de chaque scénario
    for j, total in enumerate(left):
        axes[1].text(total + 0.5, y[j], f"{total:.1f} $B€_{{2015}}/y$", va='center', fontsize=16, color="black")
    axes[1].text(0.03, 1, "Maintenance", fontsize=20, ha="left", va="bottom", transform=axes[1].transAxes)
    axes[1].set_yticks(y)
    axes[1].set_yticklabels([])  # Supprimer les noms des scénarios
    axes[1].set_xticks([])
    axes[1].set_xlim(0, 15)  # Limiter l'axe des x à 15
    axes[1].spines['top'].set_visible(False)
    axes[1].spines['right'].set_visible(False)
    axes[1].spines['bottom'].set_visible(False)

    # Plot de l'opération
    left = np.zeros(len(scenarios))
    # Données pour l'opération
    operation_bus = np.array([sum(transport_costs[name][i, 2] for name in transport_technologies if "BUS" in name) for i in range(3)])
    operation_rest = np.array([sum(transport_costs[name][i, 2] for name in transport_technologies if "BUS" not in name) for i in range(3)])
    
    # Convertir les valeurs en B€ avant de tracer
    operation_bus = operation_bus / 1000
    operation_rest = operation_rest / 1000

    # Ajouter les barres pour les bus et le reste
    axes[2].barh(y, operation_rest, left=left, label="Elec.", color = "#4e79a7")
    left += operation_rest
    axes[2].barh(y, operation_bus, left=left, label="Imp. Bio-diesel", color="#a9a9a9")
    left += operation_bus


    #put the total at the end of each scenario
    for j, total in enumerate(left):
        axes[2].text(total + 0.5, y[j], f"{total:.1f} $B€_{{2015}}/y$", va='center', fontsize=16, color="black")
    #put
    axes[2].text(0.03, 1, "Operation", fontsize=20, ha="left", va="bottom", transform=axes[2].transAxes)
    axes[2].set_yticks(y)
    axes[2].set_yticklabels([])  # Supprimer les noms des scénarios
    axes[2].set_xticks([])
    axes[2].set_xlim(0, 15)  # Limiter l'axe des x à 15
    axes[2].legend(fontsize=16, loc="lower center", frameon=False, bbox_to_anchor=(0.65, -0.2), ncol=3, columnspacing=0.5)
    axes[2].spines['top'].set_visible(False)
    axes[2].spines['right'].set_visible(False)
    axes[2].spines['bottom'].set_visible(False)

    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()

    # Créer un graphe bar stackplot pour chaque scénario
    scenarios = ["S1: Trends", "S2: Sufficiency", "S3: Techno"]
    categories = ["Private", "Public"]
    cost_components = ["Veh. inv.", "Veh. maint.", "Veh. op.", "Inf. inv.", "Inf. maint."]
    colors = ["blue", "orange", "green", "red", "purple", "brown"]

    '''    
    fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=False, gridspec_kw={'wspace': 0.2})

    for idx, ax in enumerate(axes):
        # Données pour le scénario actuel
        data = np.array([
            [cout_prive_inv[idx], cout_prive_main[idx], cout_prive_op[idx], cout_prive_inf_inv[idx], cout_prive_inf_main[idx]],
            [cout_public_inv[idx], cout_public_main[idx], cout_public_op[idx], cout_public_inf_inv[idx], cout_public_inf_main[idx]]
        ])
        # Diviser les données par 10**3 pour les convertir en B€/year
        data = data / 10**3

        # Calculer les pourcentages
        cout_prive = cout_prive_inv[idx] + cout_prive_main[idx] + cout_prive_op[idx] + cout_prive_inf_inv[idx] + cout_prive_inf_main[idx]
        cout_public = (cout_public_inv[idx] + cout_public_main[idx] + cout_public_op[idx] +
                       cout_public_inf_inv[idx] + cout_public_inf_main[idx])
        cout_prive_percent = cout_prive / (cout_prive + cout_public) * 100
        cout_public_percent = cout_public / (cout_prive + cout_public) * 100

        # Tracer les barres de type stack plot
        x = np.arange(len(categories))
        width = 0.5
        for i, (cost, color) in enumerate(zip(cost_components, colors)):
            ax.bar(x, data[:, i], width, label=cost, color=color, bottom=np.sum(data[:, :i], axis=1))

        # Ajouter des lignes horizontales tous les 2.5
        ax.set_yticks(np.arange(0, 20, 2.5))
        for i in np.arange(0, 17.5, 2.5):
            ax.axhline(y=i, color='grey', linestyle='--', linewidth=0.5)

        # Labels et mise en forme
        ax.set_title(scenarios[idx], fontsize=16)
        ax.set_xticks(x)
        ax.set_xticklabels(categories, fontsize=16)
        if idx == 0:
            ax.set_ylabel("Cost [B€/year]", fontsize=16)

        # Ajouter les pourcentages au-dessus des barres
        total_costs = np.sum(data, axis=1)
        for i, total in enumerate(total_costs):
            ax.text(i, total + 0.2, f"{[cout_prive_percent, cout_public_percent][i]:.1f}%", ha='center', fontsize=16, color="black")

        # Ajustements de style
        ax.tick_params(axis="y", labelsize=12)

        #si jamais second graphe mettre la légende en bas
        if idx == 1:
            ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), fontsize=16, ncol=5, frameon=False)
            ax.text(0.5, 1.1, "Private vs Public Transport Costs", fontsize=20, ha='center', va='center', transform=ax.transAxes)
    plt.tight_layout()
    plt.show()

    # Données
    categories = ["Act-Road", "Non-Act-Road", "Rail"]
    cost_components = ["Veh. inv.", "Veh. maint.", "Veh. op.", "Inf. inv.", "Inf. maint.", "Total"]
    scenarios = ["S1: Trends", "S2: Sufficiency", "S3: Techno"]

    # Valeurs des coûts pour chaque scénario
    data_scenarios = [
        np.array([
            [non_active_road_inv[0], non_active_road_main[0], non_active_road_op[0], non_active_road_inf_inv[0], non_active_road_inf_main[0], 
            non_active_road_inv[0] + non_active_road_main[0] + non_active_road_op[0] + non_active_road_inf_inv[0] + non_active_road_inf_main[0]],
            [active_road_inv[0], active_road_main[0], active_road_op[0], active_road_inf_inv[0], active_road_inf_main[0], 
            active_road_inv[0] + active_road_main[0] + active_road_op[0] + active_road_inf_inv[0] + active_road_inf_main[0]],
            [railways_inv[0], railways_main[0], railways_op[0], railways_inf_inv[0], railways_inf_main[0], 
            railways_inv[0] + railways_main[0] + railways_op[0] + railways_inf_inv[0] + railways_inf_main[0]]
        ]),
        np.array([
            [non_active_road_inv[1], non_active_road_main[1], non_active_road_op[1], non_active_road_inf_inv[1], non_active_road_inf_main[1], 
            non_active_road_inv[1] + non_active_road_main[1] + non_active_road_op[1] + non_active_road_inf_inv[1] + non_active_road_inf_main[1]],
            [active_road_inv[1], active_road_main[1], active_road_op[1], active_road_inf_inv[1], active_road_inf_main[1], 
            active_road_inv[1] + active_road_main[1] + active_road_op[1] + active_road_inf_inv[1] + active_road_inf_main[1]],
            [railways_inv[1], railways_main[1], railways_op[1], railways_inf_inv[1], railways_inf_main[1], 
            railways_inv[1] + railways_main[1] + railways_op[1] + railways_inf_inv[1] + railways_inf_main[1]]
        ]),
        np.array([
            [non_active_road_inv[2], non_active_road_main[2], non_active_road_op[2], non_active_road_inf_inv[2], non_active_road_inf_main[2], 
            non_active_road_inv[2] + non_active_road_main[2] + non_active_road_op[2] + non_active_road_inf_inv[2] + non_active_road_inf_main[2]],
            [active_road_inv[2], active_road_main[2], active_road_op[2], active_road_inf_inv[2], active_road_inf_main[2], 
            active_road_inv[2] + active_road_main[2] + active_road_op[2] + active_road_inf_inv[2] + active_road_inf_main[2]],
            [railways_inv[2], railways_main[2], railways_op[2], railways_inf_inv[2], railways_inf_main[2], 
            railways_inv[2] + railways_main[2] + railways_op[2] + railways_inf_inv[2] + railways_inf_main[2]]
        ])
    ]

    # Diviser les données par 10**3
    data_scenarios = [data / 10**3 for data in data_scenarios]
    # Paramètres du graphique
    x = np.arange(len(categories))
    width = 0.12
    colors = ["blue", "orange", "green", "red", "purple", "brown"]

    fig, axes = plt.subplots(1, 3, figsize=(18, 6), sharey=False, gridspec_kw={'wspace': 0.2})

    for idx, ax in enumerate(axes):
        data = data_scenarios[idx]
        # Tracer les barres
        for i, (cost, color) in enumerate(zip(cost_components, colors)):
            ax.bar(x + (i - 2.5) * width, data[:, i], width, label=cost, color=color, bottom=np.sum(data[:, :i], axis=1))

        # Mettre des hbar tous les 500
        ax.set_yticks(np.arange(0, 27.5, 2.5))
        # Mettre une ligne horizontale au même endroit que le yticks
        for i in np.arange(0, 27.5, 2.5):
            ax.axhline(y=i, color='grey', linestyle='--', linewidth=0.5)

        # Labels et mise en forme
        ax.set_title(scenarios[idx], fontsize=16)
        ax.set_xticks(x)
        ax.set_xticklabels(categories, fontsize=14)
        if idx == 0:
            ax.set_ylabel("Cost [B€/year]", fontsize=14)

        # Ajustements de style
        ax.tick_params(axis="y", labelsize=12)

        #si jamais second graphe mettre la légende en bas
        if idx == 1:
            ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.2), fontsize=14, ncol=5, frameon=False)
            ax.text(0.5, 1.1, "Transport Costs by category", fontsize=18, ha='center', va='center', transform=ax.transAxes)
    plt.tight_layout()
    plt.show()
    '''
if consumptionmobility:
    list_energy = ['ELECTRICITY', 'DIESEL']
    list_energy_display_name = ['Electricity', 'Imp. Bio-Diesel','Imp. Re. Gas', "Imp. Re. H2", 'Imp. Bio-Ethanol']
    colorsmob = ['#1f77b4', '#dcdcdc', '#ffd700', '#ff00ff', '#ffffff']
    df1 = pd.read_csv(os.path.join(path1, "year_balance.txt"), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, "year_balance.txt"), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, "year_balance.txt"), sep=r'\s+', engine='python')

    # Initialiser les tableaux avec des zéros
    mobility_scenario_1 = np.zeros(len(list_energy))
    mobility_scenario_2 = np.zeros(len(list_energy))
    mobility_scenario_3 = np.zeros(len(list_energy))

    # Parcourir la liste des énergies
    for i in range(len(list_energy)):
        # Ajouter les valeurs pour les technologies de transport
        for j in range(len(df1)):
            # Vérifier si la technologie est dans la liste transport_technologies
            if df1["Tech"][j] in transport_technologies.keys():
                if transport_technologies[df1["Tech"][j]]["energy"] == list_energy[i]:
                    mobility_scenario_1[i] -= df1[list_energy[i]][j]/1000
                    mobility_scenario_2[i] -= df2[list_energy[i]][j]/1000
                    mobility_scenario_3[i] -= df3[list_energy[i]][j]/1000
                if transport_technologies[df1["Tech"][j]]["energy_bis"] == list_energy[i]:
                    mobility_scenario_1[i] -= df1[list_energy[i]][j]/1000
                    mobility_scenario_2[i] -= df2[list_energy[i]][j]/1000
                    mobility_scenario_3[i] -= df3[list_energy[i]][j]/1000

    # Print in a table format
    table = {
        "Energy": list_energy_display_name + ["Total"],
        "Scenario 1": list(mobility_scenario_1) + [mobility_scenario_1.sum()],
        "Scenario 2": list(mobility_scenario_2) + [mobility_scenario_2.sum()],
        "Scenario 3": list(mobility_scenario_3) + [mobility_scenario_3.sum()],
        "Total": [mobility_scenario_1.sum(), mobility_scenario_2.sum(), mobility_scenario_3.sum(), (mobility_scenario_1 + mobility_scenario_2 + mobility_scenario_3).sum()]
    }
    print(tabulate.tabulate(table, headers="keys", tablefmt="grid", showindex=False))
    # Plotting the data
    fig, ax = plt.subplots(figsize=(10, 6))
    scenarios = ["S3 : Techno", "S2 : Sufficiency", "S1 : Trends"]
    y = np.arange(len(scenarios))  # Positions des scénarios sur l'axe y

    # Initialiser les barres empilées
    left_scenario_1 = np.zeros(len(scenarios))
    left_scenario_2 = np.zeros(len(scenarios))
    left_scenario_3 = np.zeros(len(scenarios))

    # Ajouter les ressources au graphique
    for i, resource in enumerate(list_energy):
        display_name = list_energy_display_name[i]
        color = None
        for tech, tech_info in transport_technologies.items():
            if tech_info["energy"] == resource:
                #look in list_energy the same name as tech_info["energy"] and take the same index place in colorsmob
                color = colorsmob[i] 

        # Only plot if at least one scenario has a value >= 1
        if mobility_scenario_1[i] >= 1 or mobility_scenario_2[i] >= 1 or mobility_scenario_3[i] >= 1:
            # Ajouter les barres pour chaque scénario
            ax.barh(scenarios[0], mobility_scenario_3[i], left=left_scenario_3[0], color=color, label=display_name)
            ax.barh(scenarios[1], mobility_scenario_2[i], left=left_scenario_2[1], color=color, label=display_name)
            ax.barh(scenarios[2], mobility_scenario_1[i], left=left_scenario_1[2], color=color, label=display_name)

            # Mettre à jour les bases pour empiler les barres
            left_scenario_1[2] += mobility_scenario_1[i]
            left_scenario_2[1] += mobility_scenario_2[i]
            left_scenario_3[0] += mobility_scenario_3[i]
        else:
            # Plot zero bars so all labels appear
            ax.barh(scenarios[0], 0, left=left_scenario_3[0], color=color, label=display_name)
            ax.barh(scenarios[1], 0, left=left_scenario_2[1], color=color, label=display_name)
            ax.barh(scenarios[2], 0, left=left_scenario_1[2], color=color, label=display_name)

    # Configurer les axes et les étiquettes
    ax.set_yticks(np.arange(len(scenarios)))
    ax.set_yticklabels(scenarios, fontsize=16)  # Toujours afficher Scenario 1 en premier

    ax.set_xlabel("Energy consumption [TWh]", fontsize=16)
    #ax.set_title("Mobility energy consumption", fontsize=20)
    # faire que le max de x soit 1.1 par rapport à la valeur max de la barre
    max_value = max(np.sum(mobility_scenario_1), np.sum(mobility_scenario_2), np.sum(mobility_scenario_3))
    ax.set_xlim(0, 1.1 * max_value)  # Ajuster la limite de l'axe x
    # Ajouter les xticks
    ax.tick_params(axis='x', labelsize=16)
    # Ajouter une légende
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Éviter les doublons dans la légende
    ax.legend(by_label.values(), by_label.keys(), fontsize=16, loc="center left", bbox_to_anchor=(1, 0.5),frameon=False)

    ax.spines['top'].set_visible(False)  # Supprimer la bordure supérieure
    ax.spines['right'].set_visible(False)  # Supprimer la bordure droite
    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()
 
if shareofelecprod:
    df1 = pd.read_csv(os.path.join(path1, "year_balance.txt"), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, "year_balance.txt"), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, "year_balance.txt"), sep=r'\s+', engine='python')

    # Créer un tableau pour chaque scénario
    elec_scenario_1 = np.array([])
    elec_scenario_2 = np.array([])
    elec_scenario_3 = np.array([])

    # Ajouter les valeurs pour les technologies de production d'électricité
    for i in range(len(df1)):
        if df1["Tech"][i] in ELEC_TECHNO.keys():
            elec_scenario_1 = np.append(elec_scenario_1, df1["ELECTRICITY"][i])
            elec_scenario_2 = np.append(elec_scenario_2, df2["ELECTRICITY"][i])
            elec_scenario_3 = np.append(elec_scenario_3, df3["ELECTRICITY"][i])

    # Filtrer les ressources avec des valeurs non nulles pour au moins un scénario
    valid_resources = []
    elec_scenario_1_filtered = []
    elec_scenario_2_filtered = []
    elec_scenario_3_filtered = []

    for i, resource in enumerate(ELEC_TECHNO.keys()):
        value_scenario_1 = elec_scenario_1[i] if i < len(elec_scenario_1) else 0
        value_scenario_2 = elec_scenario_2[i] if i < len(elec_scenario_2) else 0
        value_scenario_3 = elec_scenario_3[i] if i < len(elec_scenario_3) else 0

        # Inclure uniquement les ressources avec des valeurs non nulles
        if value_scenario_1 > 1 or value_scenario_2 > 1 or value_scenario_3 > 1:
            valid_resources.append(resource)
            elec_scenario_1_filtered.append(value_scenario_1)
            elec_scenario_2_filtered.append(value_scenario_2)
            elec_scenario_3_filtered.append(value_scenario_3)


    # Convertir les données filtrées en tableaux numpy
    elec_scenario_1_filtered = np.array(elec_scenario_1_filtered) / 1000
    elec_scenario_2_filtered = np.array(elec_scenario_2_filtered) / 1000
    elec_scenario_3_filtered = np.array(elec_scenario_3_filtered) / 1000

    
    # Création du stacked bar plot
    fig, ax = plt.subplots(figsize=(10, 6))

    scenarios = ["S3 : Techno", "S2 : Sufficiency", "S1 : Trends"]
    y = np.arange(len(scenarios))  # Positions des scénarios sur l'axe y

    # Initialiser les barres empilées
    left_1 = np.zeros(len(y))
    left_2 = np.zeros(len(y))
    left_3 = np.zeros(len(y))

    # Réorganiser les ressources pour que "Ammonia" soit en dernière position
    reordered_resources = [res for res in valid_resources if res != "CCGT_AMMONIA" and res != "IND_COGEN_GAS" and res != "ELECTRICITY"]
    if "ELECTRICITY" in valid_resources:
        reordered_resources.append("ELECTRICITY")
    if "CCGT_AMMONIA" in valid_resources:
        reordered_resources.append("CCGT_AMMONIA")
    if "IND_COGEN_GAS" in valid_resources:
        reordered_resources.append("IND_COGEN_GAS")

    # Ajouter les ressources au graphique
    for resource in reordered_resources:
        i = valid_resources.index(resource)
        color = ELEC_TECHNO[resource]["color"]
        display_name = ELEC_TECHNO[resource]["display_name"]

        # Ajouter les barres pour chaque scénario
        ax.barh(y[0], elec_scenario_3_filtered[i], left=left_3[0], color=color, label=display_name)
        ax.barh(y[1], elec_scenario_2_filtered[i], left=left_2[1], color=color, label=display_name)
        ax.barh(y[2], elec_scenario_1_filtered[i], left=left_1[2], color=color, label=display_name)


        # Mettre à jour les bases pour empiler les barres
        left_1[2] += elec_scenario_1_filtered[i]
        left_2[1] += elec_scenario_2_filtered[i]
        left_3[0] += elec_scenario_3_filtered[i]

    # Configurer les axes et les étiquettes
    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, fontsize=16)  # Toujours afficher Scenario 1 en premier
    ax.tick_params(axis="x", labelsize=16)
    ax.set_xlabel("Electricity [TWh]", fontsize=16)

    ax.spines['top'].set_visible(False)  # Supprimer la bordure supérieure
    ax.spines['right'].set_visible(False)  # Supprimer la bordure droite
    # Ajouter une légende
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Éviter les doublons dans la légende
    ax.legend(by_label.values(), by_label.keys(), fontsize=16, loc="center left",frameon = False, bbox_to_anchor=(1.3, 0.5), ncol=1)


    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()

    #print the table
    table = {
        "Energy": valid_resources,
        "Scenario 1": list(elec_scenario_1_filtered),
        "Scenario 2": list(elec_scenario_2_filtered),
        "Scenario 3": list(elec_scenario_3_filtered)
    }
    print(tabulate.tabulate(table, headers="keys", tablefmt="grid", showindex=False))

if shareofLHTheat:
    filename = "year_balance.txt"

    # Charger les données pour chaque scénario
    df1 = pd.read_csv(os.path.join(path1, filename), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, filename), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, filename), sep=r'\s+', engine='python')

    # Initialiser les tableaux pour les scénarios
    heat_scenario_1_DHN = np.array([])
    heat_scenario_1_DEC = np.array([])
    heat_scenario_2_DHN = np.array([])
    heat_scenario_2_DEC = np.array([])
    heat_scenario_3_DHN = np.array([])
    heat_scenario_3_DEC = np.array([])

    # Ajouter les valeurs pour les technologies de chauffage basse température HEAT_LOW_T_DHN	HEAT_LOW_T_DECEN
    for i in range(len(df1)):
        if df1["Tech"][i] in LT_HEAT_TECHNO.keys():
            if "DHN" in df1["Tech"][i]:
                heat_scenario_1_DHN = np.append(heat_scenario_1_DHN, df1["HEAT_LOW_T_DHN"][i])
                heat_scenario_2_DHN = np.append(heat_scenario_2_DHN, df2["HEAT_LOW_T_DHN"][i])
                heat_scenario_3_DHN = np.append(heat_scenario_3_DHN, df3["HEAT_LOW_T_DHN"][i])
            else:
                heat_scenario_1_DEC = np.append(heat_scenario_1_DEC, df1["HEAT_LOW_T_DECEN"][i])
                heat_scenario_2_DEC = np.append(heat_scenario_2_DEC, df2["HEAT_LOW_T_DECEN"][i])
                heat_scenario_3_DEC = np.append(heat_scenario_3_DEC, df3["HEAT_LOW_T_DECEN"][i])

    #combiner les deux tableaux pour avoir un seul tableau par scenario en commencant par DHN
    heat_scenario_1 = np.concatenate((heat_scenario_1_DHN, heat_scenario_1_DEC))
    heat_scenario_2 = np.concatenate((heat_scenario_2_DHN, heat_scenario_2_DEC))
    heat_scenario_3 = np.concatenate((heat_scenario_3_DHN, heat_scenario_3_DEC))

    # Filtrer les ressources avec des valeurs non nulles pour au moins un scénario
    valid_resources = []
    heat_scenario_1_filtered = []
    heat_scenario_2_filtered = []
    heat_scenario_3_filtered = []

    for i, resource in enumerate(LT_HEAT_TECHNO.keys()):
        value_scenario_1 = heat_scenario_1[i] if i < len(heat_scenario_1) else 0
        value_scenario_2 = heat_scenario_2[i] if i < len(heat_scenario_2) else 0
        value_scenario_3 = heat_scenario_3[i] if i < len(heat_scenario_3) else 0

        # Inclure uniquement les ressources avec des valeurs non nulles
        if value_scenario_1 > 1 or value_scenario_2 > 1 or value_scenario_3 > 1:
            valid_resources.append(resource)
            heat_scenario_1_filtered.append(value_scenario_1)
            heat_scenario_2_filtered.append(value_scenario_2)
            heat_scenario_3_filtered.append(value_scenario_3)

    # Convertir les données filtrées en tableaux numpy
    heat_scenario_1_filtered = np.array(heat_scenario_1_filtered) / 1000
    heat_scenario_2_filtered = np.array(heat_scenario_2_filtered) / 1000
    heat_scenario_3_filtered = np.array(heat_scenario_3_filtered) / 1000
    # Création du stacked bar plot
    fig, ax = plt.subplots(figsize=(10, 6))

    scenarios = ["S3 : Techno", "S2 : Sufficiency", "S1 : Trends"]
    y = np.arange(len(scenarios))  # Positions des scénarios sur l'axe y

    # Initialiser les barres empilées
    left_1 = np.zeros(len(y))
    left_2 = np.zeros(len(y))
    left_3 = np.zeros(len(y))

    # Réorganiser les ressources pour que "Gas" et "Resistor" soient en dernière position
    reordered_resources = [res for res in valid_resources if res not in ["IND_BOILER_GAS", "IND_DIRECT_ELEC"]]
    if "IND_BOILER_GAS" in valid_resources:
        reordered_resources.append("IND_BOILER_GAS")
    if "IND_DIRECT_ELEC" in valid_resources:
        reordered_resources.append("IND_DIRECT_ELEC")

    # Ajouter les ressources au graphique
    for resource in reordered_resources:
        i = valid_resources.index(resource)
        color = LT_HEAT_TECHNO[resource]["color"]
        display_name = LT_HEAT_TECHNO[resource]["display_name"]

        # Ajouter les barres pour chaque scénario
        ax.barh(y[2], heat_scenario_1_filtered[i], left=left_1[2], color=color, label=display_name)
        ax.barh(y[1], heat_scenario_2_filtered[i], left=left_2[1], color=color, label=display_name)
        ax.barh(y[0], heat_scenario_3_filtered[i], left=left_3[0], color=color, label=display_name)

        # Mettre à jour les bases pour empiler les barres
        left_1[2] += heat_scenario_1_filtered[i]
        left_2[1] += heat_scenario_2_filtered[i]
        left_3[0] += heat_scenario_3_filtered[i]

    # Configurer les axes et les étiquettes
    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, fontsize=16)  # Toujours afficher Scenario 1 en premier
    ax.set_xlabel("Heat [TWh]", fontsize=16)
    #ax.set_title("High temperature technology", fontsize=18)
    ax.tick_params(axis="x", labelsize=16)

    ax.spines['top'].set_visible(False)  # Supprimer la bordure supérieure
    ax.spines['right'].set_visible(False)  # Supprimer la bordure droite
    # Ajouter une légende
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Éviter les doublons dans la légende
    ax.legend(by_label.values(), by_label.keys(), fontsize=16, loc="center left", frameon=False, bbox_to_anchor=(1, 0.5), ncol=1)
    ax.spines['right'].set_visible(False)  # Supprimer la bordure droite
    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()

if shareofHTheat:
    filename = "year_balance.txt"

    df1 = pd.read_csv(os.path.join(path1, filename), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, filename), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, filename), sep=r'\s+', engine='python')

    #si jamais le nom de la colonne est HEAT_HIGH_T et de la ligne est ds HT_HEAT_TECHNO, on la mets dans une liste qu'on va stackplot par scenario

    heat_scenario_1 = np.array([])
    heat_scenario_2 = np.array([])
    heat_scenario_3 = np.array([])

    for i in range(len(df1)):
        if df1["Tech"][i] in HT_HEAT_TECHNO.keys():
            heat_scenario_1 = np.append(heat_scenario_1, df1["HEAT_HIGH_T"][i])
            if df1["HEAT_HIGH_T"][i]> 1: 
                print(df1["Tech"][i])
            heat_scenario_2 = np.append(heat_scenario_2, df2["HEAT_HIGH_T"][i])
            heat_scenario_3 = np.append(heat_scenario_3, df3["HEAT_HIGH_T"][i])
    # Filtrer les ressources avec des valeurs non nulles pour au moins un scénario
    valid_resources = []
    heat_scenario_1_filtered = []
    heat_scenario_2_filtered = []
    heat_scenario_3_filtered = []

    for i, resource in enumerate(HT_HEAT_TECHNO.keys()):
        value_scenario_1 = heat_scenario_1[i] if i < len(heat_scenario_1) else 0
        value_scenario_2 = heat_scenario_2[i] if i < len(heat_scenario_2) else 0
        value_scenario_3 = heat_scenario_3[i] if i < len(heat_scenario_3) else 0

        # Inclure uniquement les ressources avec des valeurs non nulles
        if value_scenario_1 > 1 or value_scenario_2 > 1 or value_scenario_3 > 1:
            valid_resources.append(resource)
            heat_scenario_1_filtered.append(value_scenario_1)
            heat_scenario_2_filtered.append(value_scenario_2)
            heat_scenario_3_filtered.append(value_scenario_3)
        
    
    # Convertir les données filtrées en tableaux numpy
    heat_scenario_1_filtered = np.array(heat_scenario_1_filtered)/1000
    heat_scenario_2_filtered = np.array(heat_scenario_2_filtered)/1000
    heat_scenario_3_filtered = np.array(heat_scenario_3_filtered)/1000
    print(sum(heat_scenario_1_filtered), sum(heat_scenario_2_filtered), sum(heat_scenario_3_filtered))

    # Création du stacked bar plot
    fig, ax = plt.subplots(figsize=(10, 6))

    scenarios = [ "S3 : Techno", "S2 : Sufficiency","S1 : Trends"]
    y = np.arange(len(scenarios))  # Positions des scénarios sur l'axe y

    # Initialiser les barres empilées
    left_1 = np.zeros(len(y))
    left_2 = np.zeros(len(y))
    left_3 = np.zeros(len(y))
    


    # Réorganiser les ressources pour que "Gas" et "Resistor" soient en dernière position
    reordered_resources = [res for res in valid_resources if res not in ["IND_BOILER_GAS", "IND_DIRECT_ELEC", "IND_COGEN_GAS"]]
    if "IND_BOILER_GAS" in valid_resources:
        reordered_resources.append("IND_BOILER_GAS")
    if "IND_DIRECT_ELEC" in valid_resources:
        reordered_resources.append("IND_DIRECT_ELEC")
    if "IND_COGEN_GAS" in valid_resources:
        reordered_resources.append("IND_COGEN_GAS")

    # Ajouter les ressources au graphique
    for resource in reordered_resources:
        i = valid_resources.index(resource)
        color = HT_HEAT_TECHNO[resource]["color"]
        display_name = HT_HEAT_TECHNO[resource]["display_name"]

        # Ajouter les barres pour chaque scénario
        ax.barh(y[2], heat_scenario_1_filtered[i], left=left_1[2], color=color, label=display_name)
        ax.barh(y[1], heat_scenario_2_filtered[i], left=left_2[1], color=color, label=display_name)
        ax.barh(y[0], heat_scenario_3_filtered[i], left=left_3[0], color=color, label=display_name)

        # Mettre à jour les bases pour empiler les barres
        left_1[2] += heat_scenario_1_filtered[i]
        left_2[1] += heat_scenario_2_filtered[i]
        left_3[0] += heat_scenario_3_filtered[i]

    # Configurer les axes et les étiquettes
    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, fontsize=16)  # Toujours afficher Scenario 1 en premier
    ax.set_xlabel("Heat [TWh]", fontsize=16)
    #ax.set_title("High temperature technology", fontsize=18)
    ax.tick_params(axis="x", labelsize=16)

    ax.spines['top'].set_visible(False)  # Supprimer la bordure supérieure
    ax.spines['right'].set_visible(False)  # Supprimer la bordure droite
    # Ajouter une légende
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Éviter les doublons dans la légende
    ax.legend(by_label.values(), by_label.keys(), fontsize=16, frameon=False, ncol=1, loc="center left", bbox_to_anchor=(1, 0.5))

    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()

    table = {
        "Energy": valid_resources + ["Total"],
        "Scenario 1": list(heat_scenario_1_filtered) + [heat_scenario_1_filtered.sum()],
        "Scenario 2": list(heat_scenario_2_filtered) + [heat_scenario_2_filtered.sum()],
        "Scenario 3": list(heat_scenario_3_filtered) + [heat_scenario_3_filtered.sum()]
    }
    print(tabulate.tabulate(table, headers="keys", tablefmt="grid", showindex=False))
if shareoflocal :
    Share_scenario_1 = np.array([0,0])
    Share_scenario_2 = np.array([0,0])
    Share_scenario_3 = np.array([0,0])
    filename = "resources_breakdown.txt"
    #open the file in a dataframe
    df1 = pd.read_csv(os.path.join(path1, filename), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, filename), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, filename), sep=r'\s+', engine='python')

    #on addition les energies qui sont importées et par importées de chaque scenarios
    for i in range(len(df1)):
        if df1["Name"][i] in ressource.keys():
            #si jamais dans display name il y a importé ou importée on additionne la valeur à la valeur de l'array
            if "Imp." in ressource[df1["Name"][i]]["display_name"] or "Imp." in ressource[df1["Name"][i]]["display_name"]:
                Share_scenario_1[0] += df1["Used"][i]
                Share_scenario_2[0] += df2["Used"][i]
                Share_scenario_3[0] += df3["Used"][i]
            else:
                Share_scenario_1[1] += df1["Used"][i]
                Share_scenario_2[1] += df2["Used"][i]
                Share_scenario_3[1] += df3["Used"][i]
    print(Share_scenario_1.sum(), Share_scenario_2.sum(), Share_scenario_3.sum())
    # Création du stackplot pour les parts locales et importées
    fig, ax = plt.subplots(figsize=(10, 6))

    # Données pour les stackplots
    scenarios = ["S3 : Techno", "S2 : Sufficiency", "S1 : Trends"]
    y = np.arange(len(scenarios))  # Positions des scénarios sur l'axe y
    imported = [Share_scenario_3[0], Share_scenario_2[0], Share_scenario_1[0]]
    endogenous = [Share_scenario_3[1], Share_scenario_2[1], Share_scenario_1[1]]
    #divieser par 1000 pour avoir les valeurs en TWh
    imported = np.array(imported)/1000
    endogenous = np.array(endogenous)/1000
    # Tracer le stackplot
    ax.barh(y, endogenous, label="Endogenous", color="#dcdcdc")   # Vert foncé
    ax.barh(y, imported, left=endogenous, label="Imported", color="#ff7f0e")  # Orange vif

    #ecrire les % de chaque barres par rapport à leurs total
    for i in range(len(scenarios)):
        total = imported[i] + endogenous[i]
        if total > 0:
            ax.text(endogenous[i] / 2, y[i], f"{endogenous[i] / total:.1%}", ha='center', va='center', fontsize=12, color="white")
            ax.text(endogenous[i] + imported[i] / 2, y[i], f"{imported[i] / total:.1%}", ha='center', va='center', fontsize=12, color="white")

    # Configurer les axes et les étiquettes
    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, fontsize=14)
    ax.set_xlabel("PEC [TWh]", fontsize=14)
    ax.set_title("Local vs Imported PEC", fontsize=18)

    # Ajouter une légende
    ax.legend(fontsize=12, loc="upper left", bbox_to_anchor=(1, 1))

    #supprimier l'axe de haut

    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()
    #print(Share_scenario_1, Share_scenario_2, Share_scenario_3)
    table = {
        "Scenario": ["S1 : Trends", "S2 : Sufficiency", "S3 : Techno"],
        "Endogenous [%]": [Share_scenario_1[1]/Share_scenario_1.sum(), Share_scenario_2[1]/Share_scenario_2.sum(), Share_scenario_3[1]/Share_scenario_3.sum()],
        "Imported [%]": [Share_scenario_1[0]/Share_scenario_1.sum(), Share_scenario_2[0]/Share_scenario_2.sum(), Share_scenario_3[0]/Share_scenario_3.sum()],
    }
    print(tabulate.tabulate(table, headers="keys", tablefmt="grid", showindex=False))

if PEC :

    PEC_SCENARIO_1 = np.array([])
    PEC_SCENARIO_2 = np.array([])
    PEC_SCENARIO_3 = np.array([])

    filename = "resources_breakdown.txt"

    #open the file in a dataframe
    df1 = pd.read_csv(os.path.join(path1, filename), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, filename), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, filename), sep=r'\s+', engine='python')

    #faire un boucle à travers chaque ligne et dire que si jamais le nom correspond à un nom du dictionnaire un peut l'ajouter au PEC_SCENARIO_1, PEC_SCENARIO_2 ou PEC_SCENARIO_3 dans le même ordre
    for i in range(len(df1)):
        if df1["Name"][i] in ressource.keys():
            PEC_SCENARIO_1 = np.append(PEC_SCENARIO_1, df1["Used"][i])
            PEC_SCENARIO_2 = np.append(PEC_SCENARIO_2, df2["Used"][i])
            PEC_SCENARIO_3 = np.append(PEC_SCENARIO_3, df3["Used"][i])

    # Filtrer les ressources avec des valeurs non nulles pour au moins un scénario
    valid_resources = []
    PEC_SCENARIO_1_filtered = []
    PEC_SCENARIO_2_filtered = []
    PEC_SCENARIO_3_filtered = []

    for i, resource in enumerate(ressource.keys()):
        value_scenario_1 = PEC_SCENARIO_1[i] if i < len(PEC_SCENARIO_1) else 0
        value_scenario_2 = PEC_SCENARIO_2[i] if i < len(PEC_SCENARIO_2) else 0
        value_scenario_3 = PEC_SCENARIO_3[i] if i < len(PEC_SCENARIO_3) else 0

        # Inclure uniquement les ressources avec des valeurs non nulles
        if value_scenario_1 > 1 or value_scenario_2 > 1 or value_scenario_3 > 1:
            valid_resources.append(resource)
            PEC_SCENARIO_1_filtered.append(value_scenario_1)
            PEC_SCENARIO_2_filtered.append(value_scenario_2)
            PEC_SCENARIO_3_filtered.append(value_scenario_3)

    # Convertir les données filtrées en tableaux numpy
    PEC_SCENARIO_1_filtered = np.array(PEC_SCENARIO_1_filtered)/1000
    PEC_SCENARIO_2_filtered = np.array(PEC_SCENARIO_2_filtered)/1000
    PEC_SCENARIO_3_filtered = np.array(PEC_SCENARIO_3_filtered)/1000
    


    # Création du stacked bar plot
    fig, ax = plt.subplots(figsize=(10, 6))

    # Positions des barres (inverser l'ordre pour que S3 soit en bas)
    scenarios = ["S1 : Trends", "S2 : Sufficiency", "S3 : Techno"]
    y = np.arange(len(scenarios))[::-1]  # Inverser l'ordre des positions

    # Initialiser les barres empilées
    left_1 = np.zeros(len(y))
    left_2 = np.zeros(len(y))
    left_3 = np.zeros(len(y))

    # Réorganiser les ressources pour que "Ammonia" et "Bio Diesel" soient en dernière position
    reordered_resources = [res for res in valid_resources if res not in ["AMMONIA_RE", "BIODIESEL","GAS_RE","ELECTRICITY","GAS","H2_RE","METHANOL_RE"]]
    #if imp resouces is True, we add the resources in the end
    if "ELECTRICITY" in valid_resources:
        reordered_resources.append("ELECTRICITY")
    if "GAS" in valid_resources:
        reordered_resources.append("GAS")
    if "H2_RE" in valid_resources:
        reordered_resources.append("H2_RE")
    if "METHANOL_RE" in valid_resources:
        reordered_resources.append("METHANOL_RE")    
    if "BIODIESEL" in valid_resources:
        reordered_resources.append("BIODIESEL")
    if "AMMONIA_RE" in valid_resources:
        reordered_resources.append("AMMONIA_RE")
    if "GAS_RE" in valid_resources:
        reordered_resources.append("GAS_RE")



    # Ajouter les ressources au graphique
    for resource in reordered_resources:
        i = valid_resources.index(resource)
        color = ressource[resource]["color"]
        display_name = ressource[resource]["display_name"]

        # Ajouter les barres pour chaque scénario
        ax.barh(y[0], PEC_SCENARIO_1_filtered[i], left=left_1[0], color=color, label=display_name)
        ax.barh(y[1], PEC_SCENARIO_2_filtered[i], left=left_2[1], color=color, label=display_name)
        ax.barh(y[2], PEC_SCENARIO_3_filtered[i], left=left_3[2], color=color, label=display_name)

        # Mettre à jour les bases pour empiler les barres
        left_1[0] += PEC_SCENARIO_1_filtered[i]
        left_2[1] += PEC_SCENARIO_2_filtered[i]
        left_3[2] += PEC_SCENARIO_3_filtered[i]

    # Configurer les axes et les étiquettes
    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, fontsize=16)  # Mettre à jour les étiquettes des scénarios
    ax.set_xlabel("PEC [TWh]", fontsize=16)
    #ax.set_title("Primary Energy Consumption", fontsize=18)
    #set xticks at font size 16
    ax.tick_params(axis='x', labelsize=16)

    # Ajouter une légende
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Éviter les doublons dans la légende
    ax.legend(by_label.values(), by_label.keys(), fontsize=16, loc="center left", bbox_to_anchor=(1, 0.5), frameon=False)

    ax.spines['top'].set_visible(False)  # Supprimer la bordure supérieure
    ax.spines['right'].set_visible(False)  # Supprimer la bordure droite
    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()
    # Print in a table format
    table = {
        "Energy": valid_resources,
        "Scenario 1": list(PEC_SCENARIO_1_filtered),
        "Scenario 2": list(PEC_SCENARIO_2_filtered),
        "Scenario 3": list(PEC_SCENARIO_3_filtered)
    }
    print(tabulate.tabulate(table, headers="keys", tablefmt="grid", showindex=False))

if freightfleetconsumption :
    list_energy = ['ELECTRICITY', 'DIESEL',  'H2','GAS']
    list_energy_display_name = ['Electricity', 'Imp. Bio-Diesel', "Imp. Re. H2",'Imp. Re. Gas']
    df1 = pd.read_csv(os.path.join(path1, "year_balance.txt"), sep=r'\s+', engine='python')  # \s+ capture tabulations et espaces
    df2 = pd.read_csv(os.path.join(path2, "year_balance.txt"), sep=r'\s+', engine='python')
    df3 = pd.read_csv(os.path.join(path3, "year_balance.txt"), sep=r'\s+', engine='python')

    # Initialiser les tableaux avec des zéros
    freight_scenario_1 = np.zeros(len(list_energy))
    freight_scenario_2 = np.zeros(len(list_energy))
    freight_scenario_3 = np.zeros(len(list_energy))

    # Parcourir la liste des énergies
    for i in range(len(list_energy)):
        # Ajouter les valeurs pour les technologies de transport de fret
        for j in range(len(df1)):
            # Vérifier si la technologie est dans la liste freight_transport_technologies
            if df1["Tech"][j] in freight_transport_technologies.keys():
                if freight_transport_technologies[df1["Tech"][j]]["energy"] == list_energy[i]:
                    freight_scenario_1[i] -= df1[list_energy[i]][j] / 1000
                    freight_scenario_2[i] -= df2[list_energy[i]][j] / 1000
                    freight_scenario_3[i] -= df3[list_energy[i]][j] / 1000
                if freight_transport_technologies[df1["Tech"][j]]["energy_bis"] == list_energy[i]:
                    freight_scenario_1[i] -= df1[list_energy[i]][j] / 1000
                    freight_scenario_2[i] -= df2[list_energy[i]][j] / 1000
                    freight_scenario_3[i] -= df3[list_energy[i]][j] / 1000

    # Print in a table format
    table = {
        "Energy": list_energy_display_name + ["Total"],
        "Scenario 1": list(freight_scenario_1) + [freight_scenario_1.sum()],
        "Scenario 2": list(freight_scenario_2) + [freight_scenario_2.sum()],
        "Scenario 3": list(freight_scenario_3) + [freight_scenario_3.sum()]
    }
    print(tabulate.tabulate(table, headers="keys", tablefmt="grid", showindex=False))

    # Plotting the data
    fig, ax = plt.subplots(figsize=(10, 6))
    scenarios = ["S1 : Trends", "S2 : Sufficiency", "S3 : Techno"]
    y = np.arange(len(scenarios))[::-1]  # Reverse the order for proper display

    # Initialiser les barres empilées
    left_1 = np.zeros(len(y))
    left_2 = np.zeros(len(y))
    left_3 = np.zeros(len(y))

    # Ajouter les ressources au graphique
    for i, resource in enumerate(list_energy):
        display_name = list_energy_display_name[i]
        color = None
        for tech, tech_info in freight_transport_technologies.items():
            if tech_info["energy"] == resource:
                color = tech_info["color"]
                break

         # Si aucune couleur n'est trouvée ou si la couleur n'est pas valide, utiliser une couleur par défaut
        if color is None or not isinstance(color, str) or not color.startswith("#"):
            color = "#cccccc"  # Couleur par défaut (gris clair)

        # Ajouter les barres pour chaque scénario
        ax.barh(y[0], freight_scenario_1[i], left=left_1[0], color=color, label=display_name)
        ax.barh(y[1], freight_scenario_2[i], left=left_2[1], color=color, label=display_name)
        ax.barh(y[2], freight_scenario_3[i], left=left_3[2], color=color, label=display_name)

        # Mettre à jour les bases pour empiler les barres
        left_1[0] += freight_scenario_1[i]
        left_2[1] += freight_scenario_2[i]
        left_3[2] += freight_scenario_3[i]

    # Configurer les axes et les étiquettes
    ax.set_yticks(y)
    ax.set_yticklabels(scenarios, fontsize=16)  # Toujours afficher Scenario 1 en premier

    ax.set_xlabel("Energy consumption [TWh]", fontsize=16)
    #ax.set_title("Freight energy consumption", fontsize=20)
    # faire que le max de x soit 1.1 par rapport à la valeur max de la barre
    max_value = max(np.sum(freight_scenario_1), np.sum(freight_scenario_2), np.sum(freight_scenario_3))
    ax.set_xlim(0, 1.1 * max_value)  # Ajuster la limite de l'axe x
    # Ajouter les xticks
    ax.tick_params(axis='x', labelsize=16)
    # Ajouter une légende
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))  # Éviter les doublons dans la légende
    ax.legend(by_label.values(), by_label.keys(), fontsize=16, loc="center left", bbox_to_anchor=(1, 0.5), frameon=False)

    ax.spines['top'].set_visible(False)  # Supprimer la bordure supérieure
    ax.spines['right'].set_visible(False)  # Supprimer la bordure droite
    # Ajuster la mise en page
    plt.tight_layout()
    plt.show()
