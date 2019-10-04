import discord
from discord.ext import commands
import src.web_scrapper as news
import datetime as dt
import time

class News(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def patch(self, ctx):
        patch_note = "https://www.reddit.com/r/apexlegends/comments/dbxzn4/season_3_meltdown_patch_notes/"
        embed = discord.Embed(colour=self.colour,
                              timestamp=dt.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name="**Patch Notes** (Last -> 1 October 2019)",
                        value=f"[**Live patch**]({patch_note})\n[**Season 2**](https://www.reddit.com/r/apexlegends/comments/c8bul6/season_2_battle_charge_begins_patch_notes_here/)\n[**06.20.2019**](https://www.reddit.com/r/apexlegends/comments/c2zc07/pc_client_patch_live_today_6202019/)\n[**06.04.2019**](https://www.reddit.com/r/apexlegends/comments/bwus7u/the_legendary_hunt_begins_today_patch_notes/)")
        embed.set_thumbnail(url="https://ya-webdesign.com/images/reddit-alien-png-3.png")
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def news(self, ctx):
        finding = await ctx.send('📡`Fetching news...`📡')
        desc = news.get_news()
        embed = discord.Embed(title='**Apex News** (from recent to oldest)',
                                description=desc,
                                colour=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)

        await finding.edit(content='', embed=embed)

def setup(bot):
    bot.add_cog(News(bot))