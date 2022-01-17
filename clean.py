import pandas as pd
import csv

df = pd.read_csv("final.csv")

del df['Luminosity']
del df["Unnamed: 0"]
del df["Unnamed: 5"]
del df["Star_name"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]

# df = df.rename({
#                 'pl_hostname': "solar_system_name", 
#                 'pl_discmethod': "planet_discovery_method", 
#                 'pl_orbincl': "planet_orbital_inclination", 
#                 'pl_dens': "planet_density", 
#                 'ra_str': "right_ascension", 
#                 'dec_str': "declination", 
#                 "st_teff": "host_temperature", 
#                 'st_mass': "host_mass", 
#                 'st_rad': "host_radius"
#             }, axis='columns')

df.to_csv('main.csv')