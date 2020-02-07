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
        patch_note = "https://www.reddit.com/r/apexlegends/comments/eyu1r7/season_4_assimilation_patch_notes/"
        embed = discord.Embed(colour=self.colour,
                              timestamp=dt.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name="**Patch Note** (Last -> 4 February 2020)",
                        value=f"[**Live patch**]({patch_note})")
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