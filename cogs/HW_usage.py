import discord, time, datetime, psutil
from discord.ext import commands
from uptime import uptime

class HarwareInfo(commands.Cog):
    """Hardware info commands"""
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004


    @commands.command(pass_context=True)
    async def usage(self,ctx):
        embed = discord.Embed(title='**Apex Stats usage**',
                            colour=self.colour)
        embed.add_field(name="Uptime (HH:MM:SS)",value=str(datetime.timedelta(seconds=uptime())))
        embed.add_field(name="CPU Usage",value=f"{psutil.cpu_percent()}%")
        embed.add_field(name="Memory Usage",value=f"{psutil.virtual_memory()[2]}%")
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(HarwareInfo(bot))
    print("Added HardwareInfo")
