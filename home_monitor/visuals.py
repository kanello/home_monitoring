import plotly.express as px
import pandas as pd
import home_monitor.pipeline.connections as cons

def simple(column):
        

    df = cons.fromSqlite("select * from internet_speeds;")
    df["timestamp"] = pd.to_datetime(df['timestamp'])

    # must match the columns you have in the dataframe if you're passing the whole df in
    fig = px.scatter(df, x="timestamp", y=column)

    # fig = px.scatter(df, x="timestamp", y="ping", color="species",
    #                  size='petal_length', hover_data=['petal_width'])

    # fig.show()
    return fig



