#!/usr/bin/env python3
#coding:utf-8
import discord, re, time, datetime, os, aiohttp, asyncio
from discord.ext import commands
from cogs import *

client = commands.Bot(command_prefix='a!', activity=discord.Game(name='Updating...'),
                      status=discord.Status('idle'), afk=True)

@client.event
async def on_guild_join(ctx):
    embed = discord.Embed(title='**Nice to meet you!**',
                        colour=0xff0004,
                        description= "Thanks for inviting me!")
    embed.add_field(name="**Prefix**", value="`a!`")
    embed.add_field(name="**About Apex Stats**",
                    value="Type `a!help` to get all the commands!")
    embed.set_footer(text="Made by Taki#0853 (WIP)")
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
                print(f"{file} loaded")
        except Exception as e:
            print(f"{file} can't be loaded :\n {type(e).__name__} : {e}")
    print('All cogs loaded!')
    await client.change_presence(activity=discord.Activity(name='[a!help] | Apex Legends', type=3))

client.run(os.environ['TOKEN'])
