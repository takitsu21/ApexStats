# This cog is basically all the !support, !discord, !upvote, etc....
import discord
from discord.ext import commands

class Bot_Info:
    def __init__(self,bot):
      self.bot = bot
    
    @commands.command(pass_context=True)
    async def support(self,ctx):
      embed = (discord.Embed(title='Support me :', description='Hey if you like my work and want to support me, you can do it here [Patreon](https://www.patreon.com/takitsu) or here [Buy me a Kofi](https://ko-fi.com/takitsu)', colour=colour))
      embed.set_thumbnail(url=client.user.avatar_url)
      embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=client.user.avatar_url)
      await ctx.send(embed = embed)
      
    @commands.command(pass_context=True)
    async def discord(self,ctx):
      await ctx.send('{0.author.mention} https://discordapp.com/invite/wTxbQYb'.format(message))
    
    @commands.command(pass_context=True)
    async def invite(self,ctx):
      await ctx.send('{0.author.mention} https://discordbots.org/bot/551446491886125059/'.format(message))
      
    @commands.command(pass_context=True)
    async def upvote(self,ctx):
      await ctx.send('{0.author.mention} https://discordbots.org/bot/551446491886125059/vote'.format(message))

def setup(bot):
  bot.add_cog(Bot_Info(bot))
  print("Bot Info cog was added!")
    
