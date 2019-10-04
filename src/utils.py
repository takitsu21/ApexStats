import os
import requests
from src.config import Config

headers = {'TRN-Api-Key': Config()._api_token()}

class RequestError(Exception):
    pass

class PlayerNotFound(Exception):
    pass

def platform_convert(s):
    """adapt platform for the request"""
    return {"pc":"5", "psn":"2", "xbox":"1"}[s.lower()]

def generate_url_profile(platform, player):
    """generate link to the website profile"""
    return f"https://tracker.gg/apex/profile/{platform}/{player}/overview"

def _request(url, headers: dict = None, cookies: dict = None, call=None):
    try:
        r = requests.get(url, headers=headers, cookies=cookies)
        if r.status_code == 200:
            if call is not None:
                if call == "text":
                    return r.text
                elif call == "read":
                    return r.read()
                elif call == "json":
                    return r.json()
                return r
            else:
                raise RequestError(r.status_code)
    except Exception as e:
        print(type(e).__name__, e)