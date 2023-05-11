######-----Import Dash-----#####
import dash
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import gspread
import pandas as pd
import numpy as np

import plotly.express as px
import plotly.graph_objects as go

dash.register_page(__name__, name='Fuel Ratio') 

##-----page 4 data

##-----Import Data
cred_file = 'cts-performance-dashboard-8380302ca267.json'
gc = gspread.service_account(cred_file)

database = gc.open('Database')

borneo = database.worksheet('Bulk Borneo')
celebes = database.worksheet('Bulk Celebes')
sumatra = database.worksheet('Bulk Sumatra')
java = database.worksheet('Bulk Java')
chloe = database.worksheet('Princess Chloe')
karimun = database.worksheet('Bulk Karimun')
of1 = database.worksheet('Ocean Flow 1')
natuna = database.worksheet('Bulk Natuna')
blitz = database.worksheet('Blitz')
derawan = database.worksheet('Bulk Derawan')


##-----Function
#-- 1. Pre-Processing
def preprocessing(df):
    total = df[['Volume Plan', 'Volume Actual']].apply(np.sum)
    avg = round(df[['NLR Plan', 'NLR Actual', 'GLR Plan', 'GLR Actual','Fuel Ratio Gross', 'Fuel Ratio Net']] \
                .apply(np.nanmean),2)
    per_v = round(total['Volume Actual']/total['Volume Plan']*100)
    per_nlr = round(avg['NLR Actual']/avg['NLR Plan']*100)
    per_glr = round(avg['GLR Actual']/avg['GLR Plan']*100)
    per_fr = round(avg['Fuel Ratio Net']/avg['Fuel Ratio Gross']*100)
    ytd = list(['YTD',
                total['Volume Plan'], total['Volume Actual'], per_v, 
                avg['NLR Plan'], avg['NLR Actual'], per_nlr,
                avg['GLR Plan'], avg['GLR Actual'], per_glr,
                avg['Fuel Ratio Gross'], avg['Fuel Ratio Net'], per_fr,])

    dat = df.copy()
    dat.loc[len(df)] = ytd

    # dat_borneo.style.format(thousands=",")

    return(dat)

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


#-- 1. Bulk Borneo
df_borneo = pd.DataFrame(borneo.get_all_records())
df_borneo = df_borneo.replace(r'^\s*$', np.nan, regex=True)
dat_borneo = preprocessing(df_borneo)

#-- 2. Bulk Celebes
df_celebes = pd.DataFrame(celebes.get_all_records())
df_celebes = df_celebes.replace(r'^\s*$', np.nan, regex=True)
dat_celebes = preprocessing(df_celebes)

#-- 3. Bulk Sumatra
df_sumatra = pd.DataFrame(sumatra.get_all_records())
df_sumatra = df_sumatra.replace(r'^\s*$', np.nan, regex=True)
dat_sumatra = preprocessing(df_sumatra)

#-- 4. Bulk Java
df_java = pd.DataFrame(java.get_all_records())
df_java = df_java.replace(r'^\s*$', np.nan, regex=True)
dat_java = preprocessing(df_java)

#-- 5. Princess Chloe
df_chloe = pd.DataFrame(chloe.get_all_records())
df_chloe = df_chloe.replace(r'^\s*$', np.nan, regex=True)
dat_chloe = preprocessing(df_chloe)

#-- 6. Bulk Karimun
df_karimun = pd.DataFrame(karimun.get_all_records())
df_karimun = df_karimun.replace(r'^\s*$', np.nan, regex=True)
dat_karimun = preprocessing(df_karimun)

#-- 7. Ocean Flow 1
df_of1 = pd.DataFrame(of1.get_all_records())
df_of1 = df_of1.replace(r'^\s*$', np.nan, regex=True)
dat_of1 = preprocessing(df_of1)

#-- 8. Bulk Natuna
df_natuna = pd.DataFrame(natuna.get_all_records())
df_natuna = df_natuna.replace(r'^\s*$', np.nan, regex=True)
dat_natuna = preprocessing(df_natuna)

#-- 9. Blitz
df_blitz = pd.DataFrame(blitz.get_all_records())
df_blitz = df_blitz.replace(r'^\s*$', np.nan, regex=True)
dat_blitz = preprocessing(df_blitz)

#-- 10. Bulk Derawan
df_derawan = pd.DataFrame(derawan.get_all_records())
df_derawan = df_derawan.replace(r'^\s*$', np.nan, regex=True)
dat_derawan = preprocessing(df_derawan)


fr_borneo = plot_fr(dat_borneo, "Fuel Ratio Bulk Borneo")
fr_celebes = plot_fr(dat_celebes, "Fuel Ratio Bulk Celebes")
fr_sumatra = plot_fr(dat_sumatra, "Fuel Ratio Bulk Sumatra")
fr_java = plot_fr(dat_java, 'Fuel Ratio Bulk Java')
fr_chloe = plot_fr(dat_chloe, 'Fuel Ratio Princess Chloe')
fr_karimun = plot_fr(dat_karimun, 'Fuel Ratio Bulk Karimun')
fr_of1 = plot_fr(dat_of1, 'Fuel Ratio Ocean Flow 1')
fr_natuna = plot_fr(dat_natuna, 'Fuel Ratio Bulk Natuna')
fr_blitz = plot_fr(dat_blitz, 'Fuel Ratio Blitz')
fr_derawan = plot_fr(dat_derawan, 'Fuel Ratio Bulk Derawan')

## -----LAYOUT-----
layout = html.Div([
                ## --ROW1--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=fr_borneo),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(figure=fr_celebes),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(figure=fr_sumatra),
                    ], width=4)
                ]),

                html.Br(),

                ## --ROW2--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=fr_java),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(figure=fr_chloe),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(figure=fr_karimun),
                    ], width=4)
                ]),

                html.Br(),

                ## --ROW3--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=fr_of1),
                    ], width=4),
                        
                    dbc.Col([
                        dcc.Graph(figure=fr_natuna),
                    ], width=4),

                    dbc.Col([
                        dcc.Graph(figure=fr_blitz),
                    ], width=4)
                ]),

                html.Br(),

                ## --ROW4--
                dbc.Row([
                    dbc.Col([
                        dcc.Graph(figure=fr_derawan),
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
