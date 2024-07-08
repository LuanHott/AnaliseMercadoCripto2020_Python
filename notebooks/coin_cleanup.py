# %%

import pandas as pd
import os

input_folder = "../data/Coin_Raw/"
output_folder = "../data/Coin_Clean/"
start_date = '2020-01-01'
end_date = '2020-12-31'
#%%
csv_files = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

for csv_file in csv_files:

    df_coins = pd.read_csv(os.path.join(input_folder, csv_file))
    
    df_coins = df_coins.drop(['Symbol', 'SNo', 'Low', 'Open', 'Close'], axis=1)
    
    coins_filtered = df_coins[(df_coins['Date'] >= start_date) & (df_coins['Date'] <= end_date)]

    coins_filtered.reset_index(inplace=True, drop=True)
    
    output_file = os.path.join(output_folder, csv_file.replace('.csv', '_clean.csv'))
    coins_filtered.to_csv(output_file, index=False)

# %%
