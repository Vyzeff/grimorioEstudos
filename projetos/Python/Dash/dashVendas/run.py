import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

import locale
import pandas as pd
from datetime import datetime, timedelta

# ===========================================
# Data Load 
df = pd.read_csv('assets/dadosVendas003.csv', sep=';', encoding='utf-8-sig')
dfFilter = df['Empresa']==227
dfTime = pd.to_datetime(df['DataVenda'], dayfirst=True, format='%d/%m/%Y', errors="coerce")

dfFiltered = df.where(dfFilter)
dfFiltered["DataVenda"] = dfTime

dfCopy = dfFiltered
monthsYearSeries = dfCopy['DataVenda'].apply(lambda x: x.strftime('%m-%y')) 
dfMonthsYear = pd.DataFrame({'DataVenda': monthsYearSeries})

#locale.setlocale(locale.LC_ALL, 'pt_BR')
# ===========================================
# Start App
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LUX],
)

# ===========================================
# Layout
app.layout = dbc.Container(
    children=[
        html.Div(id='top'),
        dbc.Row(children=
                 [
                    dbc.Card(dbc.CardBody([
                        html.H2(["Vendas UAU"]),
                        dbc.Button("227", color="primary", id="empresa-button", size="lg", class_name='defaultButton'),
                        html.H3('CARREGANDO...', id='mesLabel'),
                        dcc.Dropdown(    
                            id="mesCheck",                                    
                            options=dfMonthsYear.DataVenda.dropna().unique(), 
                            value='12-20'
                            ),
                dbc.Row([
                    dbc.Col([dbc.Card([
                        dbc.CardBody([
                            html.Span("Contagem de Vendas No Mês", className='cardText'),
                            html.H3("CARREGANDO...", id='contagemVendasMes'),
                            html.Span("Estado com mais Vendas no Mês", className='cardText'),
                            html.H3("CARREGANDO...", id='estadoMaisVendasMes')
                        ])
                    ])], md=4),
                    
                        dbc.Col([dbc.Card([
                        dbc.CardBody([
                            html.Span("Valor das Vendas em R$ no Mês", className='cardText'),
                            html.H3("CARREGANDO...", id='valorVendasMes'),
                        ])
                    ])], md=4),
                            
                         dbc.Col([dbc.Card([
                            dbc.CardBody([
                                html.Span("Contagem de Cancelamentos no Mês", className='cardText'),
                                html.H3("CARREGANDO...", id='contagemCancelasMes'),
                                html.Span("Contagem de Vendas Quitadas no Mês", className="cardText"),
                                html.H3("CARREGANDO...", id='contagemQuitadasMes')
                        ])
                    ])], md=4),
                ]),
                    ])),
  dbc.Col([              
                    ], md=5),
                dbc.Col([
                    dbc.Row([
                        dbc.Card(dbc.CardBody(dcc.Graph(id="vendasPorFaixaEtáriaMes")))
                        ]),
                    dbc.Row([ 

                    ]),
                ], md=12),
                dbc.Row([
                html.Span('Número de Vendas por UF no Mês'),
                dcc.RadioItems(id='vendasFilterMes', options=[
                    {'label': 'Top 5', 'value': 5},
                    {'label': 'Top 10', 'value': 10},
                    {'label': 'Top 15', 'value': 15},
                    {'label': 'Todos', 'value': 'todos'}], value=5),
                dbc.Col([dcc.Graph(id="vendasPorUfMes"),], sm=6),
                dbc.Col([dcc.Graph(id="vendasPorStatusMes")], sm=6),
                    ]),
               
            ]),

        
                dbc.Row(
            children=[
                html.H3('Dados Gerais'),
                dbc.Col([              
                    dbc.Row([
                    dbc.Col([dbc.Card([
                        dbc.CardBody([
                            html.Span("Contagem de Vendas Total", className='cardText'),
                            html.H3("CARREGANDO...", id='contagemVendas'),
                            html.Span("Nos ultimos 6 meses", className="cardText"),
                            html.H3("CARREGANDO...", id='vendas6Meses')
                        ])
                    ])], md=4),
                    
                        dbc.Col([dbc.Card([
                        dbc.CardBody([
                            html.Span("Total das Vendas em R$", className='cardText'),
                            html.H3("CARREGANDO...", id='valorVendas'),
                        ])
                    ])], md=4),
                            
                         dbc.Col([dbc.Card([
                            dbc.CardBody([
                                html.Span("Contagem de Cancelamentos", className='cardText'),
                                html.H3("CARREGANDO...", id='contagemCancelas'),
                                html.Span("Estado com mais Vendas", className='cardText'),
                                html.H3("CARREGANDO...", id='estadoMaisVendas')
                        ])
                    ])], md=4),
                ]),
                    dbc.Row([html.Div([
                        dbc.Card([
                            dbc.CardBody([
                                html.Span('Número de Vendas por UF'),
                            dcc.RadioItems(id='vendasFilter', options=[
                                {'label': 'Top 5', 'value': 5},
                                {'label': 'Top 10', 'value': 10},
                                {'label': 'Top 15', 'value': 15},
                                {'label': 'Todos', 'value': 'todos'}]),
                          dbc.Row([dcc.Graph(id="vendasPorUf")])])])
                        
                    ])
                    ])
                    ], md=5),
                dbc.Col([
                    dbc.Row([
                        dbc.Col([dbc.Card(dbc.CardBody(dcc.Graph(id="vendas4Meses")))]),
                        dbc.Col([dbc.Card(dbc.CardBody(dcc.Graph(id="vendasPorStatus")))], sm=6),
                        ]),
                    dbc.Row([ 
                             html.Div(dbc.Card(dbc.CardBody(dcc.Graph(id="vendasPorFaixaEtária"))))
                    ]),
                ], md=7),
                dbc.Row([
                            dbc.Col([dbc.Card([
                                dbc.CardBody([
                                    html.H5(['Estados']),
                                    dcc.Checklist(
                                        id="ufCheck",
                                        options=dfFiltered.UF.dropna().unique(),
                                        inline=False,
                                                  ), 
                                    dbc.Row([html.Div('Top 5 Vendas entre Cidades'),
                                        dcc.Graph(id='topCidades')
                                    ]) 
                                    ])
                                ])
                    ], md=5),
                    dbc.Col(dbc.Card(dbc.CardBody(dcc.Graph(id='cidades'))), md=7),
            ])
            ]
        ),
    html.Div(id='bottom'),], fluid=True
)


