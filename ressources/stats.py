#!/usr/bin/env python3
#coding:utf-8
import os, requests
from ressources.tools import *
from ressources.exceptions import *

class Stats:
    """Get apex legends stats"""
    def __init__(self, player: str = "", platform: str = 'pc'):
        self.player = player
        self.base_platform = platform.lower()
        self.platform = platformConvert(platform)

    def data(self):
        url = f"https://public-api.tracker.gg/v2/apex/standard/profile/{self.platform}/{self.player}"
        try:
            r = requests.get(url, headers=headers)
            data = r.json()
            return data["data"]
        except Exception:
            raise PlayerNotFound(r.status_code)

    def exists(self):
        try:
            data = self.data()
            return True
        except PlayerNotFound:
            return False