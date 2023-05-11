######-----Import Dash-----#####
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np

from data import dat_borneo, dat_celebes, dat_sumatra, dat_java, dat_chloe, dat_karimun, dat_of1, dat_natuna, dat_blitz, dat_derawan

import plotly.express as px
import plotly.graph_objects as go

dash.register_page(__name__, path='/', name='Volume') # '/' is home page

##-----page 1 data

##-----Function
#-- 1. Volume Function
def plot_volume(df, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Volume Plan'].tail(4),
        name='Plan',
        text=df['Volume Plan'].tail(4),
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightblue'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Volume Actual'].tail(4),
        name='Actual',
        text=df['Volume Actual'].tail(4),
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightsalmon'))
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',},
        title={
            'text': title,
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        legend={
            'yanchor':"bottom",
            'y':-0.25,
            'xanchor':"center",
            'x':0.5},
        hovermode="x")

    labels = list(df['Month'])
    labels[-1] = "YTD'23"

    fig.update_xaxes(tickvals=np.arange(4), ticktext=labels[-4:])
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#d62728', griddash='dash')
    
    return(fig)

#-- 2. NLR Function
def plot_nlr(df, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['NLR Plan'].tail(4),
        name='Plan',
        text=df['NLR Plan'].tail(4),
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightblue'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['NLR Actual'].tail(4),
        name='Actual',
        text=df['NLR Actual'].tail(4),
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightsalmon'))
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',},
        title={
            'text': title,
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        legend={
            'yanchor':"bottom",
            'y':-0.25,
            'xanchor':"center",
            'x':0.5},
        hovermode="x")

    labels = list(df['Month'])
    labels[-1] = "AVG YTD'23"

    fig.update_xaxes(tickvals=np.arange(4), ticktext=labels[-4:])
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#d62728', griddash='dash')
    
    return(fig)

#-- 3. GLR Function
def plot_glr(df, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['GLR Plan'].tail(4),
        name='Plan',
        text=df['GLR Plan'].tail(4),
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightblue'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['GLR Actual'].tail(4),
        name='Actual',
        text=df['GLR Actual'].tail(4),
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightsalmon'))
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',},
        title={
            'text': title,
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        legend={
            'yanchor':"bottom",
            'y':-0.25,
            'xanchor':"center",
            'x':0.5},
        hovermode="x")

    labels = list(df['Month'])
    labels[-1] = "AVG YTD'23"

    fig.update_xaxes(tickvals=np.arange(4), ticktext=labels[-4:])
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#d62728', griddash='dash')
    
    return(fig)

#-- 4. Fuel Ratio Function
def plot_fr(df, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Fuel Ratio Gross'].tail(4),
        name='Gross',
        text=df['Fuel Ratio Gross'].tail(4),
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightblue'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Fuel Ratio Net'].tail(4),
        name='Net',
        text=df['Fuel Ratio Net'].tail(4),
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightsalmon'))
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',},
        title={
            'text': title,
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        legend={
            'yanchor':"bottom",
            'y':-0.25,
            'xanchor':"center",
            'x':0.5},
        hovermode="x")

    labels = list(df['Month'])
    labels[-1] = "AVG YTD'23"

    fig.update_xaxes(tickvals=np.arange(4), ticktext=labels[-4:])
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#d62728', griddash='dash')
    
    return(fig)


volume_borneo = plot_volume(dat_borneo, "Volume Bulk Borneo")
volume_celebes = plot_volume(dat_celebes, "Volume Bulk Celebes")
volume_sumatra = plot_volume(dat_sumatra, "Volume Bulk Sumatra")
volume_java = plot_volume(dat_java, 'Volume Bulk Java')
volume_chloe = plot_volume(dat_chloe, 'Volume Princess Chloe')
volume_karimun = plot_volume(dat_karimun, 'Volume Bulk Karimun')
volume_of1 = plot_volume(dat_of1, 'Volume Ocean Flow 1')
volume_natuna = plot_volume(dat_natuna, 'Volume Bulk Natuna')
volume_blitz = plot_volume(dat_blitz, 'Volume Blitz')
volume_derawan = plot_volume(dat_derawan, 'Volume Bulk Derawan')


## -----LAYOUT-----
layout = html.Div([
                ## --ROW1--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=volume_borneo),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(figure=volume_celebes),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(figure=volume_sumatra),
                    ], width=4)
                ]),

                html.Br(),

                ## --ROW2--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=volume_java),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(figure=volume_chloe),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(figure=volume_karimun),
                    ], width=4)
                ]),

                html.Br(),

                ## --ROW3--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=volume_of1),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(figure=volume_natuna),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(figure=volume_blitz),
                    ], width=4)
                ]),

                html.Br(),

                ## --ROW4--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=volume_derawan),
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
