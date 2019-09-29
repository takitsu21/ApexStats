# !/usr/bin/env python3
# coding:utf-8
import discord
import os
from discord.ext import commands
from cogs import *
from src import __init__

client = commands.Bot(command_prefix='a!', activity=discord.Game(name='Updating...'),
                      status=discord.Status('dnd'))
                 
@client.event
async def on_ready():
    await client.wait_until_ready() # waiting internal cache to be ready
    client.remove_command("help")
    loaded = None
    fail = str()
    for file in os.listdir("cogs/"): # Adding Cogs
        try:
            if file.endswith(".py"):
                client.load_extension(f'cogs.{file.split(".")[0]}')
                print(f"{file} loaded")
        except Exception as e:
            print(f"{file} can't be loaded :\n {type(e).__name__} : {e}")
            fail += file + ", "
            loaded = False
    if loaded is None:
        print('All cogs loaded!')
    else: print(f"Cogs missing -> {fail}")
    await client.change_presence(
        activity=discord.Activity(
            name='[a!help] | Apex Legends',
            type=3))

client.run(os.environ['TOKEN'])