# ===========================================
# Logic
@app.callback([
    Output("contagemVendasMes", 'children'),
    Output("valorVendasMes", 'children'),
    Output("contagemCancelasMes", 'children'),
    Output("estadoMaisVendasMes", 'children'),  
    Output("vendasPorStatusMes", 'figure'),
    Output("vendasPorUfMes", 'figure'),
    Output("vendasPorFaixaEtáriaMes", 'figure'),
    Output('contagemQuitadasMes', 'children'),
    Output('mesLabel', 'children') 
], [
    Input("empresa-button", "children"),
    Input("mesCheck", "value"),
    Input('vendasFilterMes', 'value')])
def displayMonthFilter(empresa, mesFilter, vendasFilter):
    dfFodder = dfFiltered
    dfFodder['DataVenda'] = monthsYearSeries
    dfMonthFilter = dfFodder[dfFodder['DataVenda']==mesFilter]
    
    # Transformar Numero do Mes em Nome
    mesLabel = 'Dados Mensais de ' + datetime.strptime(mesFilter, '%m-%y').strftime('%B/%Y').capitalize()
    mesLabel.capitalize()
    # Total de Rows StatusDaVendaUAU
    contagemVendasMes = dfMonthFilter.shape[0]
    # Total Cancelamento
    contagemCancelasMes = dfMonthFilter[dfMonthFilter['StatusSQL']=='Cancelada'].count().values[0]
    
    # Total Quitadas do Mês
    contagemQuitadasMes = dfMonthFilter[dfMonthFilter['StatusDaVendaUAU']=='3 - Quitado'].count().values[0]

    # Soma Total Vendas
    somaVendasMes = int(dfMonthFilter['TotalVenda'].sum())
    valorVendasMes = f"{somaVendasMes:0,.2f}"
    
    # Lista de Maiores UF por vendas
    dfVendasUfCountMes = dfMonthFilter.groupby(['UF']).count()
    dfSort = dfVendasUfCountMes.sort_values(['Obra'], ascending=False).head(3)
    estadoMaisVendasMes = ", ".join(dfSort.index.values)
    
    # Pie graph vendas por UF top 10
    dfVendasUf = dfMonthFilter.groupby(['UF']).count()
    vendasDataframeMes = pd.DataFrame({'UF': dfVendasUf.index, 'Vendas': dfVendasUf['Obra']})
    if (type(vendasFilter) != int):
        vendasSortMes = vendasDataframeMes.sort_values(['Vendas'], ascending=False).head(5)
        if (type(vendasFilter) == str):
            vendasSortMes = vendasDataframeMes.sort_values(['Vendas'], ascending=False)
    else:
        vendasSortMes = vendasDataframeMes.sort_values(['Vendas'], ascending=False).head(vendasFilter)
            
    vendasPorUfMes = px.pie(vendasSortMes, values='Vendas', names='UF',  hole=.5)
    
    
    
    # Pie graph cancelados/ativos/quitados
    countCanceladosMes = dfMonthFilter.groupby(['StatusDaVendaUAU']).count()
    dfCanceladosMes = pd.DataFrame({'Status': countCanceladosMes.index, 'Count': countCanceladosMes['Obra']})
    vendasPorStatusMes = px.pie(dfCanceladosMes, values='Count', names='Status', title='Número de Vendas por Status')
    
    # Vendas por faixa etária
    ranges = [18,25,30,35,40,45,50,55,60,100]
    labels = ['18-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60-100']
    
    yearNowMes = int(datetime.now().strftime('%Y'))
    dfYearMes = pd.to_datetime(dfMonthFilter['DataNascimento'], dayfirst=True)
    dfBirthMes = dfYearMes.dt.year
    dob = dfBirthMes.apply(lambda x : (yearNowMes - x))
    cutMes = pd.cut(dob, ranges)
    cutMes.cat.rename_categories(labels, inplace=True)
    ageGroupMes = dob.groupby(cutMes).count()
    ageGroupMes = ageGroupMes.rename('vendasCount', inplace=True)
    vendasPorFaixaEtáriaMes = px.bar(ageGroupMes, x=ageGroupMes.index, y='vendasCount', title='Quantia de Vendas por Grupo de Idade', color='vendasCount')

    return (
        contagemVendasMes,
        valorVendasMes,
        contagemCancelasMes,
        estadoMaisVendasMes,
        vendasPorStatusMes,
        vendasPorUfMes,
        vendasPorFaixaEtáriaMes,
        contagemQuitadasMes,
        mesLabel,
    )

