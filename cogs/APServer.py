import discord
import datetime
import time
from discord.ext import commands
import ressources.web_scrapper as server


class APServer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def patch(self,ctx):
        patch_note = "https://www.reddit.com/r/apexlegends/comments/c8bul6/season_2_battle_charge_begins_patch_notes_here/"
        embed = discord.Embed(colour=self.colour,
                              timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name="**Patch Notes** (Last -> 2 July 2019)", value=f"[**Live patch**]({patch_note})\n[**06.20.2019**](https://www.reddit.com/r/apexlegends/comments/c2zc07/pc_client_patch_live_today_6202019/)\n[**06.04.2019**](https://www.reddit.com/r/apexlegends/comments/bwus7u/the_legendary_hunt_begins_today_patch_notes/)")
        embed.set_thumbnail(url="https://ya-webdesign.com/images/reddit-alien-png-3.png")
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def servers(self,ctx):
        try:
            finding = await ctx.send("`Checking servers...`")
            Aps = server.ApexStatus()
            embed = discord.Embed(title='**Apex Servers Status**',
                                  description=f'{Aps.status()}',
                                   colour=self.colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="using apexlegendsstatus.com | Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url) 
        except Exception:
            embed = discord.Embed(title='__**Apex Servers Status**__', description='[Apex Server Status](https://apexlegendsstatus.com/datacenters)', colour=self.colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
        await finding.edit(content="", embed=embed)

def setup(bot):
    bot.add_cog(APServer(bot))
    print("Added APServer cog!")
