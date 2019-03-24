import discord
from discord.ext import commands
import ressources.web_scrapper as server


class APServer(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def apserver(self,ctx):
        try:
        #
            Aps = server.ApexStatus()
            embed = discord.Embed(title='__**Apex Servers Status**__', description=f'{Aps.status()}', colour=self.colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="using apexlegendsstatus.com | Bot created by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
            await ctx.send(embed = embed)
        except:
            embed = discord.Embed(title='__**Apex Servers Status**__', description='[Apex Server Status](https://apexlegendsstatus.com/datacenters)', colour=self.colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(APServer(bot))
    print("Added APServer cog!")
