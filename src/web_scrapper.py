import re
from bs4 import BeautifulSoup
from src.utils import _request

user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'}
reddit = 'https://www.reddit.com'
SERVERS = 'https://apexlegendsstatus.com/'

class UnvailableServices(Exception):
    pass

def checkDaily(a) -> bool: # we don't want daily_discussion
    for c in a.split('/'):
        if re.match(r'^(daily_discussion)\w+',c):
            return False
    return True

def get_subj_title(a) -> str:
    a = a.split('/')
    return a[len(a)-2]

def get_post(categorie) -> str:
    """Returns reddit url filtered by categorie
    -> returns urls filtered"""
    url = f"{reddit}/r/apexlegends/{categorie}"
    content = _request(url, headers=user_agent, call="text")
    page = BeautifulSoup(content, features="lxml")
    reddit_post, check_list = [], []
    for a in page.find_all('a',href=True):
        if a['href'].startswith('/r/apexlegends/comments/') and reddit + a['href'] not in check_list and checkDaily(a['href']):
            check_list.append(reddit + a['href'])
            reddit_post.append('[r/apexlegends/{}]({})\n'.format(get_subj_title(a['href']), reddit + a['href']))
    return '\n'.join(reddit_post)

def get_server_status():
    content = _request(SERVERS, cookies={'lang': 'EN'}, call="text")
    page = BeautifulSoup(content, features="lxml")
    status = page.find(class_="alert")
    return status.get_text()

def get_news(limit=6) -> str:
    """Get news from https://www.ea.com/games/apex-legends/news"""
    news_url = "https://www.ea.com/games/apex-legends/news"
    content = _request(news_url, headers=user_agent, call="text")
    page = BeautifulSoup(content, features="lxml")
    news_link = []
    acc = 1
    for c in page.find_all("a", href=True):
        if str(c['href']).startswith('/games/apex-legends/news/') and len(news_link) < limit:
            news_link.append('**#{}** {}{}'.format(acc, "https://www.ea.com",c['href']))
            acc += 1
    return '\n\n'.join(news_link)
