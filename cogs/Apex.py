import discord
import time, datetime
from discord.ext import commands
from ressources.stats import *

class Apex(commands.Cog):
    def __init__(self, bot):
        """Display apex stats"""
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def stats(self, ctx, player : str = '', platform : str = 'pc'):
        """Displays apex stats for a given player (and platform)"""
        user_icon = ctx.author.avatar_url
        client_icon = ctx.guild.me.avatar_url
        try:
            finding = await ctx.send('`Finding Stats...`')
            if platform.lower() in ['pc','xbox','psn']:
                stats = Stats(player, platform)
                if len(player) >= 1:
                    data = stats.getStats()
                    embed = discord.Embed(colour=self.colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                    all_value, res = '', ''
                    embed.set_thumbnail(url = stats.iconUrl())
                    embed.set_author(name='{} | Level {}'.format(data['name'],data['level']) ,
                                     url=data['profile'],
                                      icon_url=client_icon)

                    for i, key in enumerate(data['legends']):
                        legend = key[str(i)].get('legend')
                        for value in key[str(i)]:
                            if key[str(i)][value] != legend:
                                res += '***{}*** : {}\n'.format(value, key[str(i)][value])
                        embed.add_field(name = '__{}__'.format(legend), value='{}'.format(res), inline=True)
                        res = ''

                    for key, value in data['all'].items():
                        all_value += '***{}*** : {}\n'.format(key, value)
                    embed.add_field(name = '__**All Stats**__',
                                    value='{}'.format(all_value),
                                     inline=True)
                    embed.set_footer(text="data provided by apex.tracker.gg | Made by Taki#0853 (WIP)",
                                     icon_url=client_icon)
                await finding.edit(content='',embed=embed)
                stats.doRequestStatus()

            else:
                await ctx.send(f'{ctx.author.mention} Wrong platform! retry with `pc` | `xbox` | `psn`')

        except discord.errors.HTTPException: #if len(data) > 2000
            embed = discord.Embed(title="**Too Many Stats to show!**",
                                  description=f"Sorry, but i couldn't show your stats. It's too big.\nYou can see your profile [__**here**__]({data['profile']}).",
                                  timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
            embed.set_thumbnail(url= client_icon)
            embed.set_footer(text="data provided by apex.tracker.gg | Made by Taki#0853 (WIP)",
                             icon_url=client_icon)
            await finding.edit(content='', embed=embed)

        except Exception as e:
            embed = discord.Embed(title="__Command__: **!apex**",
                                  description="!apex <username> - Returns Apex Legends stats for PC\n!apex <username> <platform> (XBOX,PSN)",
                                  timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
            embed.set_thumbnail(url=client_icon)
            embed.set_footer(text="data provided by apex.tracker.gg | Made by Taki#0853 (WIP)",
                             icon_url=client_icon)
            print(e)
            await finding.edit(content='', embed=embed)

def setup(bot):
    bot.add_cog(Apex(bot))
    print("Added Apex Cog from cogs")
