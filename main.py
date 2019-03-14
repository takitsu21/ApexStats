#!/usr/bin/env python3
#coding:utf-8
import discord, logging, re, web_scrapper, time, datetime, os
from discord.ext import commands
from stats import *

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = commands.Bot(command_prefix='!')
COMMANDS = ['!apex','!reddit','!ss','!support','!invite']
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
                data = data_parser(args[1], platform)
                embed = discord.Embed(colour=colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                res = ''
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.set_author(name='{} | Level {}'.format(data['name'],data['level']) , url=data['profile'], icon_url=client.user.avatar_url)
                for i, key in enumerate(data['legends']):
                    legend = key[str(i)].get('legend')
                    for value in key[str(i)]:
                        if key[str(i)][value] != legend:
                            res += '**{}** : {}\n'.format(value, int(float(key[str(i)][value])))
                    embed.add_field(name = '**{}**'.format(legend), value='{}'.format(res), inline=True)
                    res=''
                embed.set_footer(text="data provided by apex.tracker.gg | Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)

            elif len(args) == 2:
                data = data_parser(args[1])
                embed = discord.Embed(colour=colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                res = ''
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.set_author(name='{} | Level {}'.format(data['name'],data['level']) , url=data['profile'], icon_url=client.user.avatar_url)
                for i, key in enumerate(data['legends']):
                    legend = key[str(i)].get('legend')
                    for value in key[str(i)]:
                        if key[str(i)][value] != legend:
                            res += '**{}** : {}\n'.format(value, int(float(key[str(i)][value])))
                    embed.add_field(name = '**{}**'.format(legend), value='{}'.format(res), inline=True)
                    res=''
                embed.set_footer(text="data provided by apex.tracker.gg | Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed)

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
        embed = (discord.Embed(title='Kofi support', description='Hey if you like my work and want to support me, you can do it here [Support my creativty](https://ko-fi.com/takitsu)', colour=colour))
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!invite'):
        await client.send_message(message.channel, '{0.author.mention} https://discordapp.com/oauth2/authorize?client_id=551446491886125059&scope=bot&permissions=52224'.format(message))

    if message.content.startswith('!apvote'):
        await client.send_message(message.channel, '{0.author.mention} https://discordbots.org/bot/551446491886125059/vote'.format(message))

@client.event
async def on_ready():
    active_servers = client.servers
    nb_users = 0
    for s in active_servers:
        nb_users += len(s.members)
    await client.change_presence(game=discord.Game(name='!help | Users: {}'.format(nb_users)))

client.run(os.environ['TOKEN'])
