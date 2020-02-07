import discord
import time
import datetime
from discord.ext import commands
import src.sql as sql
from src.stats import *
from src.utils import generate_url_profile, better_formatting
from src.decorators import trigger_typing

class DataBase(commands.Cog):
    """Save player profile and get player stats"""
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

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
            name='{0} [{1}]  Rankscore : {2}'.format(
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
        embed.add_field(name = f'__Lifetime__', value='```css\n{}```'.format(overview), inline=False)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg", icon_url=ctx.guild.me.avatar_url)
        return embed

    @staticmethod
    def parse_user(args):
        platform = args.pop().lower()
        if platform in ["pc", "xbox", "psn"]:
            user = '%20'.join(args)
        return user, platform

    @commands.command(aliases=["p"])
    @trigger_typing
    async def profile(self,ctx, mode : str = "N", *args):
        userDb = sql.select('users', 'id', str(ctx.author.id))
        if not len(userDb):
            sql.addUser(str(ctx.author.id), "NAN")
        if mode.lower() == "display":
            user = sql.select('users', 'id', str(ctx.author.id))
            return await ctx.send(f"{ctx.author.mention} You're in the database as `{user[0][1]}` on `{user[0][2]}`")
        if mode.lower() == 'unlink':
            row = sql.select('users', 'id', str(ctx.author.id))
            player, platform = row[0][1], row[0][2]
            if player == 'NAN':
                embed=discord.Embed(title="⚠️Profile not registered!",
                description=f'{ctx.author.mention} Your profile is not yet registered in the database',
                timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                    icon_url=ctx.guild.me.avatar_url)
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(title="Profile unlinked",
                description=f'{ctx.author.mention} `{player}` on `{platform}` has been successfully unlinked!',
                timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                    icon_url=ctx.guild.me.avatar_url)
                sql.unlink(str(ctx.author.id))
                await ctx.author.send(embed=embed)
            return
        if mode.lower() == "save":
            if len(args) == 0:
                return await ctx.send("❌Please provide an username and the plaftorm you want to save to your profile")
            if len(args) == 1:
                embed = discord.Embed(title="Command: `a!profile`",
                                      description="**`a!profile save <username> <platform>(PC, XBOX, PSN)`** - Link profile to your discord\n`**a!profile display**` - returns your current saved profile\n`**a!profile unlink**` - Unlink your profile\n`**a!profile**` - Return your Apex Legends statistics if you linked a profile before",
                                      timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                                 icon_url=ctx.guild.me.avatar_url)
                await ctx.send(embed=embed)
            if len(args) >= 2:
                info = self.parse_user(list(args))
                player, platform = info[0], info[1]
                if platform in ['pc','xbox','psn']:
                    stats = Stats(player, platform)
                    if stats.exists():
                        embed = discord.Embed(title="✔️Your profile has been saved!✔️",
                                                description=f"You're profile is successfully linked!",
                                                timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                        embed.set_thumbnail(url=ctx.author.avatar_url)
                        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                                            icon_url=ctx.guild.me.avatar_url)
                        sql.change("users", str(ctx.author.id), "username", str(' '.join(player.split("%20"))))
                        sql.change("users", str(ctx.author.id), "platform", str(platform))
                        return await ctx.send(embed=embed)
                    else:
                        embed = discord.Embed(title=f"❌Profile `{player}` on `{platform}` doesn't exist❌",
                        description=f"{ctx.author.mention} This profile doesn't exist!\nRetry, you might have spelled it wrong",
                        timestamp=datetime.datetime.utcfromtimestamp(time.time()),colour=self.colour)
                        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                                            icon_url=ctx.guild.me.avatar_url)
                else:
                    embed = discord.Embed(title=f"❌Wrong platform❌",
                    description=f"{ctx.author.mention} Wrong platform selected!\nRetry with another platform `PC` | `XBOX` | `PSN`",
                    timestamp=datetime.datetime.utcfromtimestamp(time.time()),colour=self.colour)
                    embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                    embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                                        icon_url=ctx.guild.me.avatar_url)
                await ctx.send(embed=embed)
        if mode.lower() == "n":
            row = sql.select('users', 'id', str(ctx.author.id))

            if row[0][1] == "NAN":
                embed = discord.Embed(title="Command: `a!profile`",colour=self.colour,
                                      description="**Sorry but I didn't find your profile on the database.**\n\n**`a!profile save <username> <platform>(PC, XBOX, PSN)`** - Link profile to your discord\n**`a!profile display`** - returns your current saved profile\n**`a!profile unlink`** - Unlink your profile\n**`a!profile`** - Return your Apex Legends statistics if you linked a profile before",
                                      timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                                 icon_url=ctx.guild.me.avatar_url)
                await ctx.send(embed=embed)
            else:
                try:
                    finding = await ctx.send("`📡Fetching data...📡`")
                    client_icon = ctx.guild.me.avatar_url
                    player, platform = row[0][1], row[0][2]
                    player_check_whitespace = player.split(" ")
                    if len(player_check_whitespace) > 1:
                        player = '%20'.join(player_check_whitespace)
                    stats = Stats(player, platform)
                    data = stats.data()
                    embed = self.embed_stats(ctx, data)
                    return await finding.edit(content="", embed=embed)
                except discord.errors.HTTPException: #if len(data) > 2000
                    embed = discord.Embed(title="**Too Many Stats to show! || New data has been added to Apex Legends**",
                                          description=f"Sorry, but i couldn't show your stats. It's too big.\nYou can see your profile [__**here**__]({data['profile']}).",
                                          timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                    embed.set_thumbnail(url= client_icon)
                    embed.set_footer(text="data provided by apex.tracker.gg | Made with ❤️ by Taki#0853 (WIP)",
                                     icon_url=client_icon)
                    await finding.edit(content="", embed=embed)
                except PlayerNotFound:
                    embed = discord.Embed(title="❌Stats not found!❌", description="Sorry but i couldn't found your Apex Legends Statistics.\nYou may have made a foul of strikes.\n\nIf you spelled it right then the API might be down.",colour=self.colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                    embed.set_thumbnail(url = client_icon)
                    embed.set_footer(text="data provided by apex.tracker.gg | Made with ❤️ by Taki#0853 (WIP)",
                                    icon_url=client_icon)
                    await finding.edit(content="", embed=embed)
                except Exception as e:
                    print(type(e).__name__, e)
                    embed = discord.Embed(title="**Command**: **`a!stats`**",
                                          description="**`a!stats <username>`**\n**`a!stats <username> <platform>(pc,xbox,psn)`**",
                                          timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                    embed.add_field(name="Stats explanation", value="- Stats are provided by [apex.tracker.gg](https://apex.tracker.gg/) API (stats might not be fully exact)\n\n- We can only get stats from selected banners\n\n- To update a legend stats you have to pick the legend wanted and then do **`a!stats <username> <platform>`**\n\n- It will keep all update you've done on your account\n\n- The «All Stats» value is just the sum of all banner **AVAILABLE** and **SELECTED** on each legends")
                    embed.set_thumbnail(url=client_icon)
                    embed.set_footer(text="data provided by apex.tracker.gg | Made with ❤️ by Taki#0853 (WIP)",
                                     icon_url=client_icon)
                    await finding.edit(content="", embed=embed)

def setup(bot):
    bot.add_cog(DataBase(bot))
