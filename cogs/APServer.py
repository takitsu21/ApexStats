import discord
from discord.ext import commands
import ressources.web_scrapper as scrap_data

colour = 0xc8db

class APServer(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def apserver(self,ctx):
        try:
        #
            Aps = scrap_data.ApexStatus()
            embed = discord.Embed(title='__**Apex Servers Status**__', description=f'{Aps.status()}', colour=colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="using apexlegendsstatus.com | Bot created by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
            await ctx.send(embed = embed)
        except:
            embed = discord.Embed(title='__**Apex Servers Status**__', description='[Apex Server Status](https://apexlegendsstatus.com/datacenters)', colour=colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(APServer(bot))
    print("Added APServer cog!")
