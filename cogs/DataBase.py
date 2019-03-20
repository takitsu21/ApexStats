import discord
from discord.ext import commands
# import sqlite3

colour = 0xc8db

class DataBase(commands.Cog):
    """Save player profile and get player stats"""
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def profile(self, ctx, *args):
        embed = discord.Embed(title="This command is not yet implemented!",
                              colour=colour)
        await ctx.send(embed=embed)
        # try:
        #     if args[0] == 'save':
        #         pass
        #     elif len(args) == 0:
        #         return #Profile stats if exist in database
        # except:
        #     return


def setup(bot):
    bot.add_cog(DataBase(bot))
    print("Added DataBase cog!")
