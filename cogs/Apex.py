import time
import datetime
import asyncio
import discord
from discord.ext import commands
from ressources.stats import *
from ressources.exceptions import PlayerNotFound
from ressources.tools import generate_url_profile

class Apex(commands.Cog):
    def __init__(self, bot):
        """Display apex stats"""
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def ranked(self, ctx):
        about_ranked = "https://www.reddit.com/r/apexlegends/comments/c7w3iq/how_ranked_leagues_will_work_in_season_2_of_apex/"
        embed = discord.Embed(title="About ranked",
                        colour=self.colour,
                        timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                        description=f"To know how ranked works go -> [here]({about_ranked})")
        embed.set_thumbnail(url= ctx.guild.me.avatar_url)
        embed.set_footer(text="data provided by apex.tracker.gg | Mad with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)            
    async def map(self, ctx):
        embed = discord.Embed(title="Map & loot Tier", colour=self.colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url="https://i.imgur.com/SuGEoSs.jpg")
        embed.set_footer(text="Mad with ❤️ by Taki#0853 (WIP)",
                         icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)     

    def embed_stats(self, ctx, data):
        legend, res, overview = "", "", ""
        player = '%20'.join(data["platformInfo"]["platformUserHandle"].split(" "))
        platform = data["platformInfo"]["platformSlug"]
        embed = discord.Embed(
            colour=self.colour,
            timestamp=datetime.datetime.utcfromtimestamp(time.time())
        )
        embed.set_thumbnail(url = data["segments"][0]["stats"]["rankScore"]["metadata"]["iconUrl"])
        embed.set_author(
            name='{0} | Level {1} | Elo : {2}'.format(
            data["platformInfo"]["platformUserHandle"],
            int(data["segments"][0]["stats"]["level"]["value"]),
            data["segments"][0]["stats"]["rankScore"]["displayValue"]
        ),
            url=generate_url_profile(platform, player),
            icon_url=data["platformInfo"]["avatarUrl"]
        )
        for i, stats in enumerate(data["segments"]):
            try:
                if i == 0:
                    for i, children in enumerate(stats["stats"]):
                        if i > 0:
                            overview += '*{}* : `{}`\n'.format(stats["stats"][children]["displayName"], str(int(stats["stats"][children]["value"])))

                else:
                    legend = stats["metadata"]["name"]
                    for children in stats["stats"]:
                        res += '*{}* : `{}`\n'.format(stats["stats"][children]["displayName"], str(int(stats["stats"][children]["value"])))
                    if len(res) > 0:
                        embed.add_field(name = '__`{}`__'.format(legend), value='{}'.format(res), inline=True)
                        res = ''
            except Exception as e:
                print(f"{type(e).__name__} : {e}")
        embed.add_field(name = f'__`Lifetime`__', value='{}'.format(overview), inline=True)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg", icon_url=ctx.guild.me.avatar_url)
        return embed

    @staticmethod
    def parse_user(args, platform):
        if len(args) > 1:
            platform = args.pop().lower()
        if platform in ["pc", "xbox", "psn"]:
            user = '%20'.join(args)
        return user, platform

    @commands.command(aliases=["s"])
    async def stats(self, ctx, *args, platform = "pc"):
        """Displays apex stats for a given player (and platform)"""
        try:
            finding = await ctx.send("`📡Fetching data...📡`")
            info = self.parse_user(list(args), platform)
            player, platform = info[0], info[1]
            if platform in ['pc','xbox','psn']:
                stats = Stats(player, platform)
                if len(player) >= 1:
                    data = stats.data()
                    embed = self.embed_stats(ctx, data)
            else:
                embed = discord.Embed(title="❌Wrong platform!❌", colour=self.colour,
                description=f'{ctx.author.mention} Wrong platform! retry with `pc` | `xbox` | `psn`')
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg", icon_url=ctx.guild.me.avatar_url)
        except discord.errors.HTTPException as e: #if len(data) > 2000
            print(type(e).__name__, e)
            embed = discord.Embed(title="**Too Many Stats to show!**",
                                description=f"Sorry, but i couldn't show your stats. It's too big.\nYou can see your profile [__**here**__]({generate_url_profile(data['platformInfo']['platformSlug'], player)})",
                                timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
            embed.set_thumbnail(url= ctx.guild.me.avatar_url)
        except PlayerNotFound:
            embed = discord.Embed(title="❌Stats not found!❌", description="Sorry but i couldn't found your Apex Legends Statistics.\nYou may have made a foul of strikes.\n\nIf you spelled it right then the API might be down.",colour=self.colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        except Exception as e:
            print(type(e).__name__, e)
            embed = discord.Embed(title="**Command**: **`a!stats`**",
                                  description="**`a!stats [USERNAME]`**\n**`a!stats [USERNAME] < pc | xbox | psn >`**",
                                  timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
            embed.add_field(name="Stats explanation", value="- Stats are provided by [apex.tracker.gg](https://apex.tracker.gg/) API (stats might not be fully exact)\n\n- We can only get stats from selected banners\n\n- To update a legend stats you have to pick the legend wanted and then do **`a!stats [USERNAME] < pc | xbox | psn >`**\n\n- It will keep all update you've done on your account\n\n- The «Lifetime» value is just the sum of all banner **AVAILABLE** and **SELECTED** on each legends")
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg", icon_url=ctx.guild.me.avatar_url)
        await finding.edit(content="",embed=embed)

def setup(bot):
    bot.add_cog(Apex(bot))
