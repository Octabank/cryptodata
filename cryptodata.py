import numpy as np
import pandas as pd
import json
import requests
import json
import time


def get_markets(api = "cryptowatch", active = True):
    """get markets available in API"""
    if api == "cryptowatch":
        try:
            r = requests.get("https://api.cryptowat.ch/markets").json()['result']
            if (active):
                exchanges = {item['exchange'] for item in r if item['active'] is True}
            else:
                exchanges = {item['exchange'] for item in r}
        except:
            print("Error: disfunctional API from Cryptowatch")
    return exchanges

def get_pairs(api = "cryptowatch", active = True):
    """get pairs available in API"""
    if api == "cryptowatch":
        try:
            r = requests.get("https://api.cryptowat.ch/markets").json()['result']
            if (active):
                pairs = {item['pair'] for item in r if item['active'] is True}
            else:
                pairs = {item['pair'] for item in r}
        except:
            print("Error: disfunctional API from Cryptowatch")
    return pairs

def get_ohlc(market, pair, period = 1440, api = "cryptowatch", start = "", end = "", local_timezone = True):
    """get OHLC prices available in API"""
    period *= 60
    period = str(period)
    params = []
    url = "https://api.cryptowat.ch/markets/" + market + "/" + pair + "/ohlc"
    print(url)
    if (end == ""):
        before = ""
    else:
        before = time.mktime(time.strptime(end, "%d %m %y %H %M"))
    if (start == ""):
        after = start
    else:
        after = time.mktime(time.strptime(start, "%d %m %y %H %M"))
    if (not before or not after):
        prms = [('before', before), ('after', after)]
    else:
        prms = {'before': int(before) , 'after': int(after) }

#    print('params',prms)
    
    if api == "cryptowatch":
        try:
            r = requests.get(url, params=prms).json()['result'][period]
            #ohlc = [item['pair'] for item in r]
            if (local_timezone):            
                a = pd.DataFrame(r, columns = ['date(local)','open','high','low','close','volume','neg'])
                a[a.columns[0]] = pd.to_datetime(a[a.columns[0]] - time.timezone, unit = 's')
                return a
            else:
                a = pd.DataFrame(r, columns = ['date(utc)','open','high','low','close','volume','neg'])
                a[a.columns[0]] = pd.to_datetime(a[a.columns[0]], unit = 's')
                return a               
                

        except:
            print("Error: disfunctional API from Cryptowatch")
            
#columns = ['period','open','high','low','close','volume','neg']    


    
