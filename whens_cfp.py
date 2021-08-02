#!/usr/bin/env python3

import datetime
import json
import requests
from datetime import date
from requests.exceptions import HTTPError

def get_cfps():
    try:
        response = requests.get("https://api.cfptime.org/api/cfps/")

        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
        print('Success!\n')
        return response.json()
        


def parse_cfps(cfps):
    today = date.today() # we need yyyy-mm-dd'T'hh:mm:ss
    now = today.strftime("%Y-%m-%d" + "T" + "%H:%M%S")
    
    for cfp in cfps:
        if  cfp['cfp_deadline'] > str(now):
            print(cfp['id'])

cfps = get_cfps()

parse_cfps(cfps)