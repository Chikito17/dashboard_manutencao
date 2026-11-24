import json
import pandas as pd


file = open('dados/SM_j.json')
data = json.load(file)

df = pd.DataFrame.from_dict(data)

file.close()