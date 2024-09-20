import pandas as pd

data = pd.read_excel('C:/Users/A51607/Desktop/Work/股票當天波動finish.xlsx').fillna(0)
pick_count = 0
win_count = 0

for i in range(1, len(data) - 231 , 231):
    pick = []
    win = []
    date = data['日期'].iloc[i]

    for j in range(231):
        id = i + j 
        stock = data['股票代號'].iloc[id]
        if data['振幅'].iloc[id] > 3.5 and data['現股當沖比例'].iloc[id] > 0.0015 and data['實際值與理論值的差異'].iloc[id] > 2:
            pick.append(stock)
            if data['股票當天波動'].iloc[id] > 0.05:
                win.append(stock)
        else:
            continue
    pick_num = len(pick)
    win_num = len(win)
    winrate = win_num / pick_num
    pick_count += pick_num
    win_count += win_num
    daily = {'Date': date, 'Stock': pick, 'Winrate': winrate}
    print(daily)

totalwinrate = win_count / pick_count
print(win_count)
print(pick_count)
print(totalwinrate)




            

