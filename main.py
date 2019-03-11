#!/usr/bin/env python3
#coding:utf-8
import discord, logging, re, web_scrapper
from discord.ext import commands
from stats import *


TOKEN='NTUxNDQ2NDkxODg2MTI1MDU5.D1xGrw.UR40QVPCnnrrSCqlG0SV_zT1d7s'
# url='https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(CLIENT_ID)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix='!')

# client=discord.Client()

COMMANDS = ['!apex','!reddit','!ss','!support']
colour = 0xc8db

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!apex'):
        args = message.content.split(' ')
        try:
            username = args[1]
            if len(args) == 3:
                platform = platform_convert(args[2])
                msg = get_data(username, platform)
            elif len(args) == 2:
                msg = get_data(username)
            await client.send_message(message.channel, msg)
        except:
            embed = (discord.Embed(title="Command: !apex", description="!apex username (Return Apex Legends stats)\n!apex username platform (XBOX,PSN) (Return Apex Legends stats according to the platform)", colour=colour))
            await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!help'):
        embed = (discord.Embed(title='Commands: ', description='\n'.join(COMMANDS), colour=colour))
        ch = await client.start_private_message(message.author)
        await client.send_message(ch, embed=embed)

    if message.content.startswith('!reddit'):
        args = message.content.split(' ')
        try:
            reddit_parameter = args[1]
            if reddit_parameter == 'hot':
                msg = web_scrapper.reddit_post('hot')
            elif reddit_parameter == 'top':
                msg = web_scrapper.reddit_post('top')
            await client.send_message(message.channel, msg)
        except Exception as e:
            embed = (discord.Embed(title='Command: !reddit', description='!reddit hot (Return random recent hot on r/apexlegends)\n!reddit top (Return random recent top on r/apexlegends)', colour=colour))
            await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!ss'):
        embed = (discord.Embed(title='Server Status', description='[Apex Server Status](https://apexlegendsstatus.com/datacenters)', colour=colour))
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!support'):
        embed = (discord.Embed(title='Kofi support', description='Hey if you like my work and want to support me, you can do it here [Support me](https://ko-fi.com/takitsu)', colour=colour))
        await client.send_message(message.channel, embed=embed)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='!apex username | !help'))

client.run(TOKEN)
