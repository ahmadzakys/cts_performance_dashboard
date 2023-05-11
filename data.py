import gspread
import pandas as pd
import numpy as np

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
                round(avg['NLR Plan']), round(avg['NLR Actual']), per_nlr,
                round(avg['GLR Plan']), round(avg['GLR Actual']), per_glr,
                avg['Fuel Ratio Gross'], avg['Fuel Ratio Net'], per_fr,])

    dat = df.copy()
    dat.loc[len(df)] = ytd

    # dat_borneo.style.format(thousands=",")

    return(dat)

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