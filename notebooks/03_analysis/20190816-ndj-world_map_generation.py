#!/usr/bin/env python
# coding: utf-8

# In[1]:


import folium
from folium.plugins import MarkerCluster
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

src_dir = os.path.join(os.getcwd(), '..', '..', 'src')
sys.path.append(src_dir)
pd.set_option('display.max_columns', None)


# In[2]:


map_data = pd.read_pickle('../../data/02_intermediate/kick_World_map.pkl')


# In[3]:


map_data.head()


# In[4]:


locations = list(zip(map_data.lat, map_data.lng))
popup_content = list(zip(map_data.name, map_data.backers_count, map_data.goal, map_data.sub_category))
popups = ['<center> {} <br>  <b>Category:</b> {} <br><b>Goal:</b> ${} <br> <b>BackerCount: </b> {}  </center>'.format(name, category, goal, count) for (name, count, goal, category) in popup_content]

len(popups)


# In[7]:


m = folium.Map(location=[map_data.lat.mean(), map_data.lng.mean()], zoom_start=5)

marker_cluster = MarkerCluster(
    name='Global Kickstarter Campaigns',
    overlay=True,
    control=True,
    icon_create_function=None
)

for k in range(len(locations)):
    location = locations[k][0], locations[k][1]
    marker = folium.Marker(location=location)
    popup = popups[k]
    folium.Popup(popup, max_width='150%').add_to(marker)
    if list(map_data.state)[k] == 'live':
        icons = folium.Icon(color='lightgreen', icon='bullhorn').add_to(marker)
    elif list(map_data.state)[k] == 'successful':
        icons = folium.Icon(color='green', icon='ok-sign').add_to(marker)
    else:
        icons = folium.Icon(color='red', icon='remove-sign').add_to(marker)
    marker_cluster.add_child(marker)

marker_cluster.add_to(m)
folium.LayerControl().add_to(m)

m.save(os.path.join('../../results', 'WorldKickStarterProjects_All.html'))


# In[ ]:




