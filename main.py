#!/usr/bin/env python3
#coding:utf-8
import discord, logging, re, reddit
from stats import *


TOKEN='NTUxNDQ2NDkxODg2MTI1MDU5.D1xGrw.UR40QVPCnnrrSCqlG0SV_zT1d7s'
# url='https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(CLIENT_ID)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client=discord.Client()

COMMANDS = ['!clean','!apex','!reddit']
colour = 0xc8db

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Need to set permission to uncomment
    if message.content.startswith('!clean'):
        embed = (discord.Embed(title='Command: !clean', description='!clean number_message (Limit all)\nNot available now', colour=colour))
        await client.send_message(message.channel, embed=embed)
    #     args=message.content.split(' ')
    #     if args[1].isdigit():
    #         await client.purge_from(message.channel,limit=int(args[1])+1)
    #     elif args[1] == 'all':
    #         await client.purge_from(message.channel,limit=float("inf"))
    #     else:
    #         await client.send_message(message.channel,'{0.author.mention} Réssayez avec ```!purge [nb_message]```'.format(message))

    if message.content.startswith('!apex'):
        args = message.content.split(' ')
        try:
            pseudo = args[1]
            if len(args) == 3:
                platform = platform_convert(args[2])
                msg = get_data(pseudo, platform)
            elif len(args) == 2:
                msg = get_data(pseudo)
            else:
                msg = '{0.author.mention} Un argument manquant ou eronné ```yaml\n!apex pseudo platform (set default to PC if no platform mentionned)```'.format(message)
            await client.send_message(message.channel, msg)
        except:
            embed = (discord.Embed(title="Command: !apex", description="!apex pseudo\n!apex pseudo platform (XBOX,PSN)", colour=colour))
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
                msg = reddit.reddit_post('hot')
            elif reddit_parameter == 'top':
                msg = reddit.reddit_post('top')
            await client.send_message(message.channel, msg)
        except Exception as e:
            embed = (discord.Embed(title='Command: !reddit', description='!reddit hot\n!reddit top', colour=colour))
            await client.send_message(message.channel, embed=embed)

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='!apex pseudo | !help'))

client.run(TOKEN)
