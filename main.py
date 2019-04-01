#!/usr/bin/env python3
#coding:utf-8
import discord, re, time, datetime, os, aiohttp, asyncio
from discord.ext import commands
from ressources.stats import *
import ressources.web_scrapper as scrap_data
import ressources.SqlManagment as SqlManagment
from cogs import Leaderboard, APServer, Bot_Info, Reddit, Help, Apex, DataBase, FunCommands

client = commands.Bot(command_prefix='!', activity=discord.Game(name='Rebooting...'),
                      status=discord.Status('idle'), afk=True)

@client.event
async def on_guild_join(ctx):
    await ctx.owner.send('Thanks for inviting me!\nPrefix : !\n Type !aphelp to get the commands!')

# @client.event
# async def on_member_join(ctx):
    # pass

@client.event
async def on_ready():
    await client.wait_until_ready() # Waiting for the bot to be ready
    client.remove_command("help") # To remove the default created help command, so later the bot can add its own.
    # Adding Cogs
    try:
        for file in os.listdir("cogs/"):
            if file.endswith(".py"):
                client.load_extension(f'cogs.{file.split(".")[0]}')
        print('All cogs loaded!')
    except Exception as e:
        print(f"Cogs can't be loaded\n{type(e).__name__} : {e}")
    nb_users, acc, t = 0, 0, 0
    while True:
        for s in client.guilds:
            nb_users += len(s.members)

        while True:
            # now = datetime.datetime.now()
            # real_time = f'{now.hour:0>2}:{now.minute:0>2}'
            # if real_time == '03:00':
            #     leaderboard = sortedLeaderboard()
            if t >= 600:
                t, acc = 0, 0
                break #Update count every 10 mins
            elif acc % 2 == 0:
                t+=15
                acc += 1
                await client.change_presence(activity=discord.Activity(name='!aphelp (API DOWN) WAITING FOR A FIX', type=2))
                await asyncio.sleep(15)
            else:
                t+=10
                acc+=1
                await client.change_presence(activity=discord.Activity(name=f'{nb_users} Users & {len(client.guilds)} Servers', type=3))
                await asyncio.sleep(10)
        nb_users = 0

client.run(os.environ['TOKEN'])