@app.callback([
    Output("contagemVendas", 'children'),
    Output("vendas6Meses", 'children'),
    Output("valorVendas", 'children'),
    Output("contagemCancelas", 'children'),
    Output("estadoMaisVendas", 'children'),  
], [
    Input("empresa-button", "children")])
def displayCards(empresa):
    # Total de Rows
    numVendas = dfFiltered.shape[0]
    
    # Vendas em 6 Meses
    time6Month = (datetime.now() - timedelta(days=180)).strftime('%Y-%m-%d')
    vendas6MesesFilter = dfFiltered[pd.to_datetime(dfFiltered['DataVenda'], format='%Y-%m-%d') > time6Month]
    vendas6MesesCount = vendas6MesesFilter.count().values[0]
    
    # Total Cancelamento
    contagemCancelamento = dfFiltered[dfFiltered['StatusSQL']=='Cancelada'].count().values[0]
    
    # Soma Total Vendas
    somaVendas = int(dfFiltered['TotalVenda'].sum())
    totalVendas = f"{somaVendas:0,.2f}"
    
    # Lista de Maiores UF por vendas
    dfVendasUfCount = dfFiltered.groupby(['UF']).count()
    dfSort = dfVendasUfCount.sort_values(['Obra'], ascending=False).head(3)
    ufMaior = ", ".join(dfSort.index.values)
    

    return (
        numVendas,
        vendas6MesesCount,
        totalVendas,
        contagemCancelamento,
        ufMaior,
    )
    
    
@app.callback([    
    Output("vendas4Meses", 'figure'),
    Output("vendasPorStatus", 'figure'),
    Output("vendasPorUf", 'figure'),
    Output("vendasPorFaixaEtária", 'figure'),  
    ], [Input("empresa-button", "children"),
        Input('vendasFilter', 'value')])
