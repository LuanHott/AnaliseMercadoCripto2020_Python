# Análise do Mercado Cripto 2020 
<p>
  <a href="https://www.linkedin.com/in/luanhteixeira/" target="_blank">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/800px-LinkedIn_logo_initials.png" alt="LinkedIn" width="30" height="30" style="vertical-align: middle;"/>
    <span style="vertical-align: middle; color: black;">/luanhteixeira</span>
  </a>
</p>

### Visão Geral

Esse projeto de análise de dados tem como objetivo fornecer insights sobre o mercado de criptomoedas. Atráves da análise de diversos pontos cruciais para o mercado cripto, busquei identificar padrões e fornecer de forma clara um melhor entendimento do mercado. 

Os notebooks que realizam a tarefa de limpeza e carregamento de dados podem ser encontrados [aqui](https://github.com/LuanHott/AnaliseMercadoCripto2020_Python/tree/main/notebooks/Limpeza%20e%20carregamento).

O notebook que realiza a análise exploratória pode ser encontrado [aqui](https://github.com/LuanHott/AnaliseMercadoCripto2020_Python/blob/main/notebooks/An%C3%A1lise%20explorat%C3%B3ria/EDA.py)

E o notebook que contém as visualizações é encontrado [aqui](https://github.com/LuanHott/AnaliseMercadoCripto2020_Python/blob/main/notebooks/Visualiza%C3%A7%C3%A3o%20dos%20resultados/Visualiza%C3%A7%C3%A3o.py)

<p align="center">
  <img src="https://github.com/LuanHott/AnaliseMercadoCripto2020_Python/blob/main/notebooks/Visualiza%C3%A7%C3%A3o%20dos%20resultados/imagem1.png" alt="Gráfico1" width="600"/>
</p>
<p align="center">
  <img src="https://github.com/LuanHott/AnaliseMercadoCripto2020_Python/blob/main/notebooks/Visualiza%C3%A7%C3%A3o%20dos%20resultados/imagem2.png" alt="Gráfico2" width="600"/>
</p>

### Fonte de dados

[Coin_Raw](https://www.kaggle.com/datasets/sudalairajkumar/cryptocurrencypricehistory/data): O data set primário do projeto, contendo informações detalhadas de 23 das principais moedas do mercado de 2020 como preço, data, market cap e volume.

[Calendar_Raw](https://www.kaggle.com/datasets/devorvant/economic-calendar/data?select=D2019-21.csv): O data set de apoio usado primariamente na primeira página do relatório, contendo o nome dos anúncios fiscais, países, volatilidade esperada e data.

### Ferramentas
- Python
  - Pandas: Limpeza, carregamento e análise exploratória.
  - Matplotlib: Visualização gráfica.
  - Numpy: Algumas operações matemáticas
    
### Limpeza e preparação dos dados

Na fase inicial do projeto foram seguidas as seguintes etapas:

- Limpeza inicial dos .csv utilizando pandas para fazer a primeira seleção de colunas e valores conforme escopo do projeto.

  - Utilizando um notebook python [Calendar_cleanup](https://github.com/LuanHott/Analise_MercadoCripto2020/blob/main/notebooks/calendar_cleanup.py) , realizei a limpeza selecionando apenas o nome e a data dos anúncios fiscais realizados no ano de 2020, que possuiam alta volatilidade esperada e foram realizados nos EUA. O resultado pode ser encontrado [aqui](https://github.com/LuanHott/Analise_MercadoCripto2020/blob/main/data/Calendar_Clean/calendar_clean.csv)
  - Utilizando de uma lógica similar [Coin_cleanup](https://github.com/LuanHott/Analise_MercadoCripto2020/blob/main/notebooks/coin_cleanup.py), realizei a limpeza das tabelas selecionando apenas as colunas relevantes para o escopo, que foram Nome, Data, Volume, Marketcap e o preço.

- Após a limpeza inicial, utilizei [desse](https://github.com/LuanHott/AnaliseMercadoCripto2020_Python/blob/main/notebooks/An%C3%A1lise%20explorat%C3%B3ria/EDA.py) notebook para separar os dados limpos em 4 tabelas que são usadas posteriormente MudançaHigh,MudançaMarketcap e MudançaVolume que contém os dados respectivos ao título e referentes apenas as datas em que aconteceram anúncios fiscais e a tabela ConvarianciaBTC que calcula a convariância da mudança do preço de cada moeda com o Bitcoin. Todos essas tabelas são encontradas [aqui](https://github.com/LuanHott/AnaliseMercadoCripto2020_Python/tree/main/data/Tabelas).

### Análise exploratória de dados

A AED consistiu em explorar padrões em ambas as tabelas iniciais de dados para responder algumas perguntas chaves como:

1. Qual anúncio fiscal tem o maior impacto sobre o mercado cripto (preço, volume, marketcap)? E sobre uma moeda específica?
2. Quais as moedas que sofrem mais impacto dos anúncios fiscais em seu respectivo âmbito (preço, volume, marketcap)?
3. Qual foi o movimento do mercado em 2020, ele cresceu? O volume de dinheiro aportado e movimentado, cresceu?
4. Quais são as moedas mais voláteis? Consequentemente as melhores moedas para traders.
5. Existe uma correlação da mudança dos preços das moedas em relação a mudança da principal moeda, o bitcoin? Qual o tamanho dessa correlação?

### Análise de dados

A lógica chave para grande parte do projeto, é assimilar o anúncio fiscal à mudança de preço,volume ou marketcap de um dia para o outro. Foi realizado dessa forma:

MudançaRelativa = Preço na data posterior ao anúncio - Preço na data do anúncio
MudançaReal = (MudançaRelativa / Valor atual) * 100

Que também pode ser representado pelos códigos abaixo:

```
MudançaHigh = pd.merge(calendar['Date'], coins[['Name','Date','High']], on='Date', how ='inner')
MudançaHigh = MudançaHigh.drop_duplicates(subset=['Date', 'Name'], keep='first')
MudançaHigh.reset_index(drop=True, inplace=True)

MudançaHigh['PostDate'] = MudançaHigh['Date'] + pd.Timedelta(days=1)

MudançaHigh['PostHigh'] = pd.merge(MudançaHigh[['PostDate','Name']].rename(columns={'PostDate':'Date'}), coins[['Date','High','Name']].rename(columns={'High': 'PostHigh'}),on=['Date','Name'], how = 'inner')['PostHigh']

MudançaHigh['PostHigh'] = MudançaHigh.groupby('Name')['PostHigh'].ffill()

MudançaHigh['Change'] = abs((MudançaHigh['PostHigh'] - MudançaHigh['High']) / MudançaHigh['High'] * 100)
MudançaHigh['Change'] = MudançaHigh['Change'].round(4)
MudançaHigh.to_csv('../../Data/Tabelas/MudançaHigh.csv', index=False)
```
A lógica foi usada e replicada para volume e market cap.

Um código interessante também foi o referente a covariãncia com o bitcoin, no qual eu precisava forçar os cálculos no contexto de linha, o que não é o usual das funções do pandas, portanto utilizei desse código:

```
dfCovariancia = MudançaHigh[['Name','Change']].groupby('Name').mean().reset_index()

Varianciabtc = dfCovariancia.loc[dfCovariancia['Name'] == 'Bitcoin', 'Change'].values[0]

def varianciacombitcoin(row):
    return (row['Change'] - Varianciabtc) ** 2

dfCovariancia['CovarianceComBTC'] = dfCovariancia.apply(lambda row: varianciacombitcoin(row), axis=1)
```

### Resultados/Descobertas

O resultado das análises podem ser resumidos em:

- O PPI é o anúncio fiscal que mais impactou no preço do mercado como um todo, mas cada moeda é impactada de uma forma única.
- O EIA Short-Term Energy Outlook foi o anúncio fiscal que mais impactou o volume do mercado como um todo, mas cada moeda é impacatada de uma forma única.
- O Sesc Kashkari Speaks foi o anúncio fiscal que mais trouxe acúmulo de capital pro mercado, porém a diferença entre os 5 que mais impactaram não é muito grande, e novamente cada moeda é impactada de forma única.
- O preço, o marketcap e o volume do mercado de 2020 tiveram uma alta constante desde o ínicio ao fim do ano, o que nos leva a acreditar que tudo estaria pronto para 2021 ser um grande ano no mercado cripto (e foi).
- A melhor moeda para trade foi a Solana, que possuiu uma volatilidade de quase 6% acima da média.
- A solana também é a moeda que mais tenta imitar os movimentos do bitcoin de forma mais precisa, possuindo uma alta correlação no preço de ambas.







