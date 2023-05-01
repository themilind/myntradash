# Import necessary libraries
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app

# external_stylesheets = [dbc.themes.SLATE]
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Myntra Dashboard", className='border p-1 mb-2 text-center', 
                            style={'color':"#F47708","border-color": "#3C565B", "background-color": "#3C565B","border-width": "2px","font-family": "'Russo One', sans-serif"},
                            )
                    ),
        ]),
        dbc.Row([
            dbc.CardGroup([
                dbc.Card([
                    dbc.CardImg(src="/assets/myntra1.jpg", top=True),
                        dbc.CardBody([
                            html.H4("About Myntra", className="card-title"),
                            html.P(
                                "Myntra is a major Indian fashion e-commerce company headquartered in Bengaluru, Karnataka, India.The company was founded in 2007-2008" 
                                " to sell personalized gift items. In May 2014, Myntra.com was acquired by Flipkart.",
                                className="card-text",
                            ),
                            dbc.Button("Myntra/About", color="success",href="https://www.myntra.com/aboutus",external_link=True, target="_blank"),
                        ]),
                ],
                color='warning',
                inverse=True
                ),
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Highlights", className="card-title"),
                        html.P("Total Funding: $534 mn",className="card-text",),
                        html.P("Revenue : $420.7 mn",className="card-text",),
                        html.P("Valuation : $1.2 bn",className="card-text",),
                        dbc.Button("Go to Wikipedia", color="success",href="https://en.wikipedia.org/wiki/Myntra",external_link=True, target="_blank"),
                        ]),
                    dbc.CardImg(src="/assets/myntra3.jpg", bottom=True),
                ],
                color='warning',
                inverse=True
                ),
            ])
        ]),
        dbc.Row([
            dbc.CardGroup([
                dbc.Card([
                    dbc.Row([
                        dbc.Col(
                            dbc.CardImg(
                                    src='/assets/mukesh.jpg',
                                    className="img-fluid rounded-start",
                            ),
                            className="col-md-4",
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H3("Founder", className="card-title"),
                                    html.P("Mukesh Bansal established Myntra in 2007 along with Ashutosh Lawania and Vineet Saxena.", className="card-text"),
                                ],
                                className="col-md-8",
                            )
                        )
                    ],
                    className="g-0 d-flex align-items-center"
                    )
                    ],
                    color='info',
                    inverse=True
                    ),
                dbc.Card([
                    dbc.Row([
                        dbc.Col(
                            dbc.CardImg(
                                    src='/assets/nandita.jpg',
                                    className="img-fluid rounded-start",
                            ),
                            className="col-md-4",
                        ),
                        dbc.Col(
                            dbc.CardBody(
                                [
                                    html.H3("CEO", className="card-title"),
                                    html.P("Nandita Sinha became the Chief Executive Officer of Myntra on January 1, 2022.", className="card-text"),
                                ],
                                className="col-md-8",
                            )
                        )
                    ],
                    className="g-0 d-flex align-items-center"
                    )
                    ],
                    color='info',
                    inverse=True,
                    ),
            ],
            style={"padding-top": "40px"}
            )
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Carousel(
                        items=[
                            {"key": "1", "src":"/assets/myntra2.jpg","img_style":{"width":"1400px","height":"200px" }, "imgClassName": ""},
                            {"key": "2", "src":"/assets/myntra4.jpg","img_style":{"width":"1300px","height":"200px" }, "imgClassName": ""},
                            {"key": "3", "src":"/assets/myntra5.jpg","img_style":{"width":"1400px","height":"200px" }, "imgClassName": ""},
                        ],
                    controls=False,
                    indicators=True,
                    interval=3000,
                    ride="carousel",
                    variant='dark'
                )
            ],  width=12,
                className="mt-3",
                style={"padding-bottom": "20px"}
            )
        ])
    ])
])