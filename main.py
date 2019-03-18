#!/usr/bin/env python3
#coding:utf-8
import discord, re, time, datetime, os, aiohttp, asyncio
from discord.ext import commands
from ressources.stats import *
import ressources.web_scrapper as scrap_data

client = commands.Bot(command_prefix='!')
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
                data = data_parser(args[1], args[2])
                embed = discord.Embed(colour=colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                all_value, res = '', ''
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.set_author(name='{} | Level {}'.format(data['name'],data['level']) , url=data['profile'], icon_url=client.user.avatar_url)
                for i, key in enumerate(data['legends']):
                    legend = key[str(i)].get('legend')
                    for value in key[str(i)]:
                        if key[str(i)][value] != legend:
                            res += '**{}** : {}\n'.format(value, int(float(key[str(i)][value])))
                    embed.add_field(name = '**{}**'.format(legend), value='{}'.format(res), inline=True)
                    res = ''
                for key, value in data['all'].items():
                    all_value += '**{}** : {}\n'.format(key, value)
                embed.add_field(name = '**All Stats**', value='{}'.format(all_value), inline=True)
                embed.set_footer(text="data provided by apex.tracker.gg | Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)

            elif len(args) == 2:
                data = data_parser(args[1])
                embed = discord.Embed(colour=colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                all_value, res = '', ''
                embed.set_thumbnail(url=message.author.avatar_url)
                embed.set_author(name='{} | Level {}'.format(data['name'],data['level']) , url=data['profile'], icon_url=client.user.avatar_url)
                for i, key in enumerate(data['legends']):
                    legend = key[str(i)].get('legend')
                    for value in key[str(i)]:
                        if key[str(i)][value] != legend:
                            res += '**{}** : {}\n'.format(value, key[str(i)][value])
                    embed.add_field(name = '__{}__'.format(legend), value='{}'.format(res), inline=True)
                    res = ''
                for key, value in data['all'].items():
                    all_value += '**{}** : {}\n'.format(key, value)
                embed.add_field(name = '__All Stats__', value='{}'.format(all_value), inline=True)
                embed.set_footer(text="data provided by apex.tracker.gg | Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Command: !apex", description="!apex <username> - Return Apex Legends stats for PC\n!apex <username> <platform> (XBOX,PSN)", colour=colour)
            embed.set_thumbnail(url=client.user.avatar_url)
            embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
            print(e)
            await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!aphelp'):
        with open('commands.txt','r',encoding='utf8') as f:
            embed = discord.Embed(title='__Commands__:', description=''.join(f.readlines()), colour=colour)

        embed.set_thumbnail(url=client.user.avatar_url)
        embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
        try:
            ch = await client.start_private_message(message.author)
            await client.send_message(ch, embed=embed)
        except:
            await client.send_message(message.channel, embed = embed)

    if message.content.startswith('!reddit'):
        args = message.content.split(' ')
        try:
            reddit_parameter = args[1]
            if reddit_parameter == 'hot':
                msg = scrap_data.reddit_post('hot')
            elif reddit_parameter == 'top':
                msg = scrap_data.reddit_post('top')
            await client.send_message(message.channel, msg)
        except Exception as e:
            embed = (discord.Embed(title='Command: !reddit', description='!reddit <hot/top> - Return random recent hot/top on r/apexlegends', colour=colour))
            embed.set_thumbnail(url=client.user.avatar_url)
            embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed = embed)

    if message.content.startswith('!support'):
        embed = (discord.Embed(title='Support me :', description='Hey if you like my work and want to support me, you can do it here [Patreon](https://www.patreon.com/takitsu) or here [Buy me a Kofi](https://ko-fi.com/takitsu)', colour=colour))
        embed.set_thumbnail(url=client.user.avatar_url)
        embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed = embed)

    if message.content.startswith('!invite'):
        await client.send_message(message.channel, '{0.author.mention} https://discordbots.org/bot/551446491886125059/'.format(message))

    if message.content.startswith('!apvote'):
        await client.send_message(message.channel, '{0.author.mention} https://discordbots.org/bot/551446491886125059/vote'.format(message))

    if message.content.startswith('!leaderboard'):
        pass

    if message.content.startswith('!apserver'):
        try:
            Aps = scrap_data.ApexStatus()
            embed = discord.Embed(title='Apex Servers status', description='{}'.format(Aps.status()), colour=colour)
            embed.set_thumbnail(url=client.user.avatar_url)
            embed.set_footer(text="using apexlegendsstatus.com | Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed = embed)
        except:
            embed = discord.Embed(title='Apex Servers Status', description='[Apex Server Status](https://apexlegendsstatus.com/datacenters)', colour=colour)
            embed.set_thumbnail(url=client.user.avatar_url)
            embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)

    if message.content.startswith('!discord'):
        await client.send_message(message.channel, '{0.author.mention} https://discordapp.com/invite/wTxbQYb'.format(message))

@client.event
async def on_ready():
    active_servers = client.servers
    nb_users = 0
    while True:
        for s in active_servers:
            nb_users += len(s.members)
        await client.change_presence(game=discord.Game(name='!aphelp | Users: {} Servers : {}'.format(nb_users, len(active_servers))))
        nb_users = 0
        await asyncio.sleep(600)

client.run('NTUxNDQ2NDkxODg2MTI1MDU5.D2_K7A.B05cMHBVG_2Cin5cyQEynZC6WOc')
# client.run(os.environ['TOKEN'])
