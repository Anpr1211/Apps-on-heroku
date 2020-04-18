import dash
import dash_core_components as dcc
import dash_html_components as html
import folium

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Map"),
    html.Iframe(id='map', srcDoc=open("COVID19_World_map.html", 'r').read(), width="100%",   height="600")

])

if __name__ == '__main__':
    app.run_server(debug=True)
