import discord,asyncio
from discord.ext import commands
import ressources.web_scrapper as scrap_data

class Reddit:
  def __init__(self,bot):
    self.bot = bot
    
  @commands.command(pass_context=True)
  async def reddit(self,ctx):
		
    args = message.content.split(' ')
    try:
      reddit_parameter = args[1]
      if reddit_parameter == 'hot':
        msg = scrap_data.reddit_post('hot')
      elif reddit_parameter == 'top':
        msg = scrap_data.reddit_post('top')
      await ctx.send(embed = embed)
   	except Exception as e:
      embed = (discord.Embed(title='Command: !reddit', description='!reddit <hot/top> - Return random recent hot/top on r/apexlegends', colour=colour))
      embed.set_thumbnail(url=client.user.avatar_url)
      embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
      await ctx.send(embed = embed)
      
def setup(bot):
  bot.add_cog(Reddit(bot))
  print("Added Reddit cog from cogs")
