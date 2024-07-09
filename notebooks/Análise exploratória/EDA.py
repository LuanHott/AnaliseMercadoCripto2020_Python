# %%
import pandas as pd

coins = pd.read_csv("../../Data/Coin_Clean/Coin_Clean.csv")
calendar = pd.read_csv('../../Data/Calendar_Clean/Calendar_clean.csv')
# %%
calendar['Date'] = pd.to_datetime(calendar['Date'])
coins['Date'] = pd.to_datetime(coins['Date'])
# %%
MudançaHigh = pd.merge(calendar['Date'], coins[['Name','Date','High']], on='Date', how ='inner')
MudançaHigh = MudançaHigh.drop_duplicates(subset=['Date', 'Name'], keep='first')
MudançaHigh.reset_index(drop=True, inplace=True)

MudançaHigh['PostDate'] = MudançaHigh['Date'] + pd.Timedelta(days=1)

MudançaHigh['PostHigh'] = pd.merge(MudançaHigh[['PostDate','Name']].rename(columns={'PostDate':'Date'}), coins[['Date','High','Name']].rename(columns={'High': 'PostHigh'}),on=['Date','Name'], how = 'inner')['PostHigh']

MudançaHigh['PostHigh'] = MudançaHigh.groupby('Name')['PostHigh'].ffill()

MudançaHigh['Change'] = abs((MudançaHigh['PostHigh'] - MudançaHigh['High']) / MudançaHigh['High'] * 100)
MudançaHigh['Change'] = MudançaHigh['Change'].round(4)
# %%

# %%
MudançaHigh.tail(50)
# %%
