import COVID19Py
import pandas as pd
import folium

covid19 = COVID19Py.COVID19()

locations = covid19.getLocations()

df = pd.DataFrame(locations)

data = pd.DataFrame(columns=["Country", "Lat", "Lon", "Cases"])

for i in range(len(df)):
    
    tmp = {"Lat":float(df.iloc[i]['coordinates']['latitude']),
          "Lon": float(df.iloc[i]['coordinates']['longitude']),
          "Cases":df.iloc[i]['latest']['confirmed'],
          "Country":df.iloc[i]['country']}
    
    data = data.append(tmp, ignore_index=True)

m = folium.Map(location=[20,0], zoom_start=2)

def plot(name,lat,longi, r):
    global folium, m

    x=folium.Circle([lat,longi],
              radius=r*5,
              popup=(name + " Cases " + str(r)),
              icon=folium.Icon(color='red'),
              color='crimson',
              fill=True,
              fill_color='crimson')
    
    x.add_to(m)

for i in range(len(data)):
    name = data.iloc[i]["Country"]
    lat = data.iloc[i]["Lat"]
    longi = data.iloc[i]["Lon"]
    r = data.iloc[i]["Cases"]
    
    plot(name, lat, longi, r)

m.save("COVID19_World_map.html")

import os

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H1("Map"),
    html.Iframe(id='map', srcDoc=open("COVID19_World_map.html", 'r').read(), width="100%",   height="600")

])



if __name__ == '__main__':
    app.run_server(debug=True)
