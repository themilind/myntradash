import dash
import dash_bootstrap_components as dbc

external_stylesheets = ['https://fonts.googleapis.com/css2?family=Bruno+Ace+SC&family=Russo+One&family=Sigmar&family=Ultra&display=swap',
                        dbc.themes.UNITED]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True
app.css.config.serve_locally = True
