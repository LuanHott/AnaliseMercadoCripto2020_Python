# %%

import pandas as pd
import os

input_folder = "../data/Coin_Raw/"
start_date = '2020-01-01'
end_date = '2020-12-31'

#%%
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

df_list = []

for csv_file in csv_files:

    df_coins = pd.read_csv(os.path.join(input_folder, csv_file))
    
    df_coins = df_coins.drop(['Symbol', 'SNo', 'Low', 'Open', 'Close'], axis=1)
    
    coins_filtered = df_coins[(df_coins['Date'] >= start_date) & (df_coins['Date'] <= end_date)]

    coins_filtered.reset_index(inplace=True, drop=True)

    df_list.append(coins_filtered)
   
# %%
coins_final = pd.concat(df_list, ignore_index=True)

coins_final[['High', 'Volume', 'Marketcap']] = coins_final[['High', 'Volume', 'Marketcap']].round(4)
pd.set_option('display.float_format', '{:.4f}'.format)

coins_final['Date'] = pd.to_datetime(coins_final['Date'], errors='coerce').dt.date    
coins_final['Date'] = pd.to_datetime(coins_final['Date'].astype(str), errors='coerce')
# %%
coins_final
# %%
coins_final.to_csv("../data/Coin_Clean/Coin_Clean.csv", index=False)
# %%
