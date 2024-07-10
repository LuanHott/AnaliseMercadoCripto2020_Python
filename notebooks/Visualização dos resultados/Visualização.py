# %%
import pandas as pd
import numpy as np

Calendar = pd.read_csv("../../Data/Calendar_clean/Calendar_clean.csv")
High = pd.read_csv("../../Data/Tabelas/MudançaHigh.csv")
Volume = pd.read_csv("../../Data/Tabelas/MudançaVolume.csv")
Mktcap = pd.read_csv("../../Data/Tabelas/MudançaMarketcap.csv")
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

# %%
