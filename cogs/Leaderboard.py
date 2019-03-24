import discord,asyncio
from discord.ext import commands
import ressources.SqlManagment as SqlManagment
from ressources.stats import *

class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def leaderboard(self, ctx):
        embed = discord.Embed(title="**!leaderboard** This command is not yet implemented!",
                              colour=self.colour)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Leaderboard(bot))
    print("Leaderboard was added from cogs")
