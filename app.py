######-----Import Dash-----#####
import dash
from dash import dcc
from dash import html, callback
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import pandas as pd
import numpy as np
import gspread
import datetime

#####-----Create a Dash app instance-----#####
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LITERA],
    use_pages=True,
    )
app.title = 'CTS Performance Dashboard'

##-----Navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavLink(
                    [
                    html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
    ],
    brand="CTS Performance Dashboard",
    brand_href="#",
    color="#242947",
    dark=True,
)

## -----LAYOUT-----
app.layout = dbc.Container([
    dcc.Interval(id="timer", interval=1000*86400, n_intervals=0),
    dcc.Store(id="store", data={}),
    navbar,

    dbc.Row(
        [
            dbc.Col(
                [
                    dash.page_container
                ])
        ]
    )
], fluid=True, style={'height':'100vh'})

def load_google_sheets_data():
    cred_file = 'cts-performance-dashboard-8380302ca267.json'
    gc = gspread.service_account(cred_file)

    # Open the Google Sheets document
    database = gc.open('Database')

    data = {}
    for sheet in database.worksheets():
        sheet_data = sheet.get_all_records()
        data[sheet.title] = sheet_data

    return data

def preprocessing(df):
    dat = df.copy()
    #Rename month columns
    #Month = dat['Month'].astype('datetime64')
    Month = pd.to_datetime(df['Month'], dayfirst=True)
    month_name = []
    for i in range(len(Month)) :
        month_name.append(Month[i].strftime('%b-%y'))

    month_name[-1] = dat['Month'].iloc[-1][0:2] + '-' + month_name[-1]
    dat['Date'] = dat['Month']
    dat['Date'] = dat['Date'].astype('datetime64')
    dat['Year'] = dat['Date'].dt.year
    dat['Month'] = month_name
    
    #Aggregate data
    total = dat[dat['Year'] == datetime.date.today().year][['Volume Plan', 'Volume Actual']].apply(np.sum)
    avg = round(dat[dat['Year'] == datetime.date.today().year][['NLR Plan', 'NLR Actual', 'GLR Plan', 'GLR Actual','Fuel Ratio Gross', 'Fuel Ratio Net',
                                                                'NLR Single', 'NLR Blending', 'NLR Gear', 'NLR Barge',  
                                                                'GLR Single', 'GLR Blending', 'GLR Gear', 'GLR Barge']].apply(np.nanmean),2)
    per_v = total['Volume Actual']/total['Volume Plan']*100
    per_nlr = avg['NLR Actual']/avg['NLR Plan']*100
    per_glr = avg['GLR Actual']/avg['GLR Plan']*100
    per_fr = avg['Fuel Ratio Net']/avg['Fuel Ratio Gross']*100
    
    loadrate = ['NLR Single', 'NLR Blending', 'NLR Gear', 'NLR Barge',  
                'GLR Single', 'GLR Blending', 'GLR Gear', 'GLR Barge']
    for i in loadrate:
        if np.isnan(avg[i]):
            avg[i]=0
        
    ytd = list(['YTD',
                total['Volume Plan'], total['Volume Actual'], per_v, 
                round(avg['NLR Plan']), round(avg['NLR Actual']), per_nlr,
                round(avg['GLR Plan']), round(avg['GLR Actual']), per_glr,
                avg['Fuel Ratio Gross'], avg['Fuel Ratio Net'], per_fr,
                round(avg['NLR Single']), round(avg['NLR Blending']), round(avg['NLR Gear']), round(avg['NLR Barge']),
                round(avg['GLR Single']), round(avg['GLR Blending']), round(avg['GLR Gear']), round(avg['GLR Barge']),
                0, 0])
    
    for i in range(len(ytd)):
        if ytd[i]==0:
            ytd[i]=np.nan

    dat.loc[len(dat)] = ytd

    # dat_borneo.style.format(thousands=",")

    return(dat)

