#!/usr/bin/env python3
#coding:utf-8
import requests, os
headers={'TRN-Api-Key':os.environ['TRN_API_KEY']}

def data_parser(pseudo, platform = 'pc'):
    _json = requests.get('https://public-api.tracker.gg/apex/v1/standard/profile/{}/{}'.format(platform_convert(platform),pseudo),
                        headers = headers).json()
    data = {"level":_json['data']['metadata']['level'],
            "name":_json['data']['metadata']['platformUserHandle'],
            "profile":"https://apex.tracker.gg/profile/{}/{}".format(platform,pseudo)}
    stat_tmp = {}
    legends_stat=[]
    for i,_data in enumerate(_json['data']['children']):
        stat_tmp['legend'] = _data['metadata']['legend_name']
        for stat in _data['stats']:
            stat_tmp[stat['metadata']['name']] = str(stat['value'])
        legends_stat.append({str(i):stat_tmp})
        stat_tmp = {}
    data['legends'] = legends_stat
    return data

def platform_convert(s):
    if s.lower() == 'pc': return 5
    elif s.lower() == 'psn': return 2
    elif s.lower() == 'xbox': return 1
