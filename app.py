# Import required libraries
import os
from random import randint

import folium
import chart-studio.plotly as py
from plotly.graph_objs import *
import flask
import dash
from dash.dependencies import Input, Output, State, Event
import dash_core_components as dcc
import dash_html_components as html

server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("Map"),
    html.Iframe(id='map', src="https://raw.githubusercontent.com/Anpr1211/Apps-on-heroku/master/COVID19_World_map.html", width="100%",   height="600")

])


# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
