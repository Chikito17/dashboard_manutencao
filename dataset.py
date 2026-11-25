import json
import pandas as pd

# Rougher
file_rm = open('dados/RM_j.json')
data_rm = json.load(file_rm)

df_rm = pd.DataFrame.from_dict(data_rm)

#Steckel
file_sm = open('dados/SM_j.json')
data_sm = json.load(file_sm)

df_sm = pd.DataFrame.from_dict(data_sm)

# Bobinadeira Final
file_dc = open('dados/DC_j.json')
data_dc = json.load(file_dc)

df_dc = pd.DataFrame.from_dict(data_dc)

# Fornos SMF
file_smf = open('dados/SMF_j.json')
data_smf = json.load(file_smf)

df_smf = pd.DataFrame.from_dict(data_smf)

# Fornos SMF
file_dcv = open('dados/DCV_j.json')
data_dcv = json.load(file_dcv)

df_dcv = pd.DataFrame.from_dict(data_dcv)

file_rm.close()
file_sm.close()
file_dc.close()
file_smf.close()
file_dcv.close()