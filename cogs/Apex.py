import discord
import time, datetime
from discord.ext import commands
from ressources.stats import *

class Apex:
  def __init__(self,bot):
    """Pass the bot in as the bot not a string or a value, pass the client created using commands.Bot()"""
    self.bot = bot
  
  @commands.command(pass_context=True)
  async def apex(self,ctx):
    """Displays apex stats for a given player (and platform)"""
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
                            res += '**{}** : {}\n'.format(value, key[str(i)][value])
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
            await ctx.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(title="Command: !apex", description="!apex <username> - Return Apex Legends stats for PC\n!apex <username> <platform> (XBOX,PSN)", colour=colour)
            embed.set_thumbnail(url=client.user.avatar_url)
            embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
            print(e)
            await ctx.send(embed=embed)
  
  
def setup(bot):
   bot.add_cog(Apex(bot))
   print("Added Apex Cog from Cogs!")
