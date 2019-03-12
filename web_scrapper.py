#!/usr/bin/env python3
#coding:utf-8
import requests, re
from random import randint
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'}
reddit = 'https://www.reddit.com'

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
