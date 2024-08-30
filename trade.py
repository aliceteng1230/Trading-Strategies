import pandas as pd

data_mor = pd.read_excel("data_mor.xlsx")
calculation = pd.read_excel("calculation.xlsx")

for i in range(0, len(data_mor)-9, 10):
    hit = 0
    for j in range(0, len(calculation)):
        if data_mor.iloc[i]['date'] == calculation.loc[j]['Date']:    
            data_mor.loc[i:i+9, 'change'] = calculation.loc[j]['Change']
            hit = 1
    if hit == 0:
        data_mor.loc[i:i+9, 'change'] = 0
data_mor.to_excel('data_result.xlsx')           
