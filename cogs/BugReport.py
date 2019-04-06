import discord,asyncio, datetime, time
from discord.ext import commands
import ressources.mail_handler as mail


class BugReport(commands.Cog):
    """Report bug to dev"""
    def __init__(self, bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def bug(self, ctx, *message):
        message = ' '.join(message)
        mail.send_msg(ctx.author.name, message)
        embed = discord.Embed(title='**Bug Report**',
                            colour=self.colour,
                            description="Your bug report has been sent!\nThanks for the feedback",
                            icon_url=ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BugReport(bot))
    print("Added LeaderboardUpdate Cog from cogs")
