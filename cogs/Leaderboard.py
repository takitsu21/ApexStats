import discord,asyncio, datetime, time
from discord.ext import commands
import ressources.SqlManagment
from ressources.stats import *
from ressources.leaderboard_database import *

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def leaderboard(self, ctx):
        repr_leaderboard = ''
        rows = SqlManagment.read_table('leaderboard')
        d = datetime.date.today()
        embed = discord.Embed(title=f"**Leaderboard ({d.day}/{d.month}/{d.year})**",
                              timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                              colour=self.colour)
        for row in rows:
            if row[0] == '1':
                embed.add_field(name=f"__#{row[0]}__ **{row[1]}** :trophy:", value=f"Level **{row[2]}**", inline=False)
            else:
                embed.add_field(name=f"__#{row[0]}__ **{row[1]}**", value=f"Level **{row[2]}**", inline=False)

        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Leaderboard(bot))
