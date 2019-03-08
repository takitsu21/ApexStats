#!/usr/bin/env python3
#coding:utf-8
import requests
headers={'TRN-Api-Key':'590406fa-b989-4cb6-8085-45ff22ba89ed'}

def get_data(pseudo, platform=5):
    json = requests.get('https://public-api.tracker.gg/apex/v1/standard/profile/{}/{}'.format(platform,pseudo),
                        headers=headers).json()
    legend_list, name, value, rank, legend_number, dic_stats = [], [], [], [], [], {}

    for data in json['data']['children']:
        legend_number.append(data['id'])
        legend_list.append(data['metadata']['legend_name'])

        for stat in data['stats']:
            name.append(stat['metadata']['name'])
            value.append(stat['value'])
            rank.append('Rank# {}'.format(stat['displayRank']))

        zipped_stats = list(zip(value, name, rank))
        dic_stats[data['metadata']['legend_name']] = zipped_stats
        zipped_stats = None
        name, value, rank = [], [], []

    tmp_L = []
    res = '```yaml\n [{}]\n\n'.format(pseudo)
    for item in dic_stats.items():
        for j in range(len(item[1])):
            for z in range(len(item[1][j])):
                tmp_L.append(item[1][j][z])
            tmp_L.append('\n')
        res += item[0] + '\n  ' + '  '.join(str(c) for c in tmp_L) + '\n'
        tmp_L = []
    res += '```'
    return res

def platform_convert(s):
    if s.lower() == 'pc': return 5
    elif s.lower() == 'psn': return 2
    elif s.lower() == 'xbox': return 1
