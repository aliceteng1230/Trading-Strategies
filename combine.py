import pandas as pd

wave = pd.read_excel('股票當天波動clear.xlsx')
cond = pd.DataFrame()
cond1 = pd.read_excel("cond1.xlsx")
cond2 = pd.read_excel("cond2.xlsx")
cond31 = pd.read_excel('cond31.xlsx')
cond32 = pd.read_excel('cond32.xlsx')
cond4 = pd.read_excel("cond4.xlsx")


for i in range(231, len(wave), 1):
    print(i)
    j = i - 231
    wave.loc[i:i, '振幅'] = cond1.loc[j]['振幅']
    wave.loc[i:i, '現股當沖比例'] = cond2.loc[j]['現股當沖比例']
    wave.loc[i:i, '成交金額'] = cond31.loc[j]['成交金額']
    wave.loc[i:i, '股票佔大盤權重'] = cond32.loc[j]['股票佔大盤權重']    

for i in range(0, len(wave), 231):
    print(i)
    k = (i / 231)
    wave.loc[i:i+231, '成交量比例'] = cond4.loc[k]['比例']

wave.to_excel('股票當天波動finish.xlsx', index=False)           
