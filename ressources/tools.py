#!/usr/bin/env python3
#coding:utf-8
import os
headers={'TRN-Api-Key':os.environ['TRN_API_KEY']}
AUTH=os.environ['AUTH']

def platformConvert(s): #apex.tracker.gg
    return {"pc":"5", "psn":"2", "xbox":"1"}[s.lower()]

def generate_url_profile(platform, player):
    return f"https://tracker.gg/apex/profile/{platform}/{player}/overview"