import discord
from discord.ext import commands
import ressources.web_scrapper as reddit

class Reddit(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004
        self.redditIcon = 'https://ya-webdesign.com/images/reddit-alien-png-3.png'

    @commands.command(pass_context=True)
    async def reddit(self, ctx, parameter: str = 'nan'):
        if parameter == 'nan':
            embed = (discord.Embed(title='Command: a!reddit',
                                   description='a!reddit <hot | top | best> - Return recent hot/top/best on r/apexlegends',
                                    colour=self.colour))
            embed.set_thumbnail(url=self.redditIcon)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
            await ctx.send(embed = embed)
            return
        try:
            if parameter in ['hot','top','best']:
                searchReddit = await ctx.send(f'`Looking for reddit {parameter} recents posts...`')
                desc = reddit.redditPost(parameter)
                embed = discord.Embed(title=f'**Reddit {parameter}** recents posts in the last 24 hours',
                                               description=desc,
                                                colour=self.colour)
                embed.set_thumbnail(url=self.redditIcon)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
                await searchReddit.edit(content = '', embed = embed)
            else:
                embed = (discord.Embed(title='Command: a!reddit',
                                       description=f'Wrong argument provided, `{parameter}` is not recognized sorry!\nTry with `a!reddit <hot | top | best>`',
                                        colour=self.colour))
                embed.set_thumbnail(url=self.redditIcon)
                embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
                await ctx.send(embed = embed)
        except Exception as e:
            embed = (discord.Embed(title='Command: a!reddit',
                                   description='a!reddit a!reddit <hot | top | best> - Return recent hot/top/best on r/apexlegends',
                                    colour=self.colour))
            embed.set_thumbnail(url=self.redditIcon)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
            print(e)
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Reddit(bot))
    print("Added Reddit cog from cogs")
