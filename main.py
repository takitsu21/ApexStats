#!/usr/bin/env python3
#coding:utf-8
import discord, re, time, datetime, os, aiohttp, asyncio
from discord.ext import commands
from ressources.stats import *
import ressources.web_scrapper as scrap_data
from cogs import Leaderboard,APServer,FunCommands,Bot_Info,Reddit,Help,Apex

client = commands.Bot(command_prefix='!')
colour = 0xc8db

@client.event
async def on_ready():
    await bot.wait_until_ready() # Waiting for the bot to be ready :/
    bot.remove_command("help") # To remove the default created help command, so later the bot can add its own.
    # Adding Cogs
    Leaderboard.setup(client)
    APServer.setup(client)
    FunCommands.setup(client)
    Bot_Info.setup(client)
    Reddit.setup(client)
    Help.setup(client)
    Apex.setup(client)
    #
    active_servers = client.servers
    nb_users = 0
    while True:
        for s in active_servers:
            nb_users += len(s.members)
        await client.change_presence(game=discord.Game(name='!aphelp | Users: {} Servers : {}'.format(nb_users, len(active_servers))))
        nb_users = 0
        await asyncio.sleep(600)

client.run(os.environ['TOKEN'])
