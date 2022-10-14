from flask import Flask, render_template
import sys
import pandas as pd
import json
import plotly
import plotly.express as px
from home_monitor.visuals import simple


app = Flask(__name__)

@app.route('/')
def notdash():
   fig1 = simple("ping")
   graphJSON1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
   
   fig = simple("download")
   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

   
   return render_template('app.html', graphJSON1=graphJSON1, graphJSON=graphJSON)


# if __name__ == "__main__":
#     app.run()