#!/usr/bin/env python3
#coding:utf-8
import requests, re, unicodedata, random
from bs4 import BeautifulSoup
from ressources.exceptions import *

user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'}
reddit = 'https://www.reddit.com'
SERVERS = 'https://apexlegendsstatus.com/datacenters'

def checkDaily(a): #Cuz we don't want daily_discussion
    a_list = a.split('/')
    for c in a_list:
        if re.match(r'^(daily_discussion)\w+',c):
            return False
    return True

def getSubjectTitle(a):
    return a.split('/')[len(a.split('/'))-2]

def redditPost(filter):
    url = f'{reddit}/r/apexlegends/{filter}'
    response = requests.get(url, headers=user_agent)
    page = BeautifulSoup(response.content, features="lxml")
    redditPost = []
    checkList = []
    for a in page.find_all('a',href=True):
        if a['href'].startswith('/r/apexlegends/comments/') and reddit + a['href'] not in checkList and checkDaily(a['href']):
            checkList.append(reddit + a['href'])
            redditPost.append('[r/apexlegends/{}]({})\n'.format(getSubjectTitle(a['href']), reddit + a['href']))
    return '\n'.join(redditPost)

class ApexStatus:
    """Returns Apex Legends server status"""
    def __init__(self):
        self.response = requests.get(SERVERS, cookies={'lang': 'EN'})
        self.page = BeautifulSoup(self.response.content, features="lxml")

    def get_server_status(self):
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
                    latency_normalize = '⚠️'
                elif latency_normalize.lower() == 'down':
                    latency_normalize = '`❌`'
                else:
                    latency_normalize = '✔️'
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
            old_res = res
            if acc % 2 == 0:
                res+= '**{}** : {} {}   |  '.format(key, value['ping'], value['latency_msg'])
            else:
                res+= '**{}** : {} {}\n'.format(key, value['ping'], value['latency_msg'])
            if len(res) >= 2000:
                return old_res
            acc+=1
        return res

class ApexNews:
    """Returns last 6 Apex Legends news"""
    def __init__(self, lang, limit=6):
        self.news_url = "https://www.ea.com/games/apex-legends/news"
        self.lang = lang
        self.r = requests.get(self.news_url, cookies={'lang':self.lang}, headers=user_agent)
        self.page = BeautifulSoup(self.r.content, features="lxml")
        self.limit = limit
        if not self.r.status_code == 200:
            raise UnvailableServices(self.r.status_code)
            quit()

    def get_news(self):
        news_link = []
        acc = 1
        for c in self.page.find_all("a", href=True):
            if str(c['href']).startswith('/games/apex-legends/news/') and len(news_link) < self.limit:
                if self.lang == 'en':
                    news_link.append('**#{}** {}{}'.format(acc, "https://www.ea.com",c['href']))
                    acc += 1
                else:
                    news_link.append('**#{}** {}{}'.format(acc, f"https://www.ea.com/{self.lang}-{self.lang}"
                                                   ,c['href']))
                    acc += 1
        return '\n\n'.join(news_link)
