#!/usr/bin/env python3

import json
import requests
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
        cfps = json.loads(response.text)
        print(cfps)


get_cfps()