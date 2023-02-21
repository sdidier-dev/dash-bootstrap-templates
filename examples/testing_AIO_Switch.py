from dash import Dash, dcc, html
from dash_bootstrap_templates import ThemeSwitchAIO, ThemeChangerAIO
import dash_bootstrap_components as dbc

app = Dash(__name__)

app.layout = html.Div([ThemeSwitchAIO(aio_id='theme',
                                      ), 'testing', dbc.Button()], id='testing')

app.run(debug=True)