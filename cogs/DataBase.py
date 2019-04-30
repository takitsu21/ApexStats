import discord, time, datetime
from discord.ext import commands
import ressources.SqlManagment as SqlManagment
from ressources.stats import *
from ressources.exceptions import *


class DataBase(commands.Cog):
    """Save player profile and get player stats"""
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
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
                await ctx.send(f'{ctx.author.mention} Your profile is not yet registered in the database')
            else:
                SqlManagment.unlink(str(ctx.author.id))
                await ctx.send(f'{ctx.author.mention} `{player}` on `{platform}` has been successfully unlinked!')
            return
        if mode.lower() == "save":
            if len(args) == 0:
                await ctx.send("Please provide a username and plaftorm you want to save to your profile")
                return
            if len(args) >= 3:
                await ctx.send("Too many arguments provided!")
                return
            if len(args) == 1:
                embed = discord.Embed(title="__Command__: **a!profile**",
                                      description="**`a!profile save <username> <platform>(PC, XBOX, PSN)`** - Link profile to your discord\n`**a!profile display**` - returns your current saved profile\n`**a!profile unlink**` - Unlink your profile\n`**a!profile**` - Return your Apex Legends statistics if you linked a profile before",
                                      timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made by Taki#0853 (WIP)",
                                 icon_url=ctx.guild.me.avatar_url)
                await ctx.send(embed=embed)
            if len(args) == 2:
                finding = await ctx.send("`Working...`:tools:")
                player, platform = args[0], args[1]
                if platform.lower() in ['pc','xbox','psn']:
                    stats = Stats(player, platform)
                    if stats.exists():
                        embed = discord.Embed(title="Your profile has been saved!",
                                                description=f"You're in the database as `{player}` on `{platform}`",
                                                timestamp=datetime.datetime.utcfromtimestamp(time.time()), colour=self.colour)
                        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                        embed.set_footer(text="Made by Taki#0853 (WIP)",
                                            icon_url=ctx.guild.me.avatar_url)
                        SqlManagment.change("users",str(ctx.author.id),"username",str(player))
                        SqlManagment.change("users",str(ctx.author.id),"platform",str(platform))
                        await finding.edit(content="", embed=embed)
                        return
                    else:
                        await finding.edit(content=f"{ctx.author.mention} This profile doesn't exist!\nRetry you might spell it wrong")
                else:
                    await finding.edit(content=f"{ctx.author.mention} Wrong platform selected! retry with anotherplatform(PC, XBOX, PSN)")

        if(mode.lower() == "n"):

            row = SqlManagment.select('users', 'id', str(ctx.author.id))

            if row[0][1] == "NAN":
                embed = discord.Embed(title="**Command**: **a!profile**",colour=self.colour,
                                      description="**Sorry but I didn't find your profile on the database.**\n\n**`a!profile save <username> <platform>(PC, XBOX, PSN)`** - Link profile to your discord\n**`a!profile display`** - returns your current saved profile\n**`a!profile unlink`** - Unlink your profile\n**`a!profile`** - Return your Apex Legends statistics if you linked a profile before",
                                      timestamp=datetime.datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url=ctx.guild.me.avatar_url)
                embed.set_footer(text="Made by Taki#0853 (WIP)",
                                 icon_url=ctx.guild.me.avatar_url)
                await ctx.send(embed=embed)
                return
            else:
                client_icon = ctx.guild.me.avatar_url
                finding = await ctx.send('`Finding Stats...`')
                stats = Stats(row[0][1], row[0][2])
                data = stats.single_data()
                embed = discord.Embed(colour=self.colour,
                                      timestamp=datetime.datetime.utcfromtimestamp(time.time()))
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

def setup(bot):
    bot.add_cog(DataBase(bot))
