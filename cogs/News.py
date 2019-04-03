import discord
from discord.ext import commands
import ressources.web_scrapper as _news

class News(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def news(self, ctx, lang: str = 'en'):
        finding = await ctx.send('`Looking for news...`')
        news = _news.ApexNews(lang)
        desc = news.get_news()
        embed = discord.Embed(title='**Apex News** (from recent to oldest)',
                                description=desc,
                                colour=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)

        await finding.edit(content='',embed=embed)

def setup(bot):
    bot.add_cog(News(bot))
    print("Added News cog from cogs")
