import pandas as pd
data_mor = pd.read_excel("data_mor.xlsx")
daily = pd.read_excel("daily_data.xlsx")
for i in range(0, len(data_mor)-9, 10):
    hit = 0
    for j in range(0, len(daily)):
        if data_mor.loc[i]['date'] == daily.loc[j]['Date']:    
            data_mor.loc[i:i+9, 'Short_EMA'] = daily.loc[j]['Short_EMA']
            data_mor.loc[i:i+9, 'Long_EMA'] = daily.loc[j]['Long_EMA']
            hit = 1
            break
    if hit == 0:
        data_mor.loc[i:i+9, 'Short_EMA'] = 0
        data_mor.loc[i:i+9, 'Long_EMA'] = 0
data_mor.to_excel("data_result.xlsx")