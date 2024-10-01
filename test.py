import pandas as pd

data = pd.read_csv('C:/Users/Sreedharsh/Downloads/GRPH Historical Data.csv')  


capital = 1000  
position = 0  
entry_price = 0
count=0
success=0
total=0
profitmade=0
lossmade=0
for i in range(len(data)-1,0,-1):

    if count>=3:
        position=-1
        entry_price = data['Open'][i]
        print(f"Short at {entry_price} on {data['Date'][i]}")
    if position == -1:
        exit_price = data['Price'][i]
        profit = (entry_price - exit_price)*(2)
        capital += profit
        position = 0
        total+=1
        if(profit>0 ):
            profitmade=profitmade+profit
            success+=1
        else:
            lossmade-=profit
        print(f"Cover at {exit_price} on {data['Date'][i]}, Profit: {profit}")
    if position == 0 and data['Open'][i] > data['Price'][i]:
        count+=1
    else:
        count=0    


    

print(f"Final Capital: {capital} Succes rate= {success/total}  lossmade={lossmade}")

