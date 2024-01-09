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

dash.register_page(__name__, name='Gross Loading Rate')


## -----LAYOUT-----
layout = html.Div([
                ## --ROW1--
                html.Br(),
                html.P(children=[html.Strong('Gross Loading Rate')],
                       style={'textAlign': 'center', 'fontSize': 27, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='glr_sumatra'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='glr_java'),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(id='glr_dewata'),
                    ], width=4),
                ]),

                html.Br(),

                ## --ROW2--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='glr_karimun'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='glr_of1'),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(id='glr_natuna'),
                    ], width=4),
                ]),

                html.Br(),

                ## --ROW3--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='glr_sumba'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='glr_derawan'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='glr_borneo'),
                    ], width=4),

                ]),

                html.Br(),

                ## --ROW4--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='glr_celebes'),
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
    [Output('glr_borneo', 'figure'),
     Output('glr_celebes', 'figure'),
     Output('glr_sumatra', 'figure'),
     Output('glr_java', 'figure'),
     Output('glr_dewata', 'figure'),
     Output('glr_karimun', 'figure'),
     Output('glr_of1', 'figure'),
     Output('glr_natuna', 'figure'),
     Output('glr_sumba', 'figure'),
     Output('glr_derawan', 'figure'),
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
    glr_borneo = plot_glr(dat_borneo, "GLR Bulk Borneo")
    glr_celebes = plot_glr(dat_celebes, "GLR Bulk Celebes")
    glr_sumatra = plot_glr(dat_sumatra, "GLR Bulk Sumatra")
    glr_java = plot_glr(dat_java, 'GLR Bulk Java')
    glr_dewata = plot_glr(dat_dewata, 'GLR Bulk Dewata')
    glr_karimun = plot_glr(dat_karimun, 'GLR Bulk Karimun')
    glr_of1 = plot_glr(dat_of1, 'GLR Ocean Flow 1')
    glr_natuna = plot_glr(dat_natuna, 'GLR Bulk Natuna')
    glr_sumba = plot_glr(dat_sumba, 'GLR Bulk Sumba')
    glr_derawan = plot_glr(dat_derawan, 'GLR Bulk Derawan')

    return glr_borneo, glr_celebes, glr_sumatra, glr_java, glr_dewata, glr_karimun, glr_of1, glr_natuna, glr_sumba, glr_derawan

##-----Function
#-- 3. GLR Function
def plot_glr(df, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['GLR Single'].tail(4),
        name='Single',
        text=df['GLR Single'].tail(4),
        textfont_size=48,
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='#ffc000'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['GLR Blending'].tail(4),
        name='Blending',
        text=df['GLR Blending'].tail(4),
        textfont_size=48,
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='#00b1f1'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['GLR Gear'].tail(4),
        name='Gear',
        text=df['GLR Gear'].tail(4),
        textfont_size=48,
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='#0071c1'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['GLR Barge'].tail(4),
        name='Barge',
        text=df['GLR Barge'].tail(4),
        textfont_size=48,
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='#92d14f'))
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
            'x':0.5,
            'orientation':'h'},
        yaxis_range=[0,(df['GLR Plan'].iloc[-1])*1.8],
        bargroupgap=0.05,
        bargap=0.15,
        hovermode="x")

    labels = list(df['Month'])
    labels[-1] = "AVG YTD'24"

    fig.update_xaxes(linecolor='#e1e6e6', tickvals=np.arange(4), ticktext=labels[-4:])
    fig.update_yaxes(showgrid=False, visible=False)
    
    return(fig)