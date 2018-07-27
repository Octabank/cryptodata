import numpy as np
import pandas as pd
import json
import requests
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
    dates = ["",""]
    url = "https://api.cryptowat.ch/markets/" + market + "/" + pair + "/ohlc"
    
    for i, date in enumerate([start, end]):
        if (not date):
            dates[i] = date
        else:
            try:
                dates[i] = int(time.mktime(time.strptime(date, "%d %m %y %H %M"))) #+ local_timezone*time.timezone
            except:
                print("Error: Datetime format d m y H M")
    
    prms = {'before': dates[1], 'after': dates[0]}
    
    if api == "cryptowatch":
        try:
            r = requests.get(url, params=prms).json()['result'][period]
            a = pd.DataFrame(r, columns = ['date(local)','open','high','low','close','volume','neg'])
            a[a.columns[0]] = pd.to_datetime(a[a.columns[0]] - local_timezone*time.timezone, unit = 's')
            return a        
        except:
            print("Error: disfunctional API from Cryptowatch")
            
#columns = ['period','open','high','low','close','volume','neg']  

