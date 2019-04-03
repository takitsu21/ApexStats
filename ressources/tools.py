#!/usr/bin/env python3
#coding:utf-8

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
