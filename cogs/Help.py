import discord
from discord.ext import commands

class Help:
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(pass_context)
  async def help(self,ctx):
    with open('commands.txt','r',encoding='utf8') as f:
        embed = discord.Embed(title='__Commands__:', description=''.join(f.readlines()), colour=colour)
    await ctx.send(embed=embed)
    
def setup(bot):
  bot.add_cogs(Help(bot))
  print("Added Help cog from cogs")
    
  
