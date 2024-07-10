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
MudançaHigh.to_csv('../../Data/Tabelas/MudançaHigh.csv', index=False)
# %%
MudançaVol = pd.merge(calendar['Date'], coins[['Name','Date','Volume']], on='Date', how ='inner')
MudançaVol = MudançaVol.drop_duplicates(subset=['Date', 'Name'], keep='first')
MudançaVol.reset_index(drop=True, inplace=True)

MudançaVol['PostDate'] = MudançaVol['Date'] + pd.Timedelta(days=1)

MudançaVol['PostVol'] = pd.merge(MudançaHigh[['PostDate','Name']].rename(columns={'PostDate':'Date'}), coins[['Date','Volume','Name']].rename(columns={'Volume': 'PostVol'}),on=['Date','Name'], how = 'inner')['PostVol']

MudançaVol['PostVol'] = MudançaVol.groupby('Name')['PostVol'].ffill()

MudançaVol['Change'] = abs((MudançaVol['PostVol'] - MudançaVol['Volume']) / MudançaVol['Volume'] * 100)
MudançaVol['Change'] = MudançaVol['Change'].round(4)
MudançaVol.to_csv('../../Data/Tabelas/MudançaVolume.csv', index=False)
# %%
MudançaMarketcap = pd.merge(calendar['Date'], coins[['Name','Date','Marketcap']], on='Date', how ='inner')
MudançaMarketcap = MudançaMarketcap.drop_duplicates(subset=['Date', 'Name'], keep='first')
MudançaMarketcap.reset_index(drop=True, inplace=True)

MudançaMarketcap['PostDate'] = MudançaMarketcap['Date'] + pd.Timedelta(days=1)

MudançaMarketcap['PostMarketcap'] = pd.merge(MudançaMarketcap[['PostDate','Name']].rename(columns={'PostDate':'Date'}), coins[['Date','Marketcap','Name']].rename(columns={'Marketcap': 'PostMarketcap'}),on=['Date','Name'], how = 'inner')['PostMarketcap']

MudançaMarketcap['PostMarketcap'] = MudançaMarketcap.groupby('Name')['PostMarketcap'].ffill()

MudançaMarketcap['Change'] = abs((MudançaMarketcap['PostMarketcap'] - MudançaMarketcap['Marketcap']) / MudançaMarketcap['Marketcap'] * 100)
MudançaMarketcap['Change'] = MudançaMarketcap['Change'].round(4)
MudançaMarketcap.to_csv('../../Data/Tabelas/MudançaMarketcap.csv', index=False)
# %%
dfCovariancia = MudançaHigh[['Name','Change']].groupby('Name').mean().reset_index()

Varianciabtc = dfCovariancia.loc[dfCovariancia['Name'] == 'Bitcoin', 'Change'].values[0]

def varianciacombitcoin(row):
    return (row['Change'] - Varianciabtc) ** 2

dfCovariancia['CovarianceComBTC'] = dfCovariancia.apply(lambda row: varianciacombitcoin(row), axis=1)
# %%
dfCovariancia.to_csv('../../Data/Tabelas/Covarianciabtc.csv')
# %%
