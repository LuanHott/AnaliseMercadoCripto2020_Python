# %%
import pandas as pd

columns = ['Date','Time','Country','Volatility','Name']
pd_calendar = pd.read_csv("../data/Calendar_Raw/d2019-21.csv", delimiter=';',usecols=range(len(columns)), names=columns)
pd_calendar.head()
# %%
df_calendar = pd_calendar[pd_calendar['Volatility'].str.strip() == 'High Volatility Expected']
# %%
df_calendar = df_calendar[df_calendar['Country'].str.strip() == 'United States']
# %%
df_calendar.reset_index(inplace=True, drop=True)
df_calendar.head()
# %%
df_calendar = df_calendar.drop(['Time'],axis=1)
df_calendar.head()
# %%
df_calendar = df_calendar.drop(['Country','Volatility'],axis=1)
df_calendar.head()

# %%

start_date = '2020/01/01'
end_date = '2020/12/31'

calendar_filtered = df_calendar[(df_calendar['Date'] >= start_date) & (df_calendar['Date'] <= end_date)]

# %%
calendar_filtered.reset_index(inplace=True,drop=True)
calendar_filtered.head()

# %%

calendar_filtered.to_csv('../data/Calendar_Clean/Calendar_clean.csv',index=False)