import folium
import pandas as pd
import os
import sys
import functools

src_dir = os.path.join(os.getcwd(), '..', '..', 'src')
sys.path.append(src_dir)


m = folium.Map(location=[map_data.lat.mean(), map_data.lng.mean()], zoom_start=5)

marker_cluster = MarkerCluster(
    name='US Kickstarter Campaigns',
    overlay=True,
    control=True,
    icon_create_function=None
)

for k in range(1000):
    location = locations[k][0], locations[k][1]
    marker = folium.Marker(location=location)
    popup = popups[k]
    folium.Popup(popup, max_width='150%').add_to(marker)
    if list(df.state)[k] == 'live':
        icons = folium.Icon(color='lightgreen', icon='bullhorn').add_to(marker)
    elif list(df.state)[k] == 'successful':
        icons = folium.Icon(color='green', icon='ok-sign').add_to(marker)
    else:
        icons = folium.Icon(color='red', icon='remove-sign').add_to(marker)
    marker_cluster.add_child(marker)

marker_cluster.add_to(m)

folium.LayerControl().add_to(m)

m.save(os.path.join('results', 'USfastClusterTEST.html'))