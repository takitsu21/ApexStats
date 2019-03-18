import discord,asyncio
from discord.ext import commands

colour = 0xc8db

class Leaderboard:
  def __init__(self,bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def leaderboard(self,ctx):
    embed = discord.Embed(title="This command is not yet implemented!",color=0xc8db)
    await ctx.send(embed=embed)
    
def setup(bot):
  bot.add_cog(Leaderboard(bot))
  print("Leaderboard was added from cogs")
