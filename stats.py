#!/usr/bin/env python3
#coding:utf-8
import requests
headers={'TRN-Api-Key':'590406fa-b989-4cb6-8085-45ff22ba89ed'}

def get_data(pseudo, platform = 'pc'):
    _json = requests.get('https://public-api.tracker.gg/apex/v1/standard/profile/{}/{}'.format(platform_convert(platform),pseudo),
                        headers = headers).json()
    data = {"level":_json['data']['metadata']['level'],
            "name":_json['data']['metadata']['platformUserHandle'],
            "profile":"https://apex.tracker.gg/profile/{}/{}".format(platform,pseudo)}
    dic_tmp = {}
    legends_stat=[{}]
    for _data in _json['data']['children']:
        for stat in _data['stats']:
            dic_tmp[stat['metadata']['name']] = stat['value']
            # rank.append('Rank# {}'.format(stat['displayRank']))
        print(dic_tmp)
        legends_stat[0][_data['metadata']['legend_name']] = set(dic_tmp)
        # data[_data['metadata']['legend_name']] = dic_tmp
        dic_tmp = {}
    data['legends']= legends_stat
    return data


def platform_convert(s):
    if s.lower() == 'pc': return 5
    elif s.lower() == 'psn': return 2
    elif s.lower() == 'xbox': return 1
