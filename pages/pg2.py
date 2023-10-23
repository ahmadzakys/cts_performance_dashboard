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

dash.register_page(__name__, name='Net Loading Rate') 

## -----LAYOUT-----
layout = html.Div([
                ## --ROW1--
                html.Br(),
                html.P(children=[html.Strong('Net Loading Rate')],
                       style={'textAlign': 'center', 'fontSize': 27, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='nlr_sumatra'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='nlr_java'),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(id='nlr_dewata'),
                    ], width=4),
                ]),

                html.Br(),

                ## --ROW2--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='nlr_karimun'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='nlr_of1'),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(id='nlr_natuna'),
                    ], width=4),
                ]),

                html.Br(),

                ## --ROW3--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='nlr_sumba'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='nlr_derawan'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='nlr_borneo'),
                    ], width=4),

                ]),

                html.Br(),

                ## --ROW4--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='nlr_celebes'),
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
    [Output('nlr_borneo', 'figure'),
     Output('nlr_celebes', 'figure'),
     Output('nlr_sumatra', 'figure'),
     Output('nlr_java', 'figure'),
     Output('nlr_dewata', 'figure'),
     Output('nlr_karimun', 'figure'),
     Output('nlr_of1', 'figure'),
     Output('nlr_natuna', 'figure'),
     Output('nlr_sumba', 'figure'),
     Output('nlr_derawan', 'figure'),
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
    
    ##-----Plot NLR
    nlr_sumatra = plot_nlr(dat_sumatra, "NLR Bulk Sumatra", 52000)
    nlr_dewata = plot_nlr(dat_dewata, "NLR Bulk Dewata", 36815)
    nlr_karimun = plot_nlr(dat_karimun, "NLR Bulk Karimun", 46000)
    nlr_derawan = plot_nlr(dat_derawan, "NLR Bulk Derawan", 46000)
    nlr_of1 = plot_nlr(dat_of1, "NLR Ocean Flow 1", 36000)
    nlr_sumba = plot_nlr(dat_sumba, "NLR Bulk Sumba", 28000)
    nlr_java = plot_nlr(dat_java, "NLR Bulk Java", 46000)
    nlr_natuna = plot_nlr(dat_natuna, "NLR Bulk Natuna", 18400)
    nlr_celebes = plot_nlr(dat_celebes, "NLR Bulk Celebes", 25000)
    nlr_borneo = plot_nlr(dat_borneo, "NLR Bulk Borneo", 25000)

    return nlr_borneo, nlr_celebes, nlr_sumatra, nlr_java, nlr_dewata, nlr_karimun, nlr_of1, nlr_natuna, nlr_sumba, nlr_derawan

##-----Function
#-- 2. NLR Function
def plot_nlr(df, title, baseline):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['NLR Single'].tail(4),
        name='Single',
        text=df['NLR Single'].tail(4),
        textfont_size=48,
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='#ffc000'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['NLR Blending'].tail(4),
        name='Blending',
        text=df['NLR Blending'].tail(4),
        textfont_size=48,
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='#00b1f1'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['NLR Gear'].tail(4),
        name='Gear',
        text=df['NLR Gear'].tail(4),
        textfont_size=48,
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='#0071c1'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['NLR Barge'].tail(4),
        name='Barge',
        text=df['NLR Barge'].tail(4),
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
        yaxis_range=[0,(df['NLR Plan'].iloc[-1])*1.8],
        bargroupgap=0.05,
        bargap=0.15,
        hovermode="x")
    
    fig.add_hline(y=baseline, line_width=1, line_dash="dash", line_color="red")
    fig.add_annotation(
        x=3.75,
        y=baseline*1.07,
        xref="x",
        yref="y",
        text=str(baseline) + ' MT/Day',
        showarrow=False,
        font=dict(
            family="Verdana",
            size=6,
            color="#ffffff"
            ),
        align="center",
        # bordercolor="#c7c7c7",
        borderwidth=1,
        borderpad=2,
        bgcolor="red",
        opacity=0.8
        )

    labels = list(df['Month'])
    labels[-1] = "AVG YTD'23"

    fig.update_xaxes(linecolor='#e1e6e6', tickvals=np.arange(4), ticktext=labels[-4:])
    fig.update_yaxes(showgrid=False, visible=False)
    
    return(fig)

