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

dash.register_page(__name__, name='Fuel Ratio') 

## -----LAYOUT-----
layout = html.Div([
                ## --ROW1--
                html.Br(),
                html.P(children=[html.Strong('Fuel Ratio')],
                       style={'textAlign': 'center', 'fontSize': 27, 'background-color':'#F1F4F4','color':'#2a3f5f','font-family':'Verdana'}),

                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='fr_sumatra'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='fr_java'),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(id='fr_dewata'),
                    ], width=4),
                ]),

                html.Br(),

                ## --ROW2--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='fr_karimun'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='fr_of1'),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(id='fr_natuna'),
                    ], width=4),
                ]),

                html.Br(),

                ## --ROW3--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='fr_sumba'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='fr_derawan'),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(id='fr_borneo'),
                    ], width=4),

                ]),

                html.Br(),

                ## --ROW4--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(id='fr_celebes'),
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
    [Output('fr_borneo', 'figure'),
     Output('fr_celebes', 'figure'),
     Output('fr_sumatra', 'figure'),
     Output('fr_java', 'figure'),
     Output('fr_dewata', 'figure'),
     Output('fr_karimun', 'figure'),
     Output('fr_of1', 'figure'),
     Output('fr_natuna', 'figure'),
     Output('fr_sumba', 'figure'),
     Output('fr_derawan', 'figure'),
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
    fr_sumatra = plot_fr(dat_sumatra, "Fuel Ratio Bulk Sumatra", 0.24)
    fr_dewata = plot_fr(dat_dewata, "Fuel Ratio Bulk Dewata", 0.29)
    fr_karimun = plot_fr(dat_karimun, "Fuel Ratio Bulk Karimun", 0.25)
    fr_derawan = plot_fr(dat_derawan, "Fuel Ratio Bulk Derawan", 0.33)
    fr_of1 = plot_fr(dat_of1, "Fuel Ratio Ocean Flow 1", 0.32)
    fr_sumba = plot_fr(dat_sumba, "Fuel Ratio Bulk Sumba", 0.32)
    fr_java = plot_fr(dat_java, "Fuel Ratio Bulk Java", 0.27)
    fr_natuna = plot_fr(dat_natuna, "Fuel Ratio Bulk Natuna", 0.40)
    fr_celebes = plot_fr(dat_celebes, "Fuel Ratio Bulk Celebes", 0.24)
    fr_borneo = plot_fr(dat_borneo, "Fuel Ratio Bulk Borneo", 0.24)


    return fr_borneo, fr_celebes, fr_sumatra, fr_java, fr_dewata, fr_karimun, fr_of1, fr_natuna, fr_sumba, fr_derawan

##-----Function
#-- 4. Fuel Ratio Function
def plot_fr(df, title, baseline):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Fuel Ratio Gross'].tail(4),
        name='Gross',
        text=df['Fuel Ratio Gross'].tail(4),
        textposition = 'outside',
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='#5b9bd5'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Fuel Ratio Net'].tail(4),
        name='Net',
        text=df['Fuel Ratio Net'].tail(4),
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
        yaxis_range=[0,(df['Fuel Ratio Gross'].max())*1.8],
        bargroupgap=0.165,
        bargap=0.25,
        hovermode="x")
    
    fig.add_hline(y=baseline, line_width=2, line_dash="dash", line_color="red")
    fig.add_annotation(
        x=3.5,
        y=baseline+0.03,
        xref="x",
        yref="y",
        text=baseline,
        showarrow=False,
        font=dict(
            family="Verdana",
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
    labels[-1] = "AVG YTD'24"

    fig.update_xaxes(linecolor='#e1e6e6', tickvals=np.arange(4), ticktext=labels[-4:])
    fig.update_yaxes(showgrid=False, visible=False)
    
    return(fig)
