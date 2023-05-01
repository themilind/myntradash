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

url1 = "https://assets1.lottiefiles.com/packages/lf20_XfP3DqlQEa.json"
url2 = "https://assets1.lottiefiles.com/private_files/lf30_u4mgmpw4.json"
url3 = "https://assets9.lottiefiles.com/packages/lf20_cUA1qFmScz.json"
url4 = "https://assets4.lottiefiles.com/packages/lf20_o02kdakv.json"

options = dict(loop=True, autoplay=True, rendererSettings=dict(preserveAspectRatio='xMidYMid slice'))

myntra = pd.read_csv('myntra_cleaned.csv')
df1 = myntra.groupby(['tags', 'product_tag']).size().reset_index(name='count')
t1 = [{'label': tag, 'value': tag} for tag in df1['tags'].unique()]

bbrand = myntra.groupby('brand_name')['rating'].mean().sort_values(ascending=False).index[0].upper()
mbrand = myntra.groupby('brand_name')['rating_count'].mean().sort_values(ascending=False).index[0].upper()
dbrand = myntra.groupby('brand_name')['discount_percent'].mean().sort_values(ascending=False).index[0]
btag = myntra.groupby('tags')['rating'].mean().sort_values(ascending=False).index[1].upper()

layout = html.Div([
    dbc.Container([
        html.Div([
            dbc.Row([
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody([
                            html.Div(de.Lottie(options=options, url=url1),style={"height": "300px", "width": "270px"}),
                            html.H4("Highest Rated Brand", className="card-title",style={'color':'#030303'}),
                            html.H5(bbrand, className="card-text",style={'color':'#E74C3C','font-family':'Bruno Ace SC, cursive'})
                        ]),
                    color="#DDF133"
                    )
                ], width=3),
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody([
                            html.Div(de.Lottie(options=options, url=url2),style={"height": "300px", "width": "300px"}),
                            html.H4("Most Rated Brand", className="card-title",style={'color':'#030303'}),
                            html.H5(mbrand, className="card-text",style={'color':'#E74C3C','font-family':'Bruno Ace SC, cursive'})
                        ]),
                    color="#DDF133"
                    )
                ], width=3),
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody([
                            html.Div(de.Lottie(options=options, url=url3),style={"height": "300px", "width": "300px"}),
                            html.H4("Most Discounted Brand", className="card-title",style={'color':'#030303'}),
                            html.H5(dbrand, className="card-text",style={'color':'#E74C3C','font-family':'Bruno Ace SC, cursive'})
                        ]),
                    color="#DDF133"
                    )
                ], width=3),
                dbc.Col([
                    dbc.Card(
                        dbc.CardBody([
                            html.Div(de.Lottie(options=options, url=url4),style={"height": "300px", "width": "300px"}),
                            html.H4("Highest Rated Category", className="card-title",style={'color':'#030303'}),
                            html.H5(btag, className="card-text",style={'color':'#E74C3C','font-family':'Bruno Ace SC, cursive'})
                        ]),
                    color="#DDF133"
                    )
                ], width=3),
            ],style={'padding-top':'10px','padding-bottom':'35px'})
        ])
    ]),
    dbc.Container([
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.H4("Tags & Product Tags", style={'color':'#03032E'}),
                    dcc.Graph(id="graph1")
                    ], width=6),
                dbc.Col([
                    html.H4("Analysis of Product Tags", style={'color':'#03032E'}),
                    dcc.Graph(id="graph2")
                    ], width=6),
                html.Div([html.Label("Tags:", style={'color':'#303037','font-size': '20px', 'padding-top': '15px', 'padding-bottom':'5px'}),
                    dcc.Dropdown(id="tags", options=t1, value='clothing', clearable=False, style={'width':'50%'})
                    ])
            ], className="my-3",style={'padding-bottom':'35px'})    
        ])
    ]),
    dbc.Container([
        html.Div([
            dbc.Row([
                dbc.Col([
                    html.H4("Ratings Vs Rating Count", style={'color':'#03032E'}),
                    dcc.Graph(id="graph3")
                    ], width=6),
                dbc.Col([
                    html.H4("Marked Price Vs Discounted Price", style={'color':'#03032E'}),
                    dcc.Graph(id="graph4")
                    ], width=6),
                html.Div([html.Label("Suitable For:",style={'color':'#303037','font-size': '20px', 'padding-top': '15px', 'padding-bottom':'5px'}),
                        dbc.Checklist(
                            options=[
                                    {"label": html.Div(['Women'], style={'color': '#303037', 'font-size': '15px'}), "value": "women", "disabled": False},
                                    {"label": html.Div(['Men'], style={'color': '#303037', 'font-size': '15px'}), "value": "men", "disabled": False},
                                    {"label": html.Div(['Girls'], style={'color': '#303037', 'font-size': '15px'}), "value": "girls", "disabled": False},
                                    {"label": html.Div(['Boys'], style={'color': '#303037', 'font-size': '15px'}), "value": "boys", "disabled": False},
                                    {"label": html.Div(['Unisex'], style={'color': '#303037', 'font-size': '15px'}), "value": "unisex", "disabled": False},
                            ],
                            value=["women",'men','girls','boys','unisex'],
                            id="checkboxes",
                            switch=True,
                            inline=True,
                        ),
                ])
            ], style={'padding-bottom':'35px'})    
        ])
    ])
])

@app.callback(
        [Output("graph1", "figure"), Output("graph2", "figure")],
        Input("tags", "value"))
def generate_chart(tags):
    if not tags:
        dash.no_update
    filtered_df = df1[df1['tags'] == tags]
    fig1 = px.sunburst(filtered_df, path=['tags', 'product_tag'], values='count')
    fig1.update_layout( paper_bgcolor="#95A5A6",plot_bgcolor='#95A5A6',font_color='#040B3E')
    fig2 = px.bar(filtered_df, x='product_tag', y='count')
    fig2.update_layout(xaxis_title='Product Tags', yaxis_title='Counts', paper_bgcolor="#95A5A6",plot_bgcolor='#95A5A6',font_color='#040B3E')
    return([fig1, fig2])

@app.callback(
    [Output("graph3","figure"),Output("graph4","figure")],
    Input("checkboxes","value"))
def generate_chart1(gender):
    if not gender:
        dash.no_update
    df2 = myntra[myntra['rating'] != 0]
    mask = df2.suitable_for.isin(gender)
    fig3 = px.scatter(df2[mask], x="rating", y="rating_count", size='discount_percent', hover_data=['brand_name','tags','product_tag'])
    fig3.update_layout(xaxis_title='Ratings', yaxis_title='Rating Counts', paper_bgcolor="#95A5A6",plot_bgcolor='#95A5A6',font_color='#040B3E')
    df3 = myntra.groupby(['tags','suitable_for'])['marked_price'].mean()
    df3 = df3.reset_index()
    df4 = myntra.groupby(['tags','suitable_for'])['discounted_price'].mean()
    df4 = df4.reset_index()
    mask1 = df4.suitable_for.isin(gender)
    mask2 = df3.suitable_for.isin(gender)
    fig4 = go.Figure(layout=go.Layout(paper_bgcolor="#95A5A6",plot_bgcolor='#95A5A6'))
    fig4.add_trace(go.Bar(x=df4[mask1]['tags'], y=df4['discounted_price'], name='Discounted Price'))
    fig4.add_trace(go.Bar(x=df3[mask2]['tags'],y=df3['marked_price'], name = 'Marked Price'))
    fig4.update_layout(font_color='#040B3E')
    return([fig3, fig4])

# if __name__ == '__main__':
#     app.run_server(debug=True)