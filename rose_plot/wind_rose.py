import plotly.express as px
import pandas as pd


df = pd.read_csv('wind_dat_sorted.csv')
fig = px.bar_polar(df, r="frequency", theta="direction", \
                   color="strength", template="plotly", \
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
#fig.show()

import os

if not os.path.exists("images"):
    os.mkdir("images")
    
fig.write_image("images/plotly_rose.png")