@callback(
    Output('store', 'data'),
    Input('timer', 'n_intervals')
)
def update_data(n):
    data = load_google_sheets_data()

    df_sumatra = pd.DataFrame(data['Bulk Sumatra'])
    #-- 1. Bulk Borneo
    df_borneo = pd.DataFrame(data['Bulk Borneo'])
    df_borneo = df_borneo.replace(r'^\s*$', np.nan, regex=True)
    dat_borneo = preprocessing(df_borneo)

    #-- 2. Bulk Celebes
    df_celebes = pd.DataFrame(data['Bulk Celebes'])
    df_celebes = df_celebes.replace(r'^\s*$', np.nan, regex=True)
    dat_celebes = preprocessing(df_celebes)

    #-- 3. Bulk Sumatra
    df_sumatra = pd.DataFrame(data['Bulk Sumatra'])
    df_sumatra = df_sumatra.replace(r'^\s*$', np.nan, regex=True)
    dat_sumatra = preprocessing(df_sumatra)

    #-- 4. Bulk Java
    df_java = pd.DataFrame(data['Bulk Java'])
    df_java = df_java.replace(r'^\s*$', np.nan, regex=True)
    dat_java = preprocessing(df_java)

    #-- 5. Bulk Dewata
    df_dewata = pd.DataFrame(data['Bulk Dewata'])
    df_dewata = df_dewata.replace(r'^\s*$', np.nan, regex=True)
    dat_dewata = preprocessing(df_dewata)

    #-- 6. Bulk Karimun
    df_karimun = pd.DataFrame(data['Bulk Karimun'])
    df_karimun = df_karimun.replace(r'^\s*$', np.nan, regex=True)
    dat_karimun = preprocessing(df_karimun)

    #-- 7. Ocean Flow 1
    df_of1 = pd.DataFrame(data['Ocean Flow 1'])
    df_of1 = df_of1.replace(r'^\s*$', np.nan, regex=True)
    dat_of1 = preprocessing(df_of1)

    #-- 8. Bulk Natuna
    df_natuna = pd.DataFrame(data['Bulk Natuna'])
    df_natuna = df_natuna.replace(r'^\s*$', np.nan, regex=True)
    dat_natuna = preprocessing(df_natuna)

    #-- 9. Bulk Sumba
    df_sumba = pd.DataFrame(data['Bulk Sumba (BGE)'])
    df_sumba = df_sumba.replace(r'^\s*$', np.nan, regex=True)
    dat_sumba = preprocessing(df_sumba)

    #-- 10. Bulk Derawan
    df_derawan = pd.DataFrame(data['Bulk Derawan'])
    df_derawan = df_derawan.replace(r'^\s*$', np.nan, regex=True)
    dat_derawan = preprocessing(df_derawan)

    #-- 11. Green Calypso
    df_greencalypso = pd.DataFrame(data['Green Calypso'])
    df_greencalypso = df_greencalypso.replace(r'^\s*$', np.nan, regex=True)
    dat_greencalypso = preprocessing(df_greencalypso)

    #-- 12. Putri Alysha
    df_putrialysha = pd.DataFrame(data['Putri Alysha'])
    df_putrialysha = df_putrialysha.replace(r'^\s*$', np.nan, regex=True)
    dat_putrialysha = preprocessing(df_putrialysha)

    #-- 13. Bulk Bunaken
    df_bunaken = pd.DataFrame(data['Bulk Bunaken'])
    df_bunaken = df_bunaken.replace(r'^\s*$', np.nan, regex=True)
    dat_bunaken = preprocessing(df_bunaken)

    data_dict = {'Bulk Borneo':dat_borneo.to_dict('records'), 
                 'Bulk Celebes':dat_celebes.to_dict('records'),
                 'Bulk Sumatra':dat_sumatra.to_dict('records'),
                 'Bulk Java':dat_java.to_dict('records'),
                 'Bulk Dewata':dat_dewata.to_dict('records'),
                 'Bulk Karimun':dat_karimun.to_dict('records'),
                 'Ocean Flow 1':dat_of1.to_dict('records'),
                 'Bulk Natuna':dat_natuna.to_dict('records'),
                 'Bulk Sumba':dat_sumba.to_dict('records'),
                 'Bulk Derawan':dat_derawan.to_dict('records'),
                 'Green Calypso':dat_greencalypso.to_dict('records'),
                 'Putri Alysha':dat_putrialysha.to_dict('records'),
                 'Bulk Bunaken':dat_bunaken.to_dict('records')}

    return data_dict

######-----Start the Dash server-----#####
if __name__ == "__main__":
    app.run_server(debug=True)