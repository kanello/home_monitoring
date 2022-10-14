import plotly.express as px
import pandas as pd
import pipeline.connections as cons

df = cons.fromSqlite("select * from internet_speeds;")


fig = px.scatter(df, x="timestamp", y="ping")

# fig = px.scatter(df, x="timestamp", y="ping", color="species",
#                  size='petal_length', hover_data=['petal_width'])

fig.show()



