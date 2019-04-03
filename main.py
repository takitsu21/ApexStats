#!/usr/bin/env python3
#coding:utf-8
import discord, re, time, datetime, os, aiohttp, asyncio
from discord.ext import commands
# from ressources.stats import *
# import ressources.web_scrapper as scrap_data
# import ressources.SqlManagment as SqlManagment
from cogs import Leaderboard, APServer, Bot_Info, Reddit, Help, Apex, DataBase, FunCommands, LeaderboardUpdate

client = commands.Bot(command_prefix='a!', activity=discord.Game(name='Updating...'),
                      status=discord.Status('idle'), afk=True)

@client.event
async def on_guild_join(ctx):
    embed = discord.Embed(title='**Nice to meet you!**',
                        colour=0xff0004,
                        description= "Thanks for inviting me!")
    embed.add_field(name="**Prefix**", value="`a!`")
    embed.add_field(name="**Commands**",
                    value="Type `a!help` to get all the commands!")
    embed.set_footer(text="Made by Taki#0853 (WIP)",
                    icon_url=ctx.guild.me.avatar_url)
    await ctx.owner.send(embed = embed)

# @client.event
# async def on_member_join(ctx):
    # pass

@client.event
async def on_ready():
    await client.wait_until_ready() # Waiting for the bot to be ready
    client.remove_command("help") # To remove the default created help command, so later the bot can add its own.
    # Adding Cogs
    for file in os.listdir("cogs/"):
        try:
            if file.endswith(".py"):
                client.load_extension(f'cogs.{file.split(".")[0]}')
        except Exception as e:
            print(f"{file} can't be loaded :\n {type(e).__name__} : {e}")
    print('All cogs loaded!')
    while True:
        await client.change_presence(activity=discord.Activity(name='[a!help] (new prefix: a!) & {} servers'.format(len(client.guilds)), type=3))
        await asyncio.sleep(600)

client.run(os.environ['TOKEN'])
