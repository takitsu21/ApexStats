import discord
import time, datetime
from discord.ext import commands
from ressources.stats import *
from ressources.exceptions import PlayerNotFound

class Apex(commands.Cog):
    def __init__(self, bot):
        """Display apex stats"""
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def debug(self, ctx, member):
        # for member in ctx.message.guild.members:
        #     print(member)
            # for member in server.members:
            #     print(member, member.id)
        for memb in ctx.message.guild.members:
            print(memb.name)
            if memb.name.lower() == member:
                embed = discord.Embed(title=f"{member} has been found as {memb.id} {self.bot.get_user(memb.id)}")
                await ctx.send(embed=embed)
            

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
                    data = stats.single_data()
                    embed = discord.Embed(colour=self.colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                    all_value, res = '', ''
                    embed.set_thumbnail(url = stats.get_icon())
                    embed.set_author(name='{} | Level {}'.format(data['name'],data['level']) ,
                                    url=data['profile'],
                                    icon_url=client_icon)

                    for i, key in enumerate(data['legends']):
                        legend = key[str(i)].get('legend')
                        for value in key[str(i)]:
                            if key[str(i)][value] != legend:
                                res += '***{}*** : ***`{}`***\n'.format(value, key[str(i)][value])
                        # if i == 0:
                        #     embed.add_field(name = '__`{}`__'.format(legend), value='{}'.format(res), inline=True)
                        # else:
                        embed.add_field(name = '__`{}`__'.format(legend), value='{}'.format(res), inline=True)
                        res = ''
                    for key, value in data['all'].items():
                        all_value += '***{}*** : ***`{}`***\n'.format(key, value)
                    embed.add_field(name = '__**`All Stats`**__',
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

        except PlayerNotFound:
            embed = discord.Embed(title="Stats not found!", description="Sorry but i couldn't found your Apex Legends Statistics.\nYou may have made a foul of strikes.\n\nIf you spelled it right then the API might be down.",colour=self.colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url = client_icon)
            embed.set_footer(text="data provided by apex.tracker.gg | Made by Taki#0853 (WIP)",
                            icon_url=client_icon)
            await finding.edit(content='', embed=embed)

        except Exception as e:
            embed = discord.Embed(title="**Command**: **`a!stats`**",
                                  description="**`a!stats <username>`**\n**`a!stats <username> <platform>(pc,xbox,psn)`**",
                                  timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
            embed.add_field(name="Stats explanation", value="- Stats are provided by [apex.tracker.gg](https://apex.tracker.gg/) API (stats might not be fully exact)\n\n- We can only get stats from selected banners\n\n- To update a legend stats you have to pick the legend wanted and then do **`a!stats <username> <platform>`**\n\n- It will keep all update you've done on your account\n\n- The «All Stats» value is just the sum of all banner **AVAILABLE** and **SELECTED** on each legends")
            embed.set_thumbnail(url=client_icon)
            embed.set_footer(text="data provided by apex.tracker.gg | Made by Taki#0853 (WIP)",
                             icon_url=client_icon)
            print(e)
            await finding.edit(content='', embed=embed)

def setup(bot):
    bot.add_cog(Apex(bot))
    print("Added Apex")
