#!/usr/bin/env python3
#coding:utf-8
import requests, re, unicodedata
from random import randint
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'}
reddit = 'https://www.reddit.com'
SERVERS = 'https://apexlegendsstatus.com/datacenters'

def check_daily(a):
    a_list = a.split('/')
    for c in a_list:
        if re.match(r'^(daily_discussion)\w+',c):
            return False
    return True

def reddit_post(filtre):
    url = '{}/r/apexlegends/{}'.format(reddit,filtre)
    response = requests.get(url, headers=headers)
    page = BeautifulSoup(response.content, features="lxml")
    hot_reddit_post = []
    for a in page.find_all('a',href=True):
        if a['href'].startswith('/r/apexlegends/comments/') and a['href'] not in hot_reddit_post and check_daily(a['href']):
            hot_reddit_post.append(a['href'])
    return reddit + hot_reddit_post[randint(0,len(hot_reddit_post)-1)]

class ApexStatus:
    def __init__(self):
        self.response = requests.get(SERVERS, cookies={'lang': 'EN'})
        self.page = BeautifulSoup(self.response.content, features="lxml")

    def get_server_status(self):
        # referencies = {'eu':'europe','na':'north america',
        #                'sa':'south america','as':'asia','oc':'oceania'}
        info_server, status = {}, {}
        for i in range(len(self.page.find_all("div",class_="card-header"))):
            try:
                soup_server = BeautifulSoup(str(self.page.find_all("div",class_="card-header")[i]), features='lxml')
                server_normalize = unicodedata.normalize("NFKD", soup_server.get_text())
                soup_ms = BeautifulSoup(str(self.page.find_all("p",class_="card-text")[i]), features='lxml')
                ms_normalize = unicodedata.normalize("NFKD", soup_ms.get_text()).split(' ')[0]
                soup_latency_msg = BeautifulSoup(str(self.page.find_all("h4", class_="card-title")[i]), features='lxml')
                latency_normalize = unicodedata.normalize("NFKD", soup_latency_msg.get_text())
                if latency_normalize.lower() == 'high latency':
                    latency_normalize = ':warning:'
                elif latency_normalize.lower() == 'down':
                    latency_normalize = ':x:'
                else:
                    latency_normalize = ':white_check_mark:'
                info_server['ping'] = ms_normalize
                info_server['latency_msg'] = latency_normalize
                status[server_normalize.lstrip()] = info_server
                info_server = {}
            except Exception as e:
                print(e)
        return status

    def status(self):
        res = ''
        acc = 0
        for key, value in self.get_server_status().items():
            if acc % 2 == 0:
                res+= '**{}** : {} {}  |   '.format(key, value['ping'], value['latency_msg'])
            else:
                res+= '**{}** : {} {}\n'.format(key, value['ping'], value['latency_msg'])
            acc+=1
        res += '\n(This feature will be improve)'
        return res
