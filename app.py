import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import smps
import numpy as np
import json

from plotly import graph_objs as go
from pandas_datareader import data as web
from datetime import datetime as dt

app = dash.Dash("SMPS Data Analyzer")

# Load the sample data for now...
sample_data = smps.load_file("boston_wintertime.txt", column=False)

app.layout = html.Div([
    html.H1("SMPS.Analyzer.2017"),
    html.H2("Header 2"),
    html.H3("Header 3"),
    html.H4("Header 4"),
    html.H5("Header 5"),
    html.H6("Header 6"),
    html.P("Paragraph!", className="my-custom-p-class"),
    dcc.Dropdown(
        id="dropdown-weights",
        options=[
            {'label': 'Number', 'value': 'number'},
            {'label': 'Surface Area', 'value': 'surface'},
            {'label': 'Volume', 'value': 'volume'},
        ],
        value="number"
        ),
    dcc.Markdown("""
    **Selection Data**

    Choose the lasso or rectangle tool in the graph's menu
    bar and then select points in the graph to see this
    data update.
    """),
    html.Pre(id='selected-data', style={"border": 'thin-lightgray solid'}),
    dcc.Graph(id="graph-timeseries"),
    html.H3("Particle Size Distribution"),
    dcc.Graph(id='graph-distribution')
])

"""
@app.callback(Output('graph-timeseries', 'figure'), [Input('dropdown-weights', 'value')])
def update_timeseries_graph(weight):
    xvals = sample_data.histogram.index
    zvals = sample_data.histogram.replace(0.0, 0.1).T.values

    data = [
        go.Heatmap(x=xvals, y=sample_data.midpoints, z=np.log10(zvals))
    ]

    layout = go.Layout(
        yaxis=dict(type='log')
    )

    return go.Figure(data=data, layout=layout)

@app.callback(Output('selected-data', 'content'),[Input('graph-timeseries', 'selectedData')])
def update_graphs_based_on_selection(selectedData):
    print (selectedData)

    return json.dumps(selectedData, indent=2)

@app.callback(Output('graph-distribution', 'figure'), [Input('dropdown-weights', 'value')])
def update_distribution_graph(weight):
    yvals = sample_data.histogram.mean()
    xvals = sample_data.midpoints

    if weight == 'surface':
        yvals = yvals * np.pi * (sample_data.midpoints / 1000.)**2
        ylabel = "dS/dlogDp"
    elif weight == 'volume':
        yvals = yvals * (np.pi / 6.) * (sample_data.midpoints / 1000.)**3
        ylabel = 'dV/dlogDp'
    else:
        ylabel = 'dN/dlogDP'

    data = [
        go.Scatter(x=xvals, y=yvals, line=dict(width=6), mode='lines+markers', fill='tozeroy')
    ]

    layout = go.Layout(
        xaxis=dict(type='log', autorange=True, title="Dp / um"),
        yaxis=dict(title=ylabel)
    )

    return go.Figure(data=data, layout=layout)
"""

if __name__ == "__main__":
    app.run_server(debug=True)
