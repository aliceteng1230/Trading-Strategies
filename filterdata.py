import pandas as pd
pdata = pd.read_excel('選股池.xlsx')

pidx = pdata['Number']
psidx = [str(x) for x in pidx]

#sdata = pd.read_excel('股票波動.xlsx')
#sdata = pd.read_excel('cond1. 振幅.xlsx')
#sdata = pd.read_excel('cond2. 現股當沖比例.xlsx')
sdata1 = pd.read_excel('cond3. 成交金額與理論值的差異.xlsx', sheet_name='成交金額')
sdata2 = pd.read_excel('cond3. 成交金額與理論值的差異.xlsx', sheet_name='股票佔大盤權重')


fdata1 = sdata1[sdata1.columns.intersection(psidx)]
fdata2 = sdata2[sdata2.columns.intersection(psidx)]

#fdata.to_excel('股票波動clear.xlsx')
#fdata1.to_excel('cond3. 成交金額與理論值的差異clear.xlsx', sheet_name='成交金額')
#fdata2.to_excel('cond3. 成交金額與理論值的差異clear.xlsx', sheet_name='股票佔大盤權重')

path = r"cond3. 成交金額與理論值的差異clear.xlsx"
writer = pd.ExcelWriter(path, engine='openpyxl')
fdata1.to_excel(writer, '成交金額', index=False)
fdata2.to_excel(writer, '股票佔大盤權重', index=False)
writer.save()