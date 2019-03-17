#!/usr/bin/env python3
#coding:utf-8
import requests, re, unicodedata
from random import randint
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'}
reddit = 'https://www.reddit.com'
status = 'https://apexlegendsstatus.com/datacenters'

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
        self.response = requests.get(status, cookies={'lang': 'EN'})
        self.page = BeautifulSoup(self.response.content, features="lxml")

    def get_server_status(self, region):
        referencies = {'eu':'europe','na':'north america',
                       'sa':'south america','as':'asia','oc':'oceania'}
        servers=[]
        ping = []
        status = {}
        tag = BeautifulSoup(self.response.content, features='lxml')
        for i in range(len(tag.find_all("div", class_="container"))):
            print(tag.find("div", class_="container").div)
            # if 'europe' in str(tag.find_all("div", class_="container")).lower():
        # for i in range(len(self.page.find_all("div",class_="card-header"))):
        #     try:
        #         soup_server = BeautifulSoup(str(self.page.find_all("div",class_="card-header")[i]), features='lxml')
        #         server = unicodedata.normalize("NFKD", soup_server.get_text())
        #         soup_ms = BeautifulSoup(str(self.page.find_all("p",class_="card-text")[i]), features='lxml')
        #         ms = unicodedata.normalize("NFKD", soup_ms.get_text())
        #         last_div_tag = tag.find("div", class_="container")
        #         status[server.lstrip()] = ms
        #     except Exception as e:
        #         print(e)

            # servers.append(server.lstrip())
            # ping.append(ms)
        # print(status)

    def save_content(self):
        with open('status.html','w',encoding='utf8') as f:
            f.write(self.response.text)
