import discord, time, datetime, asyncio
from discord.ext import commands
import ressources.SqlManagment as SqlManagment
from ressources.stats import *
from ressources.exceptions import *
from ressources.tools import generate_url_profile

class DataBase(commands.Cog):
    """Save player profile and get player stats"""
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    def embed_stats(self, ctx, data):
        legend, res, overview = "", "", ""
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
            url=generate_url_profile(data["platformInfo"]["platformSlug"],data["platformInfo"]["platformUserHandle"]),
            icon_url=data["platformInfo"]["avatarUrl"]
        )
        for i, stats in enumerate(data["segments"]):
            try:

                if i == 0:
                    for i, children in enumerate(stats["stats"]):
                        if i > 0:
                            overview += '**{}** : `{}`\n'.format(stats["stats"][children]["displayName"], str(int(stats["stats"][children]["value"])))

                else:
                    legend = stats["metadata"]["name"]
                    for children in stats["stats"]:
                        res += '**{}** : `{}`\n'.format(stats["stats"][children]["displayName"], str(int(stats["stats"][children]["value"])))
                    if len(res)>0:
                        embed.add_field(name = '__`{}`__'.format(legend), value='{}'.format(res), inline=True)
                        res = ''
            except Exception as e:
                print(f"{type(e).__name__} : {e}")
        embed.add_field(name = f'__`Lifetime`__', value='{}'.format(overview), inline=True)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg", icon_url=ctx.guild.me.avatar_url)
        return embed


    @commands.command(aliases=["p"])
    async def profile(self,ctx, mode : str = "N", *args):
        userDb = SqlManagment.select('users', 'id', str(ctx.author.id))
        if not len(userDb):
            SqlManagment.addUser(str(ctx.author.id),"NAN")
        if mode.lower() == "display":
            user = SqlManagment.select('users', 'id', str(ctx.author.id))
            await ctx.send(f"{ctx.author.mention} You're in the database as `{user[0][1]}` on `{user[0][2]}`")
            return
        if mode.lower() == 'unlink':
            row = SqlManagment.select('users', 'id', str(ctx.author.id))
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
                SqlManagment.unlink(str(ctx.author.id))
                await ctx.author.send(embed=embed)
            return
        if mode.lower() == "save":
            if len(args) == 0:
                await ctx.send("❌Please provide an username and the plaftorm you want to save to your profile")
                return
            if len(args) >= 3:
                await ctx.send("❌Too many arguments provided!")
                return
            if len(args) == 1:
                embed = discord.Embed(title="Command: `a!profile`",
                                      description="**`a!profile save <username> <platform>(PC, XBOX, PSN)`** - Link profile to your discord\n`**a!profile display**` - returns your current saved profile\n`**a!profile unlink**` - Unlink your profile\n`**a!profile**` - Return your Apex Legends statistics if you linked a profile before",
                                      timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                                 icon_url=ctx.guild.me.avatar_url)
                await ctx.send(embed=embed)
            if len(args) == 2:
                player, platform = args[0], args[1]
                if platform.lower() in ['pc','xbox','psn']:
                    stats = Stats(player, platform)
                    if stats.exists():
                        embed = discord.Embed(title="✔️Your profile has been saved!✔️",
                                                description=f"You're in the database as `{player}` on `{platform}`",
                                                timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                                            icon_url=ctx.guild.me.avatar_url)
                        SqlManagment.change("users",str(ctx.author.id),"username",str(player))
                        SqlManagment.change("users",str(ctx.author.id),"platform",str(platform))
                        await ctx.send(embed=embed)
                        return
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
        if(mode.lower() == "n"):

            row = SqlManagment.select('users', 'id', str(ctx.author.id))

            if row[0][1] == "NAN":
                embed = discord.Embed(title="Command: `a!profile`",colour=self.colour,
                                      description="**Sorry but I didn't find your profile on the database.**\n\n**`a!profile save <username> <platform>(PC, XBOX, PSN)`** - Link profile to your discord\n**`a!profile display`** - returns your current saved profile\n**`a!profile unlink`** - Unlink your profile\n**`a!profile`** - Return your Apex Legends statistics if you linked a profile before",
                                      timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                                 icon_url=ctx.guild.me.avatar_url)
                await ctx.send(embed=embed)
                return
            else:
                try:
                    client_icon = ctx.guild.me.avatar_url
                    stats = Stats(row[0][1], row[0][2])
                    data = asyncio.run(stats.data())
                    legend, res, overview = "", "", ""
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
                        url=generate_url_profile(data["platformInfo"]["platformSlug"],data["platformInfo"]["platformUserHandle"]),
                        icon_url=data["platformInfo"]["avatarUrl"]
                    )
                    for i, stats in enumerate(data["segments"]):
                        try:

                            if i == 0:
                                for i, children in enumerate(stats["stats"]):
                                    if i > 0:
                                        overview += '**{}** : `{}`\n'.format(stats["stats"][children]["displayName"], str(int(stats["stats"][children]["value"])))

                            else:
                                legend = stats["metadata"]["name"]
                                for children in stats["stats"]:
                                    res += '**{}** : `{}`\n'.format(stats["stats"][children]["displayName"], str(int(stats["stats"][children]["value"])))
                                if len(res)>0:
                                    embed.add_field(name = '__`{}`__'.format(legend), value='{}'.format(res), inline=True)
                                    res = ''
                        except Exception as e:
                            print(f"{type(e).__name__} : {e}")
                    embed.add_field(name = f'__`Lifetime`__', value='{}'.format(overview), inline=True)
                    embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg", icon_url=ctx.guild.me.avatar_url)
                    return await ctx.send(embed=embed)
                except discord.errors.HTTPException: #if len(data) > 2000
                    embed = discord.Embed(title="**Too Many Stats to show! / New data has been added to Apex Legends**",
                                          description=f"Sorry, but i couldn't show your stats. It's too big.\nYou can see your profile [__**here**__]({data['profile']}).",
                                          timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                    embed.set_thumbnail(url= client_icon)
                    embed.set_footer(text="data provided by apex.tracker.gg | Made with ❤️ by Taki#0853 (WIP)",
                                     icon_url=client_icon)
                    await ctx.send(embed=embed)
                except PlayerNotFound:
                    embed = discord.Embed(title="❌Stats not found!❌", description="Sorry but i couldn't found your Apex Legends Statistics.\nYou may have made a foul of strikes.\n\nIf you spelled it right then the API might be down.",colour=self.colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                    embed.set_thumbnail(url = client_icon)
                    embed.set_footer(text="data provided by apex.tracker.gg | Made with ❤️ by Taki#0853 (WIP)",
                                    icon_url=client_icon)
                    await ctx.send(embed=embed)
                except Exception as e:
                    embed = discord.Embed(title="**Command**: **`a!stats`**",
                                          description="**`a!stats <username>`**\n**`a!stats <username> <platform>(pc,xbox,psn)`**",
                                          timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                    embed.add_field(name="Stats explanation", value="- Stats are provided by [apex.tracker.gg](https://apex.tracker.gg/) API (stats might not be fully exact)\n\n- We can only get stats from selected banners\n\n- To update a legend stats you have to pick the legend wanted and then do **`a!stats <username> <platform>`**\n\n- It will keep all update you've done on your account\n\n- The «All Stats» value is just the sum of all banner **AVAILABLE** and **SELECTED** on each legends")
                    embed.set_thumbnail(url=client_icon)
                    embed.set_footer(text="data provided by apex.tracker.gg | Made with ❤️ by Taki#0853 (WIP)",
                                     icon_url=client_icon)
                    print(e)
                    await ctx.send(embed=embed)
                
            

def setup(bot):
    bot.add_cog(DataBase(bot))
