#!/usr/bin/env python3
#coding:utf-8
import requests, os
from ressources.tools import *
import ressources.SqlManagment as SqlManagment
from ressources.exceptions import *


class Stats:
    """Get apex legends stats"""
    def __init__(self, player, platform: str = 'pc'):
        self.player = player
        self.platform = platform
        self.r = requests.get(f'https://public-api.tracker.gg/apex/v1/standard/profile/{platformConvert(self.platform)}/{self.player}', headers = headers).json()
        # try:
        #     if self.r["errors"]:
        #     raise UnvailableServices("API DOWN")
        #     quit()
        # except:
        #     pass

    def getStats(self):
        platform = 'xbl' if platformConvert(self.platform) == '1' else self.platform
        data = {"level":self.r['data']['metadata']['level'],
                "name":self.r['data']['metadata']['platformUserHandle'],
                "profile":f"https://apex.tracker.gg/profile/{platform}/{self.player}"}
        stat_tmp, legends_stat = {}, []
        for i, _data in enumerate(self.r['data']['children']):
            stat_tmp['legend'] = _data['metadata']['legend_name']
            for stat in _data['stats']:
                stat_tmp[stat['metadata']['name']] = str(stat['displayValue'])
            legends_stat.append({str(i):stat_tmp})
            stat_tmp = {}

        data['legends'] = legends_stat
        all_stats = {}
        for _all in self.r['data']['stats']:
            if _all['metadata']['name'] != 'Level':
                all_stats[_all['metadata']['name']] = _all['displayValue']

        data['all'] = all_stats
        return data

    def statsExists(self):
        try:
            if self.r["errors"]:
                return False
        except:
            return True

    def doRequestStatus(self): #Just do a request for apexlegendsstatus database
        try:
            return requests.get(f'http://api.mozambiquehe.re/bridge?platform={legendStatusConvert(self.platform)}&player={self.player}&auth={AUTH}&version=2')
        except Exception as e:
            print(f'{type(e).__name__} : {e}')
            return

    def iconUrl(self):
        return self.r['data']['children'][0]['metadata']['icon']
