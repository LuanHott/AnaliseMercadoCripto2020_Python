# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

Coins = pd.read_csv("../../Data/Coin_clean/Coin_clean.csv")
Calendar = pd.read_csv("../../Data/Calendar_clean/Calendar_clean.csv")
Calendar['Date'] = pd.to_datetime(Calendar['Date'], format='%Y/%m/%d')
High = pd.read_csv("../../Data/Tabelas/MudançaHigh.csv")
High['Date'] = pd.to_datetime(High['Date'])
Volume = pd.read_csv("../../Data/Tabelas/MudançaVolume.csv")
Volume['Date'] = pd.to_datetime(High['Date'])
Mktcap = pd.read_csv("../../Data/Tabelas/MudançaMarketcap.csv")
Mktcap['Date'] = pd.to_datetime(High['Date'])
Covariancia = pd.read_csv("../../Data/Tabelas/Covarianciabtc.csv")
# %%
# Moeda mais Impactada no Preço
MaxChange = Covariancia['Change'].max()
MoedaImpactadaPreco = Covariancia[Covariancia['Change'] == MaxChange][['Name','Change']]
MoedaImpactadaPreco
# %%
# Moeda mais Impactada no Volume
MaxChangeVoldf = Volume[['Name','Change']].groupby('Name').mean().reset_index()
MaxChangeVol = MaxChangeVoldf['Change'].max()
MoedaImpactadaVolume = MaxChangeVoldf[MaxChangeVoldf['Change'] == MaxChangeVol][['Name','Change']]
MoedaImpactadaVolume
# %%
# Moeda mais Impactada no MarketCap
MaxChangemktcapdf = Mktcap[['Name','Change']].groupby('Name').mean().reset_index()
MaxChangemktcap = MaxChangemktcapdf['Change'].max()
MoedaImpactadaMktcap = MaxChangemktcapdf[MaxChangemktcapdf['Change'] == MaxChangemktcap][['Name','Change']]
MoedaImpactadaMktcap
# %%
Impactopreco = High[['Date','Change']].groupby('Date').mean().reset_index()
Anunciopreco = pd.merge(Calendar[['Date', 'Name']], Impactopreco[['Date','Change']], on='Date', how='inner').sort_values(by='Change')
Anunciopreco = Anunciopreco[['Name','Change']].groupby('Name').mean().sort_values(by='Change').reset_index()

ImpactoVol = Volume[['Date','Change']].groupby('Date').mean().reset_index()
AnuncioVol = pd.merge(Calendar[['Date', 'Name']], ImpactoVol[['Date','Change']], on='Date', how='inner').sort_values(by='Change')
AnuncioVol = AnuncioVol[['Name','Change']].groupby('Name').mean().sort_values(by='Change').reset_index()

ImpactoMktcap = Mktcap[['Date','Change']].groupby('Date').mean().reset_index()
AnuncioMktcap = pd.merge(Calendar[['Date', 'Name']], ImpactoMktcap[['Date','Change']], on='Date', how='inner').sort_values(by='Change')
AnuncioMktcap = AnuncioMktcap[['Name','Change']].groupby('Name').mean().sort_values(by='Change').reset_index()
# %%
# Datas mais impactantes no preço
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(Anunciopreco['Name'],Anunciopreco['Change'], align='center')
ax.set_xlabel('% Mudança no preço')
ax.set_title('Impacto dos anúncios fiscais no preço das criptomoedas',loc='center')
plt.tight_layout()
plt.show()
# %%
# Datas mais impactantes no volume
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(AnuncioVol['Name'],AnuncioVol['Change'], align='center')
ax.set_xlabel('% Mudança no volume')
ax.set_title('Impacto dos anúncios fiscais no preço das criptomoedas',loc='center')
plt.tight_layout()
plt.show()
# %%
# Datas mais impactantes no MktCap
fig, ax = plt.subplots(figsize=(10, 8))
ax.barh(AnuncioMktcap['Name'],AnuncioMktcap['Change'], align='center')
ax.set_xlabel('% Mudança no MarketCap')
ax.set_title('Impacto dos anúncios fiscais no preço das criptomoedas',loc='center')
plt.tight_layout()
plt.show()
# %%
# Movimento do mercado
Coinsdf = Coins[['Date','High']].groupby('Date').std().reset_index()
plt.plot(Coinsdf['Date'],Coinsdf['High'])
plt.xticks([])
plt.xlabel('Tempo')
plt.title('Movimento do mercado')
plt.show()
# %%
# Volume do mercado
voldf = Coins[['Date','Volume']].groupby('Date').std().reset_index()
plt.plot(voldf['Date'],voldf['Volume'])
plt.xticks([])
plt.xlabel('Tempo')
plt.title('Volume do mercado')
plt.show()
# %%
# Capitalização do mercado
mktcapdf = Coins[['Date','Marketcap']].groupby('Date').std().reset_index()
plt.plot(mktcapdf['Date'],mktcapdf['Marketcap'])
plt.xticks([])
plt.xlabel('Tempo')
plt.title('Capitalização do mercado')
plt.show()
# %%
volatilidade = High[['Name','Change']].groupby('Name').std().sort_values(by="Change").reset_index()
plt.bar(volatilidade['Name'],volatilidade['Change'])
plt.title('Moedas mais voláteis')
plt.xticks(rotation=90)
plt.show()
# %%
correlacao = Covariancia[['Name','CovarianceComBTC']].sort_values('CovarianceComBTC').reset_index()
plt.bar(correlacao['Name'],correlacao['CovarianceComBTC'])
plt.title('Moedas com maior covariância com o bitcoin')
plt.xticks(rotation=90)
plt.show()
# %%
