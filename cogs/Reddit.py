import discord
from discord.ext import commands
import ressources.web_scrapper as scrap_data

class Reddit(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def reddit(self, ctx, parameter):
        try:
            if parameter == 'hot':
                msg = scrap_data.reddit_post(parameter)
            elif parameter == 'top':
                msg = scrap_data.reddit_post(parameter)
            await ctx.send(msg)
        except Exception as e:
            embed = (discord.Embed(title='Command: !reddit',
                                   description='!reddit <hot/top> - Return random recent hot/top on r/apexlegends',
                                    colour=self.colour))
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Reddit(bot))
    print("Added Reddit cog from cogs")
