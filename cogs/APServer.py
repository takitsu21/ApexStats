import discord
from discord.ext import commands
import src.web_scrapper as servers

class APServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def servers(self,ctx):
        try:
            finding = await ctx.send("`Checking servers...`")
            embed = discord.Embed(title='**Apex Servers Status**',
                                description=f'{servers.get_server_status()}',
                                colour=self.colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | using apexlegendsstatus.com", icon_url=ctx.guild.me.avatar_url)
        except Exception:
            embed = discord.Embed(title='__**Apex Servers Status**__',
                                description='[Apex Server Status](https://apexlegendsstatus.com/datacenters)',
                                colour=self.colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                            icon_url=ctx.guild.me.avatar_url)
        await finding.edit(content="", embed=embed)

def setup(bot):
    bot.add_cog(APServer(bot))