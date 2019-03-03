#coding:utf-8
import discord, logging, re
from stats import *

headers={'TRN-Api-Key':'590406fa-b989-4cb6-8085-45ff22ba89ed'}
CLIENT_SECRET='Bp0gN1Ieb6YBqXvsIq4NRVZ0FhoDrsnH'
CLIENT_ID=551446491886125059
TOKEN='NTUxNDQ2NDkxODg2MTI1MDU5.D1xGrw.UR40QVPCnnrrSCqlG0SV_zT1d7s'
url='https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(CLIENT_ID)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client=discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!purge'):
        args=message.content.split(' ')
        if args[1].isdigit():
            await client.purge_from(message.channel,limit=int(args[1])+1)
        elif args[1] == 'all':
            await client.purge_from(message.channel,limit=float("inf"))
        else:
            await client.send_message(message.channel,'{0.author.mention} Réssayez avec ```!purge [nb_message]```'.format(message))

    if message.content.startswith('!mention'):
        args=message.content.split(' ')
        member_found=False
        for member in [str(c) for c in client.get_all_members()]:
            if re.match(r'^({}#)[0-9]+'.format(args[1].lower()) ,member.lower()):
                print(client.get_user_info(member))
                msg = 'qsdsq'
                member_found=True
                # await client.send_message(message.channel, msg)
                break
        if not member_found:
            await client.send_message(message.channel, '{0.author.mention} L\'utilisateur a mentionné n\'a pas été trouvé'.format(message))

    # if message.content.startswith('!members'):
    #     print([str(c) for c in client.get_all_members()])


    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

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
                await client.send_message(message.channel, '{0.author.mention} Un argument manquant ou eronné ```!apex NAME [PC, PS4, XBOX]```'.format(message))


@client.event
async def on_ready():
    logged = 'Logged in as {} ID : {}'.format(client.user.name,client.user.id)
    print(logged,len(logged)*'-',sep='\n')


client.run(TOKEN)