def displayGraphs(empresa, vendasFilter):

    # Pie graph vendas por UF top 10
    dfVendasUf = dfFiltered.groupby(['UF']).count()
    vendasDataframe = pd.DataFrame({'UF': dfVendasUf.index, 'Vendas': dfVendasUf['Obra']})

    if (type(vendasFilter) != int):
        vendasSort = vendasDataframe.sort_values(['Vendas'], ascending=False).head(5)
        if (type(vendasFilter) == str):
            vendasSort = vendasDataframe.sort_values(['Vendas'], ascending=False)
    else:
        vendasSort = vendasDataframe.sort_values(['Vendas'], ascending=False).head(vendasFilter)
        
    vendasPorUfPie = px.pie(vendasSort, values='Vendas', names='UF',  hole=.5)
    
    # Pie graph cancelados/ativos/quitados
    countCancelados = dfFiltered.groupby(['StatusDaVendaUAU']).count()
    dfCancelados = pd.DataFrame({'Status': countCancelados.index, 'Count': countCancelados['Obra']})
    vendasPorStatus = px.pie(dfCancelados, values='Count', names='Status', title='Número de Vendas por Status')
    
    # Vendas nos ultimos 4 meses
    monthsYearSeriesTest = dfCopy['DataVenda'].apply(lambda x: datetime.strptime(x, '%m-%y').strftime('%Y-%m')) 
    dfMonthsYearTest = pd.DataFrame({'DataVenda': monthsYearSeriesTest})
    time4Months = (datetime.now() - timedelta(days=120)).strftime('%Y-%m')
    dfVendasMês = dfFiltered[dfMonthsYearTest['DataVenda'] > time4Months]
    dfMonthYear = dfVendasMês['DataVenda'].apply(lambda x: datetime.strptime(x, '%m-%y').strftime('%m-%y')) 
    dfVendasMês['DataVenda'] = dfMonthYear
    vendas4Meses = dfVendasMês.groupby(['DataVenda']).count()
    vendas4MesesDf = pd.DataFrame({'DataVendas': vendas4Meses.index, 'Vendas': vendas4Meses['Obra']})

    vendas4Meses = px.bar(vendas4MesesDf, x='DataVendas', y="Vendas", color="DataVendas", title='Quantidade de Vendas nos Últimos 3 Meses')  

    # Vendas por faixa etária
    ranges = [18,25,30,35,40,45,50,55,60,100]
    labels = ['18-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60-100']
    
    yearNow = int(datetime.now().strftime('%Y'))
    dfYear = pd.to_datetime(dfFiltered['DataNascimento'], dayfirst=True)
    dfBirth = dfYear.dt.year
    dob = dfBirth.apply(lambda x : (yearNow - x))
    
    
    cut = pd.cut(dob, ranges)
    cut.cat.rename_categories(labels, inplace=True)
    ageGroup = dob.groupby(cut).count()
    ageGroup = ageGroup.rename('vendasCount', inplace=True)
    vendasPorFaixaEtária = px.bar(ageGroup, x=ageGroup.index, y='vendasCount', title='Quantia de Vendas por Grupo de Idade', color='vendasCount')

    return (
        vendas4Meses,
        vendasPorStatus,
        vendasPorUfPie,
        vendasPorFaixaEtária

    )



@app.callback([ 
    Output("topCidades", 'figure'), 
    Output("cidades", 'figure'), 
    ], [Input("ufCheck", "value")])
def displayCities(ufCheck):
    
    if ufCheck != None:
        dfUf = dfFiltered[dfFiltered.UF.isin(ufCheck)]
        ufCountList = dfUf.groupby(['Cidade'], group_keys=True)['UF'].apply(list)
        citiesDataFrame = pd.DataFrame({'Cidades': ufCountList.index, 'UF': ufCountList.values})
        citiesDataFrame["Vendas"] = citiesDataFrame["UF"].str.len()
        citiesDataFrame["UF"] = citiesDataFrame["UF"].str[0]

    else:
        dfUf = dfFiltered[dfFiltered.UF.isin(['PR'])]
        ufCountList = dfUf.groupby(['Cidade'])['UF'].apply(list)
        citiesDataFrame = pd.DataFrame({'Cidades': ufCountList.index, 'UF': ufCountList.values})
        citiesDataFrame["Vendas"] = citiesDataFrame["UF"].str.len()
        citiesDataFrame["UF"] = citiesDataFrame["UF"].str[0]

    
    topCidades = citiesDataFrame.sort_values(['Vendas'], ascending=False).head(5)
    topCidadesFig = px.pie(topCidades, values='Vendas', names='Cidades')
    
    citiesFig = px.bar(
        citiesDataFrame,
        x='Cidades',
        y='Vendas',
        title='Número de Vendas por Cidade',
        color='UF'
    )
    return (
        topCidadesFig,
        citiesFig,
        )
    
if __name__ == '__main__':
    print("Carregando...")
    app.run_server(debug=True, port=8060)