import pandas as pd
#df = pd.read_excel('股票當天波動clear.xlsx')
#df = pd.read_excel('cond1. 振幅clear.xlsx')
df = pd.read_excel('cond2. 現股當沖比例clear.xlsx')


df2 = df.melt(id_vars=["股票代號"], var_name="stockid", value_name="Value")
df2.sort_values(['股票代號', 'stockid'], ascending=[True, True], inplace=True)
#df2.columns = ['日期', '股票代號', '當天波動']
df2.columns = ['日期', '股票代號', '現股當沖比例']

#df2.to_excel('股票當天波動unpivot.xlsx', index=False)
df2.to_excel('cond2. 現股當沖比例unpivot.xlsx', index=False)


#dfa = pd.read_excel('cond1. 振幅clear.xlsx')
#dfb = pd.read_excel('cond2. 現股當沖比例clear.xlsx')
#dfm = pd.DataFrame()
#dfm.loc[:,'日期'] = dfa.loc[:,'日期']
#dfm.loc[:,'股票代號'] = dfa.loc[:,'股票代號']
#dfm.loc[:,'振幅'] = dfa.loc[:,'振幅']
#dfm.loc[:,'現股當沖比例'] = dfb.loc[:,'現股當沖比例']
