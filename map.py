import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def colour_producer(elevation):
    if elevation >= 3000:
        return 'orange'
    elif 1500 <= elevation < 3000:
        return 'blue'
    else:
        return 'green'


map = folium.Map([47.599408, -122.323562], zoom_start=4, tiles="Mapbox Bright")

fg_volcanoes = folium.FeatureGroup(name="America's Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    loc = (lt, ln)
    fg_volcanoes.add_child(folium.CircleMarker(location=loc, radius=6, popup=str(
        el)+"m",
                                     fill_color=colour_producer(el),
                                     color='grey', fill=True, fill_opacity=0.8))


fg_population = folium.FeatureGroup(name="Population and borders")


fg_population.add_child(folium.GeoJson(data=open('world.json', 'r',
                                      encoding='utf-8-sig').read(),
                            style_function=lambda x: {'fillColor': 'green'
                            if x['properties']['POP2005'] < 10000000 else
                            'yellow'}))

map.add_child(fg_volcanoes)
map.add_child(fg_population)
map.add_child(folium.LayerControl())


map.save("first_map.html")
