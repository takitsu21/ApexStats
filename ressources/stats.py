#!/usr/bin/env python3
#coding:utf-8
import nest_asyncio

import os, json, asyncio
from aiohttp import ClientSession
from ressources.tools import *
from ressources.exceptions import *

# import __init__
# from tools import *
# import SqlManagment as SqlManagment
# from exceptions import *

nest_asyncio.apply() #fix asyncio error

class Stats:
    """Get apex legends stats"""
    def __init__(self, player: str = "", platform: str = 'pc'):
        self.player = player
        self.base_platform = platform.lower()
        self.platform = platformConvert(platform)

    async def fetch(self, session):
        async with session.get(url, headers=headers) as resp:
            try:
                return await resp.json()
            except Exception:
                raise PlayerNotFound(resp.status)

    async def data(self) -> dict:
        """returns api.warframe.market responses -> dict"""
        global url
        url = f"https://public-api.tracker.gg/v2/apex/standard/profile/{self.platform}/{self.player}"
        async with ClientSession() as session:
            responses = await self.fetch(session)
        return responses["data"]

    async def exists(self):
        try:
            self.data()
            return True
        except PlayerNotFound:
            return False

def run(func = lambda x: x):
    """asyncio runner function using python 3.7"""
    return asyncio.run(func)