import os
import requests
from src.config import _api_token

headers = {'TRN-Api-Key': _api_token()}

class RequestError(Exception):
    pass

class PlayerNotFound(Exception):
    pass

def platform_convert(s):
    """adapt platform for the request"""
    return {"pc":"5", "psn":"2", "xbox":"1"}[s.lower()]

def generate_url_profile(platform, player):
    """generate link to the website profile"""
    if platform == 'origin': return f"https://apex.tracker.gg/profile/pc/{player}" # Fixes Issue #29 of improper link sent.
    return f"https://apex.tracker.gg/profile/{platform}/{player}"

def _request(
    url,
    headers: dict = None,
    cookies: dict = None,
    call=None):
    try:
        r = requests.get(url, headers=headers,
                        cookies=cookies)
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
    except Exception:
        pass

def better_formatting(stats_segments) -> str:
    _buffer_dn = []
    _buffer_v = []
    res = ""
    for children in stats_segments:
        _buffer_dn.append(stats_segments[children]["displayName"])
        _buffer_v.append(int(stats_segments[children]["value"]))
    max_to_format = max(map(len, _buffer_dn))
    buff_zip = zip(_buffer_dn, _buffer_v)
    if len(_buffer_dn):
        for (dn, v) in buff_zip:
            res += f"{dn.ljust(max_to_format, ' ')} {v}\n"
    return res
