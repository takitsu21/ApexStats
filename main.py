#coding:utf-8
import discord, logging, re
from stats import *

TOKEN='NTUxNDQ2NDkxODg2MTI1MDU5.D1xGrw.UR40QVPCnnrrSCqlG0SV_zT1d7s'
# url='https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(CLIENT_ID)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client=discord.Client()

COMMANDS = ['!clean [number_message](not available now)','!apex [name] [platform](set default to PC if no platform mentionned)']


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Need to set permission to uncomment
    # if message.content.startswith('!clean'):
    #     args=message.content.split(' ')
    #     if args[1].isdigit():
    #         await client.purge_from(message.channel,limit=int(args[1])+1)
    #     elif args[1] == 'all':
    #         await client.purge_from(message.channel,limit=float("inf"))
    #     else:
    #         await client.send_message(message.channel,'{0.author.mention} Réssayez avec ```!purge [nb_message]```'.format(message))

    if message.content.startswith('!apex'):
        args = message.content.split(' ')
        if len(args) > 0:
            pseudo = args[1]
            if len(args) == 3:
                platform = platform_convert(args[2])
                await client.send_message(message.channel, get_data(pseudo, platform))
            elif len(args) == 2:
                await client.send_message(message.channel, get_data(pseudo))
            else:
                await client.send_message(message.channel, '{0.author.mention} Un argument manquant ou eronné ```yaml\n!apex [name] [platform](set default to PC if no platform mentionned)```'.format(message))

    if message.content.startswith('!help'):
        await client.send_message(message.channel, '{0.author.mention} ```{}```'.format(message,' \n'.join(COMMANDS)))


@client.event
async def on_ready():
    logged = 'Logged in as {} ID : {}'.format(client.user.name,client.user.id)
    print(logged,len(logged)*'-',sep='\n')


client.run(TOKEN)
