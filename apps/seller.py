#import packages to create app
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from app import app
import dash_extensions as de

# external_stylesheets = [dbc.themes.SLATE]
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

myntra = pd.read_csv('myntra_cleaned.csv')
df5 = pd.DataFrame(myntra['seller_state'].value_counts())
df5 = df5.reset_index()
df5 = df5.rename(columns = {'index':'Seller_State','seller_state':'Count'})

df6 = pd.DataFrame(myntra['seller_city'].value_counts(ascending=False)[:10])
df6 = df6.reset_index()
df6 = df6.rename(columns = {'seller_city':'Count','index':'Seller_City'})

mstate = myntra['seller_state'].value_counts(ascending=False).index[0]
mcity = myntra['seller_city'].value_counts(ascending=False).index[0]

df7 = pd.DataFrame(myntra.groupby('seller_state')['brand_name'].value_counts())
df7 = df7.rename(columns={'brand_name':'Count'})
df7 = df7.reset_index()

stateName = list(df7['seller_state'].unique())

df8 = pd.DataFrame(myntra.groupby(['seller_state','seller_city'])['tags'].value_counts())
df8 = df8.rename(columns={'tags':'Count'})
df8 = df8.reset_index()

fig5 = px.choropleth(
    df5,
    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
    featureidkey='properties.ST_NM',
    locations='Seller_State',
    color='Count',
    color_continuous_scale='sunset'
)

fig5.update_geos(fitbounds="locations", visible=False)
fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0}, geo={'landcolor' :'lightgray','showland' : True, 'showcountries' : True, 'countrycolor':'gray'},
                   paper_bgcolor="#95A5A6",plot_bgcolor='#95A5A6',font_color='#040B3E')

url5 = "https://assets3.lottiefiles.com/packages/lf20_iZLiB2fKa1.json"
url6 = "https://assets3.lottiefiles.com/packages/lf20_jif9vljs.json"
options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

layout = html.Div([
    dbc.Container([
        html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Row([
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody([
                                    html.Div(de.Lottie(options=options, url=url6),style={"height": "300px", "width": "270px"}),
                                    html.H4("State with most Sellers", className="card-title",style={'color':'#030303'}),
                                    html.H5(mstate, className="card-text",style={'color':'#E74C3C','font-family':'Bruno Ace SC, cursive'})
                                ]),
                                color="#DDF133"
                            )
                        ], width=3),
                        dbc.Col([
                            dbc.Card(
                                dbc.CardBody([
                                    html.Div(de.Lottie(options=options, url=url5),style={"height": "300px", "width": "300px"}),
                                    html.H4("City with most Sellers", className="card-title",style={'color':'#030303'}),
                                    html.H5(mcity, className="card-text",style={'color':'#E74C3C','font-family':'Bruno Ace SC, cursive'})
                                ]),
                                color="#DDF133"
                            )
                        ], width=3),
                         dbc.Col([
                            dbc.Card(
                                dbc.CardBody([dcc.Graph(id="graph6", style={"height": "360px"})]),
                                style={"height": "393px"},
                                color="#DDF133"
                            )
                        ], width=6)
                    ]),
                    dbc.Row([
                        dbc.Container([
                            html.Div([
                                dbc.Row([
                                    dbc.Col([
                                        html.H4("Seller Density in different states", style={'color':'#03032E'}),
                                        dcc.Graph(id='mapfig',figure=fig5)
                                    ], width=6),
                                    dbc.Col([
                                        html.H4("Top-10 Cities based on count", style={'color':'#03032E'}),
                                        dbc.Table.from_dataframe(df6, striped=True, bordered=True, hover=True, className='table-success')
                                    ], width=6)
                                ], className="my-3",style={'padding-bottom':'10px'})    
                            ])
                        ]),
                    ])
                ])
            ],style={'padding-top':'10px', 'padding-bottom':'10px'}),
            dbc.Row([
                dbc.Col([
                    dbc.Row(
                        html.Div([
                            html.Label('Select State',style={'color':'#303037','font-size': '20px', 'padding-bottom':'5px'}),
                            dcc.Dropdown(id='state_dropdown', options=[{'label': i, 'value': i} for i in stateName],
                            value=['Uttar Pradesh', 'Maharashtra'],
                            multi=True
                            )
                        ],style={'width': '100%', 'display': 'inline-block','padding-bottom':'15px'})
                    ),
                    dbc.Row([
                        html.Div([
                            html.H4("Number of Brands Sold in Different States", style={'color':'#03032E'}),
                            dcc.Graph(id="graph5")
                        ],style={'width': '100%','padding-bottom':'25px'})
                    ])
                ])
            ])
        ])
    ])
])

@app.callback([Output("graph5", "figure"),Output("graph6", "figure")],
        Input("state_dropdown", "value"))
def generated_chart2(state):
    if not state:
        dash.no_update
    mask3 = df7.seller_state.isin(state)
    mask4 = df8.seller_state.isin(state)
    fig7 = go.Figure(layout=go.Layout(paper_bgcolor="#95A5A6",plot_bgcolor='#95A5A6'))
    fig7.add_trace(go.Bar(x=df7[mask3]['brand_name'], y=df7['Count']))
    fig7.update_layout(font_color='#040B3E')
    fig8 = px.treemap(df8[mask4], path=['seller_state', 'seller_city', 'tags'], values='Count',color_continuous_scale='RdBu', title='Location Tree Map')
    fig8.update_layout(font_color='#040B3E', paper_bgcolor="rgba(0,0,0,0)", autosize=False, width=650, height=400,)
    return([fig7, fig8])