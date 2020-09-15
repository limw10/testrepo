#!/usr/bin/env python
# coding: utf-8

# In[1]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


# In[7]:

app = dash.Dash()

df1 = pd.read_csv("Regional DCP.csv", encoding='latin1')
fig = px.bar(df1, x="Project Type", y=" Cost Apportioned to DCP  ", color="Project Type")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig,
        'layout':{
            'title': 'Dash Data',
            'xaxis' : dict(
            title='x Axis',)
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

