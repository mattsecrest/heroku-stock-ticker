import json
import requests
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime
import seaborn as sb

se = pd.read_csv(r'WIKI-meta-data.csv')

def mmdict(mm):
    dict = {
        '01':'01','02':'02','03':'03','04':'04','05':'05','06':'06','07':'07','08':'08','09':'09','10':'10','11':'11','12':'12',
        '1':'01','2':'02','3':'03','4':'04','5':'05','6':'06','7':'07','8':'08','9':'09',
        'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12',
        'January':'01','February':'02','March':'03','April':'04','June':'06','July':'07','August':'08','September':'09','October':'10','November':'11','December':'12',
        'jan':'01','feb':'02','mar':'03','apr':'04','may':'05','jun':'06','jul':'07','aug':'08','sep':'09','oct':'10','nov':'11','dec':'12',
        'january':'01','february':'02','march':'03','april':'04','june':'06','july':'07','august':'08','september':'09','october':'10','november':'11','december':'12',
        'JAN':'01','FEB':'02','MAR':'03','APR':'04','MAY':'05','JUN':'06','JUL':'07','AUG':'08','SEP':'09','OCT':'10','NOV':'11','DEC':'12'
        }
    return dict[mm]

def stockExists(symbol):
    return symbol in list(se['code'])

def stockTicker(symbol,mm,yyyy):
    mm = mmdict(mm)
    if len(yyyy)==2:
        yyyy == '20'+yyyy
    apikey = 'EMUQWX3jkuwYobNBkmyr'
    url = 'https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json?'
    sym = symbol
    cols = ['date,close']
    req = {'ticker':sym,
           'qopts.columns':cols,
           'api_key':apikey}
    
    r = requests.get(url,req)
    lr = r.json()['datatable']['data']
    dfr = pd.DataFrame(lr)
    dfr.columns = ['datestr','close']
    dfr['date'] = pd.to_datetime(dfr['datestr'],format='%Y-%m-%d')
    #dfr = dfr.set_index(dfr['date'])[mm+'-'+yyyy:mm+'-'+yyyy]
    return dfr