import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def aphelp(self,ctx):
        with open('commands.txt','r',encoding='utf8') as f:
            embed = discord.Embed(title='__Commands__:',
                                description=''.join(f.readlines()),
                                colour=self.colour)

        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Bot created by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)

        await ctx.author.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    print("Added Help cog from cogs")
