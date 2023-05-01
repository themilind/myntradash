# Import necessary libraries
import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app import app
from apps import home, products, seller
# external_stylesheets = [dbc.themes.SLATE]
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row([
                    dbc.Col(
                        html.A(html.Img(src='/assets/myntra.svg', height="40px",),href="/home")),
                        dbc.Col(dbc.NavbarBrand("Myntra",className='ms-2',style={'color':'#F9953D','font-family':'Ultra, serif'}))
                ],
                align='center',
                className='g-0'
                ),
            dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Home", active='exact', href="/home")),
                        dbc.NavItem(dbc.NavLink("Products", active='exact', href="/products")),
                        dbc.NavItem(dbc.NavLink("Seller", active='exact', href="/seller")),
                    ],
                    className="me-auto",
                    navbar=True,
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
            dbc.Row([
                    dbc.Col(
                        dbc.Nav([
                            dbc.NavItem(dbc.NavLink(html.Img(src='/assets/internet.png', height="30px"), href="https://www.myntra.com/",external_link=True, target="_blank"))
                        ]),
                    ),
                    dbc.Col(
                        dbc.Nav([
                            dbc.NavItem(dbc.NavLink(html.Img(src='/assets/icons8-twitter.svg', height="30px"), href="https://twitter.com/myntra",external_link=True, target="_blank"))
                        ]),
                    ),
                    dbc.Col(
                        dbc.Nav([
                            dbc.NavItem(dbc.NavLink(html.Img(src='/assets/playstore.svg', height="30px"), href="https://play.google.com/store/apps/details?id=com.myntra.android&hl=en&gl=US",external_link=True, target="_blank"))
                        ]),
                    )
                ])
        ]
    ),
    color="dark",
    dark=True,
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content', style={'backgroundColor': '#C0DFF3'})
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/products':
        return products.layout
    elif pathname == '/seller':
        return seller.layout
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(port = 8090, debug=True)
