import requests
import json
from datetime import datetime
import numpy as np
import pandas as pd

def get_markets(api = "cryptowatch"):
    """get markets available in API"""
    if api == "cryptowatch":
        try:
            r = requests.get("https://api.cryptowat.ch/markets").json()['result']
            exchanges = {item['exchange'] for item in r}
        except:
            print("Error: disfunctional API from Cryptowatch")
    return exchanges

def get_pairs(api = "cryptowatch"):
    """get pairs available in API"""
    if api == "cryptowatch":
        try:
            r = requests.get("https://api.cryptowat.ch/markets").json()['result']
            pairs = {item['pair'] for item in r}
        except:
            print("Error: disfunctional API from Cryptowatch")
    return pairs
