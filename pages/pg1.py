######-----Import Dash-----#####
import dash
from dash import dcc
from dash import html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

dash.register_page(__name__, path='/', name='Volume') # '/' is home page

## -----LAYOUT-----
layout = html.Div([
                ## --ROW1--
                html.Br(),
                html.P(children=[html.Strong('Volume')],
                       style={'textAlign': 'center', 'fontSize': 27, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='volume_sumatra'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='volume_java'),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(id='volume_dewata'),
                    ], width=4),
                ]),

                html.Br(),

                ## --ROW2--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='volume_karimun'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='volume_of1'),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(id='volume_natuna'),
                    ], width=4),
                ]),

                html.Br(),

                ## --ROW3--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='volume_sumba'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='volume_derawan'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='volume_borneo'),
                    ], width=4),

                ]),

                html.Br(),

                ## --ROW4--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='volume_celebes'),
                    ], width=4),

                ]),

    html.Br(),
    html.Footer('ABL',
            style={'textAlign': 'center', 
                   'fontSize': 20, 
                   'background-color':'#242947',
                   'color':'white'})

    ], style={
        'paddingLeft':'10px',
        'paddingRight':'10px',
    })

@callback(
    [Output('volume_borneo', 'figure'),
     Output('volume_celebes', 'figure'),
     Output('volume_sumatra', 'figure'),
     Output('volume_java', 'figure'),
     Output('volume_dewata', 'figure'),
     Output('volume_karimun', 'figure'),
     Output('volume_of1', 'figure'),
     Output('volume_natuna', 'figure'),
     Output('volume_sumba', 'figure'),
     Output('volume_derawan', 'figure'),
     ],
    Input('store', 'data')
)
def update_charts(data):

    dat_borneo = pd.DataFrame(data['Bulk Borneo'])
    dat_celebes = pd.DataFrame(data['Bulk Celebes'])
    dat_sumatra = pd.DataFrame(data['Bulk Sumatra'])
    dat_java = pd.DataFrame(data['Bulk Java'])
    dat_dewata = pd.DataFrame(data['Bulk Dewata'])
    dat_karimun = pd.DataFrame(data['Bulk Karimun'])
    dat_of1 = pd.DataFrame(data['Ocean Flow 1'])
    dat_natuna = pd.DataFrame(data['Bulk Natuna'])
    dat_sumba = pd.DataFrame(data['Bulk Sumba'])
    dat_derawan = pd.DataFrame(data['Bulk Derawan'])

    
    ##-----Plot Volume
    volume_borneo = plot_volume(dat_borneo, "Volume Bulk Borneo")
    volume_celebes = plot_volume(dat_celebes, "Volume Bulk Celebes")
    volume_sumatra = plot_volume(dat_sumatra, "Volume Bulk Sumatra")
    volume_java = plot_volume(dat_java, 'Volume Bulk Java')
    volume_dewata = plot_volume(dat_dewata, 'Volume Bulk Dewata')
    volume_karimun = plot_volume(dat_karimun, 'Volume Bulk Karimun')
    volume_of1 = plot_volume(dat_of1, 'Volume Ocean Flow 1')
    volume_natuna = plot_volume(dat_natuna, 'Volume Bulk Natuna')
    volume_sumba = plot_volume(dat_sumba, 'Volume Bulk Sumba')
    volume_derawan = plot_volume(dat_derawan, 'Volume Bulk Derawan')

    return volume_borneo, volume_celebes, volume_sumatra, volume_java, volume_dewata, volume_karimun, volume_of1, volume_natuna, volume_sumba, volume_derawan


##-----Function
#-- 1. Volume Function
def plot_volume(df, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Volume Plan'].tail(4),
        name='Plan',
        text=df['Volume Plan'].tail(4),
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='#5b9bd5'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Volume Actual'].tail(4),
        name='Actual',
        text=df['Volume Actual'].tail(4),
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightsalmon'))
    fig.update_layout({
        'margin' : {'t':3, 'b':3, 'l':15, 'r':15},
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',},
        title={
            'text': f'<b>{title}</b>',
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        legend={
            'yanchor':"bottom",
            'y':-0.25,
            'xanchor':"center",
            'x':0.5},
        yaxis_range=[0,(df['Volume Plan'].iloc[-1])*1.8],
        bargroupgap=0.165,
        bargap=0.25,
        hovermode="x")

    labels = list(df['Month'])
    labels[-1] = "YTD'24"

    fig.update_xaxes(linecolor='#e1e6e6', tickvals=np.arange(4), ticktext=labels[-4:])
    fig.update_yaxes(showgrid=False, visible=False)
    
    return(fig)