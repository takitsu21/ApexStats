import time
import datetime
import discord
from discord.ext import commands
from src.stats import *
from src.utils import generate_url_profile, better_formatting
from src.decorators import trigger_typing
import logging

logger = logging.getLogger("apex-stats")

class Apex(commands.Cog):
    def __init__(self, bot):
        """Display apex stats"""
        self.bot = bot
        self.colour = 0xff0004

    @commands.command()
    @trigger_typing
    async def ranked(self, ctx):
        about_ranked = "https://www.ea.com/games/apex-legends/news/ranked-series-3-details"
        embed = discord.Embed(title="About ranked",
                        colour=self.colour,
                        timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                        description=f"To know how ranked works go -> [here]({about_ranked})")
        embed.set_thumbnail(url= ctx.guild.me.avatar_url)
        embed.set_footer(text="data provided by apex.tracker.gg | Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @trigger_typing
    async def map(self, ctx):
        embed = discord.Embed(title="Map & loot Tier (DEPRECATED)",
                            colour=self.colour,
                            timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.set_image(url="https://i.redd.it/qnb34smk41q31.jpg")
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
        embed.set_thumbnail(url = rank_url(data["segments"][0]["stats"]["rankScore"]["value"]))
        embed.set_author(
            name='{0} [{1}] Rankscore : {2}'.format(
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
                    overview = better_formatting(stats["stats"])
                else:
                    res = better_formatting(stats["stats"])
                    legend = stats["metadata"]["name"]
                    embed.add_field(name = '__{}__'.format(legend), value='```css\n{}```'.format(res), inline=False)
                    res = ''
            except Exception as e:
                print(f"{type(e).__name__} : {e}")
        embed.add_field(name = f'__Lifetime__', value='```css\n{}```'.format(overview),
                        inline=False)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg",
                        icon_url=ctx.guild.me.avatar_url)
        return embed

    @staticmethod
    def parse_user(args, platform):
        if len(args) > 1:
            platform = args.pop().lower()
        if platform in ["pc", "xbox", "psn"]:
            user = '%20'.join(args)
        return user, platform

    @commands.command(aliases=["s"])
    @trigger_typing
    async def stats(self, ctx, *args, platform = "pc"):
        """Displays apex stats for a given player (and platform)"""
        if not(len(args)):
            embed = discord.Embed(title="**Command**: **`a!stats`**",
                                description="**`a!stats [USERNAME]`**\n**`a!stats [USERNAME] < pc | xbox | psn >`**",
                                timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                                colour=self.colour)
            embed.add_field(name="Stats explanation",
                            value="- Stats are provided by [apex.tracker.gg](https://apex.tracker.gg/)"
                            " API (stats might not be fully exact)\n\n-"
                            " We can only get stats from selected banners\n\n"
                            "- To update a legend stats you have to pick the legend"
                            " wanted and then do **`a!stats [USERNAME] < pc | xbox | psn >`**\n\n"
                            "- It will keep all update you've done on your account\n\n"
                            "- The «Lifetime» value is just the sum of all banner"
                            " **AVAILABLE** and **SELECTED** on each legends")
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg",
                            icon_url=ctx.guild.me.avatar_url)
            return await ctx.send(embed=embed)
        try:
            finding = await ctx.send("`📡Fetching data...📡`")
            info = self.parse_user(list(args), platform)
            player, platform = info[0], info[1]
            player = player.replace('\\', '')
            if platform in ['pc','xbox','psn']:
                if len(player) >= 1:
                    stats = Stats(player, platform)
                    data = stats.data()
                    embed = self.embed_stats(ctx, data)
            else:
                embed = discord.Embed(title="❌Wrong platform!❌", colour=self.colour,
                description=f'{ctx.author.mention} Wrong platform! retry with `pc` | `xbox` | `psn`')
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg",
                                icon_url=ctx.guild.me.avatar_url)
                return await finding.edit(content="", embed=embed)
        except discord.errors.HTTPException: #if len(data) > 2000
            embed = discord.Embed(title="**Too Many Stats to show!**",
                                description=f"Sorry, but i couldn't show your stats. It's too big.\nYou can see your profile [__**here**__]({generate_url_profile(data['platformInfo']['platformSlug'], player)})",
                                timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                                colour=self.colour)
            embed.set_thumbnail(url= ctx.guild.me.avatar_url)
        except PlayerNotFound:
            embed = discord.Embed(title="❌Stats not found!❌",
                                description="Sorry but i couldn't found your Apex Legends Statistics.\n"
                                "You may have made a foul of strikes.\n\n"
                                "If you spelled it right then the API might be down.",
                                colour=self.colour,
                                timestamp=datetime.datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        except Exception as e:
            logging.error(f"{type(e).__name__} : {e}")
            embed = discord.Embed(title="Unknown error",
                                  description="Oops an unknown error occured sorry!",
                                  timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                                  colour=self.colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg",
                        icon_url=ctx.guild.me.avatar_url)
        await finding.edit(content="", embed=embed)

def setup(bot):
    bot.add_cog(Apex(bot))
