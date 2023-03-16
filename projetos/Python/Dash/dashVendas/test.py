import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import time
import locale


df = pd.read_csv('assets/dadosVendas003.csv', sep=';', encoding='utf-8-sig')
dfFilter = df['Empresa']==227
dfTime = pd.to_datetime(df['DataVenda'], dayfirst=True)

dfFiltered = df.where(dfFilter)
dfFiltered["DataVenda"] = dfTime

monthsYearSeries = dfFiltered['DataVenda'].apply(lambda x: x.strftime('%Y-%m')) 
dfMonthsYear = pd.DataFrame({'DataVenda': monthsYearSeries})

#locale.setlocale(locale.LC_ALL, 'pt_BR')

#dfFiltered['Cidade'] = dfFiltered['Cidade'].str.replace(' ', '_')
#filter = df['Empresa']==227
#dfFilter1 = df.where(filter)

#print(df)
#print('')
#print("carregando")
#time.sleep(2)
#print(dfFilter1)


#timeNow = datetime.now()
#less6Months = datetime.now() - timedelta(days=180)
#aybeWork = less6Months.strftime('%d/%m/%Y')

#print(timeNow)
#print(less6Months)
#print(maybeWork)

#time6Month = (datetime.now() - timedelta(days=180)).strftime('%Y/%m/%d')
#onvertToTime = pd.to_datetime(df['DataVenda'])

#print(convertToTime)
#df['DataVenda'] = convertToTime
#print(df['DataVenda'])
#print(time6Month)
#print(df['DataVenda'])

#filterUf = ['PB', 'GO', 'AM']
#groupUf = dfFiltered[dfFiltered.UF.isin(filterUf)]
#works = groupUf.groupby(['Cidade'])['UF'].apply(list)
#print(works[0])
#print(len(works))
#print(works)
#print("=====================================")
#worksDataframe = pd.DataFrame({'city': works.index, 'UF': works.values})
#print(worksDataframe)
#print("=====================================")

#worksDataframe["count"] = worksDataframe["UF"].str.len()
#worksDataframe["UF"] = worksDataframe["UF"].str[0]

#print(worksDataframe)
#print("CALMO")

#dfVendasUf = dfFiltered.groupby(['UF']).count()
#print(dfVendasUf)
#vendasUfDataframe = pd.DataFrame({'UF': dfVendasUf.index, 'Vendas': dfVendasUf['Obra']})

#vendasSort = vendasUfDataframe.sort_values(['Vendas'], ascending=False).head(10)
#print(vendasSort)
#teste = 10
#print(type(teste))

#if (type(teste) == int):
#    print('funfa')

#time4Month = (datetime.now() - timedelta(days=120)).strftime('%B-%Y')
#dfVendasMês = dfFiltered[pd.to_datetime(dfFiltered['DataVenda']) > time4Month]
#dfMonthYear = dfVendasMês['DataVenda'].apply(lambda x: x.strftime('%B-%Y')) 
#dfVendasMês['DataVenda'] = dfMonthYear
#vendas4Meses = dfVendasMês.groupby(['DataVenda']).count()

#vendas4MesesDf = pd.DataFrame({'DataVendas': vendas4Meses.index, 'Vendas': vendas4Meses['Obra']})
#print(vendas4MesesDf)

#print(locale.setlocale(locale.LC_ALL, 'pt_BR'))
#print(locale.currency( 188518982.18 ))
#print(locale.currency( 188518982.18, grouping=True ))

#time4Month = (datetime.now() - timedelta(days=120)).strftime('%B-%Y')
#dfVendasMês = dfFiltered[pd.to_datetime(dfFiltered['DataVenda']) > time4Month]
#dfMonthYear = dfVendasMês['DataVenda'].apply(lambda x: x.strftime('%B-%Y')) 
#dfVendasMês['DataVenda'] = dfMonthYear
#vendas4Meses = dfVendasMês.groupby(['DataVenda']).count()
#vendas4MesesDf = pd.DataFrame({'DataVendas': vendas4Meses.index, 'Vendas': vendas4Meses['Obra']})

#print(vendas4MesesDf)


#monthsYearSeriesTest = dfFiltered['DataVenda'].apply(lambda x: x.strftime('%m-%y')) 
#fFiltered['DataVenda'] = monthsYearSeriesTest

#dfFodder = dfFiltered
#dfFodder['DataVenda'] = monthsYearSeries
#dfMonthFilter = dfFodder[dfFodder['DataVenda']=='12-20']

time4Months = (datetime.now() - timedelta(days=120)).strftime('%Y-%m')
dfVendasMês = dfFiltered[dfMonthsYear['DataVenda'] > time4Months]
dfMonthYear = dfVendasMês['DataVenda'].apply(lambda x: x.strftime('%B-%y')) 
dfVendasMês['DataVenda'] = dfMonthYear
vendas4Meses = dfVendasMês.groupby(['DataVenda']).count()
vendas4MesesDf = pd.DataFrame({'DataVendas': vendas4Meses.index, 'Vendas': vendas4Meses['Obra']})

print(dfVendasMês['DataVenda'])
print(vendas4MesesDf)