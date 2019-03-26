#!/usr/bin/env python3
#coding:utf-8
import requests, os
import ressources.SqlManagment as SqlManagment

headers={'TRN-Api-Key':os.environ['TRN_API_KEY']}
AUTH=os.environ['AUTH']

def platformConvert(s): #apex.tracker.gg
    if str(s).lower() == 'pc': return '5'
    elif str(s).lower() == 'psn': return '2'
    elif str(s).lower() == 'xbox': return '1'

def legendStatusConvert(platform: str = 'pc'): #apexlegendsstatus
    if platform.lower() == 'pc': return 'PC'
    if platform.lower() == 'psn': return 'PS4'
    if platform.lower() == 'xbox': return 'X1'

class Stats:
    def __init__(self, player, platform: str = 'pc'):
        self.player = player
        self.platform = platform
        self.r = requests.get(f'https://public-api.tracker.gg/apex/v1/standard/profile/{platformConvert(self.platform)}/{self.player}', headers = headers).json()


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
        return requests.get(f'https://public-api.tracker.gg/apex/v1/standard/profile/{platformConvert(self.platform)}/{self.player}', headers = headers).status_code == 200

    def doRequestStatus(self): #Just do a request
        try:
            return requests.get(f'http://api.apexlegendsstatus.com/bridge?platform={legendStatusConvert(self.platform)}&player={self.player}&auth={AUTH}&version=2')
        except Exception as e:
            print(f'{type(e).__name__} : {e}')
            return
            
    def iconUrl(self):
        return self.r['data']['children'][0]['metadata']['icon']

    def leaderboardInit(self, leaderboard : dict = SqlManagment.createLeaderboard()):
        data_stats = {}
        for player, platform in leaderboard.items():
            if self.statsExists(player, platform):
                data_stats[self.r['data']['metadata']['platformUserHandle']] = r['data']['metadata']['level']
        return data_stats

    def sortedLeaderboard(self):#+ to - by level
         key_value ={}
         return sorted(self.leaderboardInit().items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
