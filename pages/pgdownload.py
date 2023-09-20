######-----Import Dash-----#####
import dash
from dash import dcc
from dash import html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from pptx import Presentation
from pptx.util import Cm, Pt

import os

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
from plotly.subplots import make_subplots

from datetime import date
from dateutil.relativedelta import relativedelta

dash.register_page(__name__, name='Download')

##-----page

## -----LAYOUT-----
layout = html.Div([
                html.Br(),
                
                html.Div([
                    html.Button('Download Slides', 
                                      id='download_button', 
                                      n_clicks=0, 
                                      style={'fontSize': 15, 'color':'#2a3f5f','font-family':'Verdana','display': 'inline-block'}), 
                    dcc.Download(id='download'),
                    ]),

                html.Br(),
                html.P(id='download_date', style={'fontSize': 15, 'color':'#2a3f5f','font-family':'Verdana'}),

    html.Footer('ABL',
            style={'textAlign': 'center', 
                   'fontSize': 20, 
                   'background-color':'#2a3f5f',
                   'color':'white',
                   'position': 'fixed',
                    'bottom': '0',
                    'width': '100%'})

    ], style={
        'paddingLeft':'10px',
        'paddingRight':'10px',
    })

#### Callback Auto Update Chart & Data

@callback(
    [Output('download', 'data'),
     Output('download_date', 'children')],
    [Input('download_button', 'n_clicks'),
     Input('store', 'data')]
)
def update_charts(n_clicks, data):
    if n_clicks == 0:
        raise PreventUpdate
    ######################
    # Data
    ######################
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

    # Chart
    volume_sumatra = plot_volume(dat_sumatra, "Volume Bulk Sumatra")
    volume_dewata = plot_volume(dat_dewata, "Volume Bulk Dewata")
    volume_karimun = plot_volume(dat_karimun, "Volume Bulk Karimun")
    volume_derawan = plot_volume(dat_derawan, "Volume Bulk Derawan")
    volume_of1 = plot_volume(dat_of1, "Volume Ocean Flow 1")
    volume_sumba = plot_volume(dat_sumba, "Volume Bulk Sumba")
    volume_java = plot_volume(dat_java, "Volume Bulk Java")
    volume_natuna = plot_volume(dat_natuna, "Volume Bulk Natuna")
    volume_celebes = plot_volume(dat_celebes, "Volume Bulk Celebes")
    volume_borneo = plot_volume(dat_borneo, "Volume Bulk Borneo")

    nlr_sumatra = plot_nlr(dat_sumatra, "NLR Bulk Sumatra")
    nlr_dewata = plot_nlr(dat_dewata, "NLR Bulk Dewata")
    nlr_karimun = plot_nlr(dat_karimun, "NLR Bulk Karimun")
    nlr_derawan = plot_nlr(dat_derawan, "NLR Bulk Derawan")
    nlr_of1 = plot_nlr(dat_of1, "NLR Ocean Flow 1")
    nlr_sumba = plot_nlr(dat_sumba, "NLR Bulk Sumba")
    nlr_java = plot_nlr(dat_java, "NLR Bulk Java")
    nlr_natuna = plot_nlr(dat_natuna, "NLR Bulk Natuna")
    nlr_celebes = plot_nlr(dat_celebes, "NLR Bulk Celebes")
    nlr_borneo = plot_nlr(dat_borneo, "NLR Bulk Borneo")

    glr_sumatra = plot_glr(dat_sumatra, "GLR Bulk Sumatra")
    glr_dewata = plot_glr(dat_dewata, "GLR Bulk Dewata")
    glr_karimun = plot_glr(dat_karimun, "GLR Bulk Karimun")
    glr_derawan = plot_glr(dat_derawan, "GLR Bulk Derawan")
    glr_of1 = plot_glr(dat_of1, "GLR Ocean Flow 1")
    glr_sumba = plot_glr(dat_sumba, "GLR Bulk Sumba")
    glr_java = plot_glr(dat_java, "GLR Bulk Java")
    glr_natuna = plot_glr(dat_natuna, "GLR Bulk Natuna")
    glr_celebes = plot_glr(dat_celebes, "GLR Bulk Celebes")
    glr_borneo = plot_glr(dat_borneo, "GLR Bulk Borneo")

    fr_sumatra = plot_fr(dat_sumatra, "Fuel Ratio Bulk Sumatra")
    fr_dewata = plot_fr(dat_dewata, "Fuel Ratio Bulk Dewata")
    fr_karimun = plot_fr(dat_karimun, "Fuel Ratio Bulk Karimun")
    fr_derawan = plot_fr(dat_derawan, "Fuel Ratio Bulk Derawan")
    fr_of1 = plot_fr(dat_of1, "Fuel Ratio Ocean Flow 1")
    fr_sumba = plot_fr(dat_sumba, "Fuel Ratio Bulk Sumba")
    fr_java = plot_fr(dat_java, "Fuel Ratio Bulk Java")
    fr_natuna = plot_fr(dat_natuna, "Fuel Ratio Bulk Natuna")
    fr_celebes = plot_fr(dat_celebes, "Fuel Ratio Bulk Celebes")
    fr_borneo = plot_fr(dat_borneo, "Fuel Ratio Bulk Borneo")

    # Save img
    pio.write_image(volume_sumatra, 'img/Volume Bulk Sumatra.png')
    pio.write_image(volume_dewata, 'img/Volume Bulk Dewata.png')
    pio.write_image(volume_karimun, 'img/Volume Bulk Karimun.png')
    pio.write_image(volume_derawan, 'img/Volume Bulk Derawan.png')
    pio.write_image(volume_of1, 'img/Volume Ocean Flow 1.png')
    pio.write_image(volume_sumba, 'img/Volume Bulk Sumba.png')
    pio.write_image(volume_java, 'img/Volume Bulk Java.png')
    pio.write_image(volume_natuna, 'img/Volume Bulk Natuna.png')
    pio.write_image(volume_celebes, 'img/Volume Bulk Celebes.png')
    pio.write_image(volume_borneo, 'img/Volume Bulk Borneo.png')

    pio.write_image(nlr_sumatra, 'img/NLR Bulk Sumatra.png')
    pio.write_image(nlr_dewata, 'img/NLR Bulk Dewata.png')
    pio.write_image(nlr_karimun, 'img/NLR Bulk Karimun.png')
    pio.write_image(nlr_derawan, 'img/NLR Bulk Derawan.png')
    pio.write_image(nlr_of1, 'img/NLR Ocean Flow 1.png')
    pio.write_image(nlr_sumba, 'img/NLR Bulk Sumba.png')
    pio.write_image(nlr_java, 'img/NLR Bulk Java.png')
    pio.write_image(nlr_natuna, 'img/NLR Bulk Natuna.png')
    pio.write_image(nlr_celebes, 'img/NLR Bulk Celebes.png')
    pio.write_image(nlr_borneo, 'img/NLR Bulk Borneo.png')

    pio.write_image(glr_sumatra, 'img/GLR Bulk Sumatra.png')
    pio.write_image(glr_dewata, 'img/GLR Bulk Dewata.png')
    pio.write_image(glr_karimun, 'img/GLR Bulk Karimun.png')
    pio.write_image(glr_derawan, 'img/GLR Bulk Derawan.png')
    pio.write_image(glr_of1, 'img/GLR Ocean Flow 1.png')
    pio.write_image(glr_sumba, 'img/GLR Bulk Sumba.png')
    pio.write_image(glr_java, 'img/GLR Bulk Java.png')
    pio.write_image(glr_natuna, 'img/GLR Bulk Natuna.png')
    pio.write_image(glr_celebes, 'img/GLR Bulk Celebes.png')
    pio.write_image(glr_borneo, 'img/GLR Bulk Borneo.png')

    pio.write_image(fr_sumatra, 'img/Fuel Ratio Bulk Sumatra.png')
    pio.write_image(fr_dewata, 'img/Fuel Ratio Bulk Dewata.png')
    pio.write_image(fr_karimun, 'img/Fuel Ratio Bulk Karimun.png')
    pio.write_image(fr_derawan, 'img/Fuel Ratio Bulk Derawan.png')
    pio.write_image(fr_of1, 'img/Fuel Ratio Ocean Flow 1.png')
    pio.write_image(fr_sumba, 'img/Fuel Ratio Bulk Sumba.png')
    pio.write_image(fr_java, 'img/Fuel Ratio Bulk Java.png')
    pio.write_image(fr_natuna, 'img/Fuel Ratio Bulk Natuna.png')
    pio.write_image(fr_celebes, 'img/Fuel Ratio Bulk Celebes.png')
    pio.write_image(fr_borneo, 'img/Fuel Ratio Bulk Borneo.png')    

    path = os.getcwd()
    download_date = html.Strong('Downloaded slides as per ' + str(dat_sumatra['Month'].iloc[-2]))
    ###################### PPTX ######################
    def to_pptx(bytes_io):
        # Create presentation
        pptx = path + '//' + 'slide_master.pptx'
        prs = Presentation(pptx)

        # define slidelayouts 
        slide = prs.slides.add_slide(prs.slide_layouts[0])
        slide1 = prs.slides.add_slide(prs.slide_layouts[1])
        slide2 = prs.slides.add_slide(prs.slide_layouts[1])
        slide3 = prs.slides.add_slide(prs.slide_layouts[2])
        slide4 = prs.slides.add_slide(prs.slide_layouts[2])
        slide5 = prs.slides.add_slide(prs.slide_layouts[2])
        slide6 = prs.slides.add_slide(prs.slide_layouts[2])
        slide7 = prs.slides.add_slide(prs.slide_layouts[2])
        slide8 = prs.slides.add_slide(prs.slide_layouts[2])
        slide9 = prs.slides.add_slide(prs.slide_layouts[2])
        slide10 = prs.slides.add_slide(prs.slide_layouts[2])
        slide11 = prs.slides.add_slide(prs.slide_layouts[2])
        slide12 = prs.slides.add_slide(prs.slide_layouts[2])

        # title slide
        title = slide.shapes.title
        subtitle = slide.placeholders[1]
        title.text = "Operation Update"
        subtitle.text = str(dat_sumatra['Month'].iloc[-2])


        # slide1 NLR Berau Coal
        slide1.placeholders[16].text = 'BERAU COAL OPERATIONAL DASHBOARD'
        slide1.placeholders[17].text = 'Berau Coal' 
        slide1.shapes.add_picture('img/NLR Bulk Sumatra.png', Cm(1.5), Cm(2.2), Cm(8.5), Cm(5))
        slide1.shapes.add_picture('img/NLR Bulk Dewata.png', Cm(12.7), Cm(2.2), Cm(8.5), Cm(5))
        slide1.shapes.add_picture('img/NLR Bulk Karimun.png', Cm(23.55), Cm(2.2), Cm(8.5), Cm(5))
        slide1.shapes.add_picture('img/NLR Bulk Derawan.png', Cm(1.5), Cm(10.2), Cm(8.5), Cm(5))
        slide1.shapes.add_picture('img/NLR Ocean Flow 1.png', Cm(12.7), Cm(10.2), Cm(8.5), Cm(5))
        slide1.shapes.add_picture('img/NLR Bulk Sumba.png', Cm(23.55), Cm(10.2), Cm(8.5), Cm(5))

        slide1.shapes.add_picture('img/yellow bullet.png', Cm(0.75), Cm(7.5))
        slide1.shapes.add_picture('img/yellow bullet.png', Cm(12), Cm(7.5))
        slide1.shapes.add_picture('img/yellow bullet.png', Cm(23), Cm(7.5))
        slide1.shapes.add_picture('img/yellow bullet.png', Cm(0.75), Cm(15.5))
        slide1.shapes.add_picture('img/yellow bullet.png', Cm(12), Cm(15.5))
        slide1.shapes.add_picture('img/yellow bullet.png', Cm(23), Cm(15.5))

        # slide2 GLR Berau Coal
        slide2.placeholders[16].text = 'BERAU COAL OPERATIONAL DASHBOARD'
        slide2.placeholders[17].text = 'Berau Coal' 
        slide2.shapes.add_picture('img/GLR Bulk Sumatra.png', Cm(1.5), Cm(2.2), Cm(8.5), Cm(5))
        slide2.shapes.add_picture('img/GLR Bulk Dewata.png', Cm(12.7), Cm(2.2), Cm(8.5), Cm(5))
        slide2.shapes.add_picture('img/GLR Bulk Karimun.png', Cm(23.55), Cm(2.2), Cm(8.5), Cm(5))
        slide2.shapes.add_picture('img/GLR Bulk Derawan.png', Cm(1.5), Cm(10.2), Cm(8.5), Cm(5))
        slide2.shapes.add_picture('img/GLR Ocean Flow 1.png', Cm(12.7), Cm(10.2), Cm(8.5), Cm(5))
        slide2.shapes.add_picture('img/GLR Bulk Sumba.png', Cm(23.55), Cm(10.2), Cm(8.5), Cm(5))

        slide2.shapes.add_picture('img/yellow bullet.png', Cm(0.75), Cm(7.5))
        slide2.shapes.add_picture('img/yellow bullet.png', Cm(12), Cm(7.5))
        slide2.shapes.add_picture('img/yellow bullet.png', Cm(23), Cm(7.5))
        slide2.shapes.add_picture('img/yellow bullet.png', Cm(0.75), Cm(15.5))
        slide2.shapes.add_picture('img/yellow bullet.png', Cm(12), Cm(15.5))
        slide2.shapes.add_picture('img/yellow bullet.png', Cm(23), Cm(15.5))

        # slide3 Bulk Sumatra
        slide3.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nBULK SUMATRA'
        slide3.placeholders[17].text = 'Berau Coal'
        slide3.placeholders[11].text = 'As of ' + str(dat_sumatra['Month'].iloc[-2])
        slide3.shapes.add_picture('img/Volume Bulk Sumatra.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide3.shapes.add_picture('img/Fuel Ratio Bulk Sumatra.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide3.shapes.add_picture('img/GLR Bulk Sumatra.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide3.shapes.add_picture('img/NLR Bulk Sumatra.png', Cm(14), Cm(10.3), Cm(12), Cm(7))

        # slide4 Bulk Dewata
        slide4.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nBULK DEWATA'
        slide4.placeholders[17].text = 'Berau Coal'
        slide4.placeholders[11].text = 'As of ' + str(dat_dewata['Month'].iloc[-2])
        slide4.shapes.add_picture('img/Volume Bulk Dewata.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide4.shapes.add_picture('img/Fuel Ratio Bulk Dewata.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide4.shapes.add_picture('img/GLR Bulk Dewata.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide4.shapes.add_picture('img/NLR Bulk Dewata.png', Cm(14), Cm(10.3), Cm(12), Cm(7))

        # slide5 Bulk Karimun
        slide5.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nBULK KARIMUN'
        slide5.placeholders[17].text = 'Berau Coal'
        slide5.placeholders[11].text = 'As of ' + str(dat_karimun['Month'].iloc[-2])
        slide5.shapes.add_picture('img/Volume Bulk Karimun.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide5.shapes.add_picture('img/Fuel Ratio Bulk Karimun.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide5.shapes.add_picture('img/GLR Bulk Karimun.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide5.shapes.add_picture('img/NLR Bulk Karimun.png', Cm(14), Cm(10.3), Cm(12), Cm(7))

        # slide6 Bulk Derawan
        slide6.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nBULK DERAWAN'
        slide6.placeholders[17].text = 'Berau Coal'
        slide6.placeholders[11].text = 'As of ' + str(dat_derawan['Month'].iloc[-2])
        slide6.shapes.add_picture('img/Volume Bulk Derawan.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide6.shapes.add_picture('img/Fuel Ratio Bulk Derawan.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide6.shapes.add_picture('img/GLR Bulk Derawan.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide6.shapes.add_picture('img/NLR Bulk Derawan.png', Cm(14), Cm(10.3), Cm(12), Cm(7))

        # slide7 Ocean Flow 1
        slide7.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nOCEAN FLOW 1'
        slide7.placeholders[17].text = 'Berau Coal'
        slide7.placeholders[11].text = 'As of ' + str(dat_of1['Month'].iloc[-2])
        slide7.shapes.add_picture('img/Volume Ocean Flow 1.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide7.shapes.add_picture('img/Fuel Ratio Ocean Flow 1.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide7.shapes.add_picture('img/GLR Ocean Flow 1.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide7.shapes.add_picture('img/NLR Ocean Flow 1.png', Cm(14), Cm(10.3), Cm(12), Cm(7))

        # slide8 Bulk Sumba
        slide8.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nBULK SUMBA'
        slide8.placeholders[17].text = 'Berau Coal'
        slide8.placeholders[11].text = 'As of ' + str(dat_sumba['Month'].iloc[-2])
        slide8.shapes.add_picture('img/Volume Bulk Sumba.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide8.shapes.add_picture('img/Fuel Ratio Bulk Sumba.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide8.shapes.add_picture('img/GLR Bulk Sumba.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide8.shapes.add_picture('img/NLR Bulk Sumba.png', Cm(14), Cm(10.3), Cm(12), Cm(7))
                            
        # slide9 Bulk Java
        slide9.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nBULK JAVA'
        slide9.placeholders[17].text = 'PSS'
        slide9.placeholders[11].text = 'As of ' + str(dat_java['Month'].iloc[-2])
        slide9.shapes.add_picture('img/Volume Bulk Java.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide9.shapes.add_picture('img/Fuel Ratio Bulk Java.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide9.shapes.add_picture('img/GLR Bulk Java.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide9.shapes.add_picture('img/NLR Bulk Java.png', Cm(14), Cm(10.3), Cm(12), Cm(7))
                            
        # slide10 Bulk Natuna
        slide10.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nBULK NATUNA'
        slide10.placeholders[17].text = 'BIB'
        slide10.placeholders[11].text = 'As of ' + str(dat_natuna['Month'].iloc[-2])
        slide10.shapes.add_picture('img/Volume Bulk Natuna.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide10.shapes.add_picture('img/Fuel Ratio Bulk Natuna.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide10.shapes.add_picture('img/GLR Bulk Natuna.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide10.shapes.add_picture('img/NLR Bulk Natuna.png', Cm(14), Cm(10.3), Cm(12), Cm(7))
                            
        # slide11 Bulk Celebes
        slide11.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nBULK CELEBES'
        slide11.placeholders[17].text = 'NORDEN'
        slide11.placeholders[11].text = 'As of ' + str(dat_celebes['Month'].iloc[-2])
        slide11.shapes.add_picture('img/Volume Bulk Celebes.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide11.shapes.add_picture('img/Fuel Ratio Bulk Celebes.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide11.shapes.add_picture('img/GLR Bulk Celebes.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide11.shapes.add_picture('img/NLR Bulk Celebes.png', Cm(14), Cm(10.3), Cm(12), Cm(7))
                            
        # slide12 Bulk Borneo
        slide12.placeholders[10].text = 'OPS PERFORMANCE DASHBOARD \nBULK BORNEO'
        slide12.placeholders[17].text = 'LDPL-KAMSAR'
        slide12.placeholders[11].text = 'As of ' + str(dat_borneo['Month'].iloc[-2])
        slide12.shapes.add_picture('img/Volume Bulk Borneo.png', Cm(1.25), Cm(3), Cm(12), Cm(7))
        slide12.shapes.add_picture('img/Fuel Ratio Bulk Borneo.png', Cm(14), Cm(3),Cm(12), Cm(7))
        slide12.shapes.add_picture('img/GLR Bulk Borneo.png', Cm(1.25), Cm(10.3), Cm(12), Cm(7))
        slide12.shapes.add_picture('img/NLR Bulk Borneo.png', Cm(14), Cm(10.3), Cm(12), Cm(7))                    


        # Saving the PowerPoint presentation
        prs.save(bytes_io)    

        # return dcc.send_bytes(to_pptx, 'Equipment Dashboard.pptx')
    
    return dcc.send_bytes(to_pptx, 'Equipment Dashboard.pptx'), download_date


######################
# Plot Function
######################
##-----Function
#-- 1. Volume Function
def plot_volume(df, title):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Volume Plan'].tail(4),
        name='Plan',
        text=df['Volume Plan'].tail(4),
        textfont_size=48,
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightblue'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Volume Actual'].tail(4),
        name='Actual',
        text=df['Volume Actual'].tail(4),
        textfont_size=48,
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightsalmon'))
    fig.update_layout({
        'height':1000,'width':1700,
        'margin' : {'t':200, 'b':3, 'l':3, 'r':3},
        "autosize": True,
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',},
        title={
            'text': title,
            'y':0.89,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size':75}},
        legend={
            'yanchor':"bottom",
            'y':-0.25,
            'xanchor':"center",
            'x':0.5,
            'itemsizing': 'constant',
            'font':{'size':40}},
        xaxis = dict(tickfont = dict(size=40)),
        yaxis = dict(tickfont = dict(size=40)),
        hovermode="x",
        shapes=[go.layout.Shape(type='rect', 
                                xref='paper',
                                yref='paper',
                                x0=-0.065,
                                y0=-0.25,
                                x1=1,
                                y1=1.25,
                                line={'width': 2, 'color': 'black'})])

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
        textfont_size=48,
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightblue'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['NLR Actual'].tail(4),
        name='Actual',
        text=df['NLR Actual'].tail(4),
        textfont_size=48,
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightsalmon'))
    fig.update_layout({
        'height':1000,'width':1700,
        'margin' : {'t':200, 'b':3, 'l':3, 'r':3},
        "autosize": True,
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',},
        title={
            'text': title,
            'y':0.89,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size':75}},
        legend={
            'yanchor':"bottom",
            'y':-0.25,
            'xanchor':"center",
            'x':0.5,
            'itemsizing': 'constant',
            'font':{'size':40}},
        xaxis = dict(tickfont = dict(size=40)),
        yaxis = dict(tickfont = dict(size=40)),
        hovermode="x",
        shapes=[go.layout.Shape(type='rect', 
                                xref='paper',
                                yref='paper',
                                x0=-0.048,
                                y0=-0.25,
                                x1=1,
                                y1=1.25,
                                line={'width': 2, 'color': 'black'})])

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
        textfont_size=48,
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightblue'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['GLR Actual'].tail(4),
        name='Actual',
        text=df['GLR Actual'].tail(4),
        textfont_size=48,
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightsalmon'))
    fig.update_layout({
        'height':1000,'width':1700,
        'margin' : {'t':200, 'b':3, 'l':3, 'r':3},
        "autosize": True,
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',},
        title={
            'text': title,
            'y':0.89,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size':75}},
        legend={
            'yanchor':"bottom",
            'y':-0.25,
            'xanchor':"center",
            'x':0.5,
            'itemsizing': 'constant',
            'font':{'size':40}},
        xaxis = dict(tickfont = dict(size=40)),
        yaxis = dict(tickfont = dict(size=40)),
        hovermode="x",
        shapes=[go.layout.Shape(type='rect', 
                                xref='paper',
                                yref='paper',
                                x0=-0.048,
                                y0=-0.25,
                                x1=1,
                                y1=1.25,
                                line={'width': 2, 'color': 'black'})])

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
        textfont_size=48,
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightblue'))
    fig.add_trace(go.Bar(
        x=df['Month'].tail(4),
        y=df['Fuel Ratio Net'].tail(4),
        name='Net',
        text=df['Fuel Ratio Net'].tail(4),
        textfont_size=48,
        hovertemplate='%{y:y}',
        textangle=0,
        marker_color='lightsalmon'))
    fig.update_layout({
        'height':1000,'width':1700,
        'margin' : {'t':200, 'b':3, 'l':3, 'r':3},
        "autosize": True,
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        'paper_bgcolor': 'rgba(0, 0, 0, 0)',},
        title={
            'text': title,
            'y':0.89,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size':75}},
        legend={
            'yanchor':"bottom",
            'y':-0.25,
            'xanchor':"center",
            'x':0.5,
            'itemsizing': 'constant',
            'font':{'size':40}},
        xaxis = dict(tickfont = dict(size=40)),
        yaxis = dict(tickfont = dict(size=40)),
        hovermode="x",
        shapes=[go.layout.Shape(type='rect', 
                                xref='paper',
                                yref='paper',
                                x0=-0.058,
                                y0=-0.25,
                                x1=1,
                                y1=1.25,
                                line={'width': 2, 'color': 'black'})])

    labels = list(df['Month'])
    labels[-1] = "AVG YTD'23"

    fig.update_xaxes(tickvals=np.arange(4), ticktext=labels[-4:])
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#d62728', griddash='dash')
    
    return(fig)