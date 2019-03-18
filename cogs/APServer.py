import discord,asyncio
from discord.ext import commands

colour = 0xc8db

class APServer:
  def __init__(self,bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def apserver(self,ctx):
     try:
      #
      Aps = scrap_data.ApexStatus()
      embed = discord.Embed(title='Apex Servers status', description='{}'.format(Aps.status()), colour=colour)
      embed.set_thumbnail(url=client.user.avatar_url)
      embed.set_footer(text="using apexlegendsstatus.com | Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
      await ctx.send(embed = embed)
     except:
      embed = discord.Embed(title='Apex Servers Status', description='[Apex Server Status](https://apexlegendsstatus.com/datacenters)', colour=colour)
      embed.set_thumbnail(url=client.user.avatar_url)
      embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
      await ctx.send(embed=embed)
      
      
#     
def setup(bot):
  bot.add_cog(APServer(bot))
  print("Added APServer cog!")
  